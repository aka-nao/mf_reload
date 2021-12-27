# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os

email = os.environ['email']
pw = os.environ['pw']
# %%
# ログイン
options = Options()
options.add_argument('--headless')
options.add_argument(
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')

try_num=3
for i in range(1,try_num+1):
    try:
        driver = webdriver.Chrome(options=options)
        try:
            # ログイン
            driver.get("https://moneyforward.com/sign_in")
            try:
                driver.find_element(By.XPATH, '//*[text()="メールアドレスでログイン"]').click()
                try:
                    driver.find_element(By.XPATH, '//*[@name="mfid_user[email]"]').send_keys(email)
                    driver.find_element(By.XPATH, '//*[contains(@class,"submitBtn")]').click()
                    driver.find_element(By.XPATH, '//*[@name="mfid_user[password]"]').send_keys(pw)
                    driver.find_element(By.XPATH, '//*[contains(@class,"submitBtn")]').click()
                    try:
                        # 更新
                        driver.get("https://moneyforward.com/accounts")
                        reload_btns = driver.find_elements(By.XPATH, '//*[@data-disable-with="更新"]')
                        for btn in reload_btns:
                            btn.click()
                    except:
                        print(f"try No.{i} Error : all reload")
                except:
                    print(f"try No.{i} Error : email&password send_keys, submit")
            except:
                print(f"try No.{i} Error : メールアドレスでログイン")
        except:
            print(f"try No.{i} Error : access https://moneyforward.com/sign_in")
    except:
        print(f"try No.{i} Error : selenium start driver")
    
    driver.close()
