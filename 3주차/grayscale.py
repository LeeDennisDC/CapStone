import cv2

# Lena.png 파일을 흑백(Grayscale) 모드로 읽기
# 0은 cv2.IMREAD_GRAYSCALE을 의미합니다.
image = cv2.imread('Lena.png', 0)

if image is None:
    print("이미지를 읽을 수 없습니다. 파일명과 경로를 확인해 주세요.")
else:
    # 윈도우 창에 이미지 표시
    cv2.imshow('Grayscale Lena', image)
    
    # 키 입력을 대기 (0은 아무 키나 누를 때까지 무한 대기)
    cv2.waitKey(0)
    
    # 생성된 모든 윈도우 창 닫기
    cv2.destroyAllWindows()