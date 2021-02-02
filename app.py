import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from flask import Flask
PATH = "drivers/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://na.op.gg/summoner/userName=NewtMo")
app = Flask(__name__)


@app.route('/')
def hello_world():
    rank = driver.find_element_by_class_name("TierRank").text
    lp = driver.find_element_by_class_name("LeaguePoints").text
    wins = driver.find_element_by_class_name("wins").text
    loss = driver.find_element_by_class_name("losses").text
    return rank


if __name__ == '__main__':
    app.run()
