from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
import time
import pyperclip

# Create your views here.
def main(request):
    return render(request, "main.html")

def login(request):
    if request.method == "POST":
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        driver = webdriver.Chrome("")
        driver.get("https://nid.naver.com/nidlogin.login")
        time.sleep(1)
        idin = driver.find_element(By.CSS_SELECTOR, "#id")
        idin.click()
        pyperclip.copy(id)
        actions = ActionChains(driver)
        # actions.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()
        actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(1)
        pwin = driver.find_element(By.CSS_SELECTOR, "#pw")
        pwin.click()
        pyperclip.copy(pw)
        actions = ActionChains(driver)
        # actions.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.COMMAND).perform()
        actions.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
        time.sleep(1)
        subu = driver.find_element(By.CSS_SELECTOR, "#log\.login")
        subu.click()
        time.sleep(1)
        if "검색어를 입력해 주세요" in driver.page_source:
            print(f"맞음 : {id}, {pw}")
            return redirect("https://nid.naver.com/nidlogin.login")
        else:
            print(f"틀림 : {id}, {pw}")
            return redirect("https://nid.naver.com/nidlogin.login")
        
    return render(request, "login.html")