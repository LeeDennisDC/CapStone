import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

# 1. 이미지 읽기 (그레이스케일)
img = cv2.imread('Hawkes.jpg', 0)

if img is None:
    print("이미지를 찾을 수 없습니다. 파일명을 확인하세요: Hawkes.jpg")
    sys.exit()

# 2. 히스토그램 스트레칭 (Min-Max Stretching) 수행
# 공식: P_out = (P_in - min) * (255 / (max - min))
img_min = np.min(img)
img_max = np.max(img)

# 계산 시 데이터 타입에 주의 (float으로 계산 후 다시 uint8로 변환)
stretched = (img - img_min) * (255.0 / (img_max - img_min))
stretched = np.clip(stretched, 0, 255).astype(np.uint8)

# 3. 결과 시각화
plt.figure(figsize=(12, 7))

# 원본 이미지와 히스토그램
plt.subplot(221)
plt.title(f'Original (Min:{img_min}, Max:{img_max})')
plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(222)
plt.title('Original Histogram')
plt.hist(img.flatten(), 256, [0, 256], color='gray')

# 스트레칭 결과 이미지와 히스토그램
plt.subplot(223)
plt.title(f'Stretched (Min:{stretched.min()}, Max:{stretched.max()})')
plt.imshow(stretched, cmap='gray', vmin=0, vmax=255)
plt.axis('off')

plt.subplot(224)
plt.title('Stretched Histogram')
plt.hist(stretched.flatten(), 256, [0, 256], color='blue')

plt.tight_layout()
plt.show()

# OpenCV 창으로 결과 확인
cv2.imshow('Original vs Stretched', np.hstack((img, stretched)))
cv2.waitKey(0)
cv2.destroyAllWindows()