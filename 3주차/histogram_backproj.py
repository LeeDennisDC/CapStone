import cv2
import numpy as np

# 1. 이미지 읽기
target = cv2.imread('Hawkes.jpg')
if target is None:
    print("이미지를 찾을 수 없습니다: Hawkes.jpg")
    exit()

# 2. ROI(관심 영역) 설정 (Hawkes.jpg 내 추출하고자 하는 특정 영역 좌표로 수정 가능)
# 예: 중앙 부근의 특정 질감 영역
h, w = target.shape[:2]
roi = target[h//3:h//2, w//3:w//2]

# 3. BGR -> HSV 변환
hsv_target = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# 4. ROI의 히스토그램 계산 (H, S 채널 사용)
roi_hist = cv2.calcHist([hsv_roi], [0, 1], None, [180, 256], [0, 180, 0, 256])

# 5. 히스토그램 정규화
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# 6. 히스토그램 역투영 적용
back_proj = cv2.calcBackProject([hsv_target], [0, 1], roi_hist, [0, 180, 0, 256], 1)

# 7. 마스크 처리 및 결과 추출
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
cv2.filter2D(back_proj, -1, kernel, back_proj)
_, mask = cv2.threshold(back_proj, 50, 255, cv2.THRESH_BINARY)
result = cv2.bitwise_and(target, target, mask=mask)

# 8. 결과 출력
cv2.imshow('Target (Hawkes)', target)
cv2.imshow('ROI', roi)
cv2.imshow('Backprojection Map', back_proj)
cv2.imshow('Result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()