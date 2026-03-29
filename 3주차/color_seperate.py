import cv2

# 이미지를 읽기 (파일명이 Len.png인지 Lena.png인지 확인하세요!)
image = cv2.imread('Len.png')

# 이미지 읽기가 성공적이지 못한 경우 처리
if image is None:
    print("이미지를 열 수 없습니다. 파일 경로를 확인하세요.")
else:
    # Blue, Green, Red 성분 분리
    blue, green, red = cv2.split(image)
    
    # 각각의 성분 행렬 출력 (콘솔창 확인)
    print("Blue Component Matrix:")
    print(blue)
    
    # 이미지 윈도우로 확인
    cv2.imshow('Original Image', image)
    
    # 채널별 출력 (각 채널은 2차원 배열이므로 흑백 영상처럼 보입니다)
    cv2.imshow('Blue Component', blue)
    cv2.imshow('Green Component', green)
    cv2.imshow('Red Component', red)

    cv2.waitKey(0)
    cv2.destroyAllWindows()