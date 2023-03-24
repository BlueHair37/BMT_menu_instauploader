import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

id = "202231102@bmt.hs.kr"
pswd = "kang0513@@#"

#드라이버 설치 및 크롬 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #또는 chromedriver.exe
driver.get('https://www.instagram.com/')

time.sleep(10)
#아이디 프롬프트
id_input = driver.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(1) > div > label > input")
id_input.send_keys(id)

#비밀번호 프롬프트
pswd_input = driver.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(2) > div > label > input")
pswd_input.send_keys(pswd)

#로그인 버튼 클릭
login_btn = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3)")
login_btn.click()

time.sleep(10)
#업로드 버튼 클릭
upload_btn = driver.find_elements(By.CLASS_NAME, "_ab6-")
upload_btn[5].click()

time.sleep(5)
#파일 업로드 여기서 개막히노 막막티비다 하
uploader = driver.find_elements(By.XPATH,"//input[@type='file']")
uploader[0].send_keys("./assets/result.png")

time.sleep(100)
driver.quit()


