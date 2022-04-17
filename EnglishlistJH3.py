#! pip install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium import webdriver
browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.eigo-duke.com/tango/chu3.html")
from selenium.webdriver.common.by import By
###英語全部見るクリック
elem_btn = browser.find_element(By.CLASS_NAME, "btn4")
elem_btn.click()
sleep(5) 
elems_English = browser.find_elements(By.CLASS_NAME, "eng")
elems_Japanese = browser.find_elements(By.CLASS_NAME, "jap")
sleep(5)
Englist=[  ]
for elem_English in elems_English :
    Eng=elem_English.text

    Englist.append(Eng)
Japlist=[  ]
for elem_Japanese in elems_Japanese :
    Jap=elem_Japanese.text
    
    Japlist.append(Jap)

###データフレーム
import pandas as pd
df = pd.DataFrame()
df["英語"]= Englist
df["日本語"]= Japlist
df=df.iloc[:-4, :]
df.to_csv("中学3年生英単語一覧.csv",index=False)