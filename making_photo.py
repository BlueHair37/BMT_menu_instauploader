import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np

def makeing_pic(menu_list):
    img = cv2.imread("./assets/img.png")

    pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_img)

    font_path = "/Library/Fonts/AppleGothic.ttf"  # 맥북 기본 한글 폰트 경로
    font = ImageFont.truetype(font_path, 25)
    font_color = (0,0,0)

    x_pos = 220
    y_pos = 100

    for i, menu in enumerate(menu_list):
        text_width, text_height = font.getsize(menu)
        x = x_pos - text_width / 2
        y = y_pos + i * 30
        draw.text((x, y), menu, font=font, fill=font_color)

    # 다시 OpenCV Image로 변환
    img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    cv2.imwrite("./assets/result.png", img)
