import sys
import cv2
import numpy as np

img = cv2.imread('./assets/dog.jpg')
if img is None:
    sys.exit("파일을 찾을 수 없습니다.")

# I = round(0.299*R + 0.587*G + 0.114*B)
# TODO: 컬러 사진을 흑백사진으로 변환하기

cvt_img = np.round(img[:, :, 2]*0.299 + img[:, :, 1]*0.587 + img[:, :, 0]*0.114).astype(np.uint8)

cv2.imshow("gray_img", cvt_img)
cv2.waitKey()
cv2.destroyAllWindows()