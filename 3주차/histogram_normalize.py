import cv2
import numpy as np
import matplotlib.pyplot as plt

# 1. 이미지 읽기 (그레이스케일로 읽어야 평활화가 가능합니다)
image = cv2.imread('Hawkes.jpg', 0)

if image is None:
    print("이미지를 찾을 수 없습니다.")
else:
    # 2. 히스토그램 평활화 적용
    equalized = cv2.equalizeHist(image)

    # 3. 결과 비교 시각화
    plt.figure(figsize=(12, 6))

    # 원본 이미지와 히스토그램
    plt.subplot(221)
    plt.title('Original Image')
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(222)
    plt.title('Original Histogram')
    plt.hist(image.flatten(), 256, [0, 256], color='r')

    # 평활화된 이미지와 히스토그램
    plt.subplot(223)
    plt.title('Equalized Image')
    plt.imshow(equalized, cmap='gray')
    plt.axis('off')

    plt.subplot(224)
    plt.title('Equalized Histogram')
    plt.hist(equalized.flatten(), 256, [0, 256], color='b')

    plt.tight_layout()
    plt.show()

    # OpenCV 윈도우로 직접 확인하고 싶을 때
    cv2.imshow('Before & After', np.hstack((image, equalized)))
    cv2.waitKey(0)
    cv2.destroyAllWindows()