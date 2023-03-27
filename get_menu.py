import requests, json, re
from datetime import datetime

def take_menu(prm):
    key = "9a45c0ca0c724287b1dc3312e0a6b041"
    url = f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={key}"
    city_code = "C10"
    school_code = "1421117"
    today_date = str(datetime.today().year)+str(datetime.today().month).zfill(2)+str(datetime.today().day).zfill(2)

    response = requests.get(url+f"&Type=json&ATPT_OFCDC_SC_CODE={city_code}&SD_SCHUL_CODE={school_code}&MLSV_YMD={today_date}")
    response_dict = json.loads(response.text)

    with open("./menu.json", 'w', encoding='utf-8') as f: # 디버그용 json파일 저장
        json.dump(response_dict, f, ensure_ascii=False, indent="\t")

    try:
        lunch_menu = response_dict["mealServiceDietInfo"][1]["row"][prm]["DDISH_NM"]
        lunch_menu = lunch_menu.replace("<br/>","")
        lunch_menu = re.sub(r"\([^)]*\)","",lunch_menu)
        lunch_menu = lunch_menu.replace("  ","\n")
        lunch_menu = lunch_menu.split()
        return lunch_menu

    except IndexError as e:
        print("메뉴가 존재하지 않습니다.")
        return None

    except BaseException as e:
        print(f"에러가 발생하였습니다.(사유:{e})")
        return None

