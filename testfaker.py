# testfaker.py

import qrcode
import cv2
from faker import Faker

my = Faker()
for k in range(20):
    print(my.name())

print()
for k in range(10):
    print(my.ipv4_private())

print()
data = Faker('ko_KR')    
for k in range(10):
    print(data.address())

print()    
for k in range(10):
    print(data.name())


#에러 ModuleNotFoundError: No module named 'qrcode'
#에러 C:\dongaAI\ch01\day0123>pip install cv2
# C:\dongaAI\ch01\day0123>pip install qrcode
# C:\dongaAI\ch01\day0123>pip install opencv-python  cv2만 다름
# C:\dongaAI\ch01\day0123>pip install faker


