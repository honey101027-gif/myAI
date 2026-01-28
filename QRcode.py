# QRcode.py

import qrcode
import time
import cv2

url = 'https://www.google.com'
qr_img = qrcode.make(url)
qr_img.save(stream='./images/gg_QR.png')
print('QRtesting~~~저장성공')



img = cv2.imread('./images/gg_QR.png')
cv2.imshow('title',img)
print('QRtesting~~~열기성공')
cv2.waitKey(0)
cv2.destroyAllWindows()

#에러 ModuleNotFoundError: No module named 'qrcode'
#에러 C:\dongaAI\ch01\day0123>pip install cv2

# C:\dongaAI\ch01\day0123>pip install faker
# C:\dongaAI\ch01\day0123>pip install qrcode
# C:\dongaAI\ch01\day0123>pip install opencv-python  (cv2만 다름)



