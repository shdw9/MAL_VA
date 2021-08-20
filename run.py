from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from colorama import Fore, init
import os
from time import sleep
import warnings

init()
init(convert=True)

warnings.filterwarnings("ignore", category=DeprecationWarning)
options = Options()
#options.headless = True #uncomment this if you want to see the browser doing its work
options.add_argument("--log-level=3")
#options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
os.system('cls')
driver = webdriver.Chrome(options=options)

watchedanime = []

def getVA(): #asks for VA, and checks grabbed list
    VAlink = input("\nEnter the voice actor's MAL link: ")
    print("Navigating to voice actor's profile ...")
    driver.get("" + VAlink)
    sleep(3)
    VAanimes = driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/table/tbody/tr/td[2]/table[1]/tbody/tr")
    #print(VAanimes[1].text.split("\n")[0])
    print("\nChecking for similarities ...")
    sleep(2)
    print("\n----------------------------------------\n")
    for anime in VAanimes:
        #print(anime.text.split("\n")[0].rstrip())
        if anime.text.split("\n")[0].rstrip() in watchedanime:
            print("[" + anime.text.split("\n")[0].rstrip() + "] as " + anime.text.split("\n")[2] + "\n")
    print("----------------------------------------")
    getVA()

        
def getAnime(): #grabs all watched anime from profile
    print("\nGrabbing all anime from MAL profile ...")
    animes = driver.find_elements_by_xpath("//tbody[@class='list-item']")
    for anime in animes:
        if "Watch Episode Video" in anime.text:
            #print(anime.text.split("\n")[0].split("Watch Episode Video")[0].split(" ", 1)[1].rstrip())
            watchedanime.append(anime.text.split("\n")[0].split("Watch Episode Video")[0].split(" ", 1)[1].rstrip())
        else:
            #print(anime.text.split("\n")[0].split(" ", 1)[1].rstrip())
            watchedanime.append(anime.text.split("\n")[0].split(" ", 1)[1].rstrip())
    print('Finished grabbing ' +  str(len(watchedanime)) + " anime from your MAL profile!")
    getVA()

def getProfile(): #checks if valid profile
    username = input('Enter your MAL username: ')
    print("Navigating to " + username + "'s MAL profile ...")
    driver.get("https://myanimelist.net/animelist/" + username)
    try:
        if (driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/div[2]/div")):
            print("Not a valid MAL username!")
            quit()
    except:
        print("MAL profile is valid!")
        sleep(3)
        getAnime()
        pass

getProfile()
