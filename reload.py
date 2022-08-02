# %%
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager  # バージョンに合わせて自動アップデート
from selenium.webdriver.common.by import By

email = 'xp700203@gmail.com'
pw = 'nao700203'
# %%
# ログイン
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome(executable_path="chromedriver/chromedriver.exe")
driver.get("https://moneyforward.com/sign_in")
# driver.find_element_by_class_name("_11ZPO93b").click()
driver.find_element(By.XPATH, '//*[text()="メールアドレスでログイン"]').click()
driver.find_element(By.XPATH, '//*[@name="mfid_user[email]"]').send_keys(email)
driver.find_element(By.XPATH, '//*[contains(@class,"submitBtn")]').click()
driver.find_element(By.XPATH, '//*[@name="mfid_user[password]"]').send_keys(pw)
driver.find_element(By.XPATH, '//*[contains(@class,"submitBtn")]').click()
# %%
# 更新
driver.get("https://moneyforward.com/accounts")
reload_btns = driver.find_elements(By.XPATH, '//*[@data-disable-with="更新"]')
for btn in reload_btns:
    btn.click()
driver.close()
