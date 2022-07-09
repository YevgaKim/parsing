import time
from bs4 import BeautifulSoup
from selenium import webdriver
import json

def get_data(url):
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36.useragent.override")
    driver = webdriver.Chrome(
            executable_path="C:\\Users\\ЯкименкоЄвгенійСергі\\source\\repos\\work\\chromedriver",
            options=options
        )
    try:
        
        driver.get(url=url)
        time.sleep(30)
    
        with open("index_selenium.html", "w",encoding="utf-8") as file:
            file.write(driver.page_source)
    
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    with open("index_selenium.html","r",encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src,"lxml")

    all_students = soup.find(class_="table table-bordered table-hover table-sm").find("tbody").find_all("tr")
    res = []
    list_students=[]
    for tr in all_students:
        td = tr.find_all('td')
        row = [tr.text.strip() for tr in td if tr.text.strip()]
        if row:
            res.append(row)
    count=0
    gr=res[0][5]
    for item in res:
        count+=1
        print(f"Операция номер {count}, осталось {len(res)-count}")
        time.sleep(1)
        list_students.append(
            {
                "Место":item[0],
                "Имя": item[1],
                "Баллы":item[2],
                "Акад.баллы":item[3]
            }
        )
    with open(f"scholarship ranking_gr_{gr}.json","w",encoding="utf-8") as file:
        json.dump(list_students, file, indent=4, ensure_ascii=False)   
    
    
def main():
    get_data("https://erp.kname.edu.ua/progress/scholarship-rating")

if __name__=="__main__":
    main()



    