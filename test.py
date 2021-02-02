import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

PATH = "drivers/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://na.op.gg/summoner/userName=NewtMo")

rank = driver.find_element_by_class_name("TierRank").text
lp = driver.find_element_by_class_name("LeaguePoints").text
wins = driver.find_element_by_class_name("wins").text
loss = driver.find_element_by_class_name("losses").text
print(rank,lp,wins,loss)

