from flask import Flask
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)
email = os.environ['email']
pw = os.environ['pw']


def reload():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get("https://moneyforward.com/sign_in")
    driver.find_element_by_class_name("_11ZPO93b").click()
    driver.find_element_by_name("mfid_user[email]").send_keys(email)
    driver.find_element_by_class_name("submitBtn").click()
    driver.find_element_by_name("mfid_user[password]").send_keys(pw)
    driver.find_element_by_class_name("submitBtn").click()

    driver.get("https://moneyforward.com/accounts")
    reload_btns = driver.find_elements(
        By.XPATH, '//*[@data-disable-with="更新"]')
    for btn in reload_btns:
        btn.click()
    driver.close()


@app.route("/")
def hello():
    reload()
    return "Hello, world!!"


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
