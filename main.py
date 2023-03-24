from get_menu import take_menu
from making_photo import makeing_pic
from datetime import datetime

hour = datetime.now().hour

if 0 < hour <= 6:
    timing = 0
elif 7 < hour <= 12:
    timing = 1
else:
    timing = 2

menu = take_menu(1)

makeing_pic(menu) if menu != None else print("사진을 제작할 수 없습니다.")
