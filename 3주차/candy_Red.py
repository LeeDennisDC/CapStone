import cv2
import numpy as np
import sys

# 1. 이미지 읽기 (같은 폴더에 있어야 합니다)
image = cv2.imread('candy.png')

# 이미지 로드 확인
if image is None:
    print("이미지를 열 수 없습니다. 파일명을 확인하세요: candy.png")
    sys.exit()

# 2. BGR에서 HSV 색 공간으로 변환
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 3. 빨간색 범위 정의 (HSV 채널 단위: H[0~179], S[0~255], V[0~255])
# 빨간색은 색상(H) 영역이 양 끝에 걸쳐 있습니다.

# 범위 1: 색상 0 ~ 10 근처
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)

# 범위 2: 색상 160 ~ 179 근처
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([179, 255, 255])
mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)

# 두 마스크를 합칩니다 (OR 연산)
red_mask = cv2.bitwise_or(mask1, mask2)

# 4. 원본 이미지에 마스크를 적용하여 빨간색만 추출 (AND 연산)
# 마스크가 흰색(255)인 부분만 원본 색상이 남고, 검은색(0)인 부분은 검게 됩니다.
red_extracted = cv2.bitwise_and(image, image, mask=red_mask)

# 5. 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Red Mask', red_mask)           # 빨간색 영역을 흰색으로 보여주는 마스크
cv2.imshow('Red Extracted', red_extracted) # 추출된 결과

cv2.waitKey(0)
cv2.destroyAllWindows()