from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 인스타그램 로그인 정보
username = "202231102@bmt.hs.kr"
password = "kang0513@@#"

# 업로드할 이미지 파일 경로
image_path = "result.png"

# 셀레니움 드라이버 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 인스타그램 로그인 페이지 열기
driver.get('https://www.instagram.com/accounts/login/')

# 로그인 폼에 아이디와 비밀번호 입력 후 로그인 버튼 클릭
time.sleep(5)
username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
username_input.send_keys(username)
password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
password_input.send_keys(password)
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# 로그인 후 인스타그램 홈페이지로 이동
time.sleep(5)
driver.get('https://www.instagram.com/')

# 이미지 업로드 페이지로 이동
time.sleep(5)
create_btn = driver.find_element(By.XPATH)

# 파일 업로드 창 띄우기
time.sleep(10)
upload_button = driver.find_element(By.XPATH, "//input[@type='file']")
upload_button.send_keys(image_path)

# 업로드 완료 후 게시물 작성
time.sleep(5)
next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
next_button.click()
caption_input = driver.find_element(By.CSS_SELECTOR, "textarea[aria-label='Write a caption…']")
caption_input.send_keys('My result image')
share_button = driver.find_element(By.XPATH, "//button[text()='Share']")
share_button.click()

# 드라이버 종료
driver.quit()