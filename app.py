import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pymongo
import datetime
import socket
import uuid
from selenium.webdriver.common.proxy import Proxy, ProxyType
import pandas as pd


def fetch_proxies():
    resp = requests.get('https://www.sslproxies.org/')
    df = pd.read_html(resp.text)[0]
    filtered_df = df[(df['Https'] == 'yes') & (df['Google'] == 'yes') & (df['Anonymity'] == 'elite proxy')]
    proxies = filtered_df[['IP Address', 'Port']].values.tolist()
    return proxies

proxies = fetch_proxies()

# Path to your ChromeDriver
driver_path = 'C:\\Users\\agd\\Downloads\\chromedriver-win64\\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)


try:
    driver.get('https://twitter.com/i/flow/login')
    wait = WebDriverWait(driver, 20)

    username = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[autocomplete=username]'))
    )
    username.send_keys("agd_27")

    login_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[role=button].r-13qz1uu'))
    )
    login_button.click()

    password = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[type=password]'))
    )
    password.send_keys("agdtwitter@45")

    login_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid*=Login_Button]'))
    )
    login_button.click()

    direct_message_link = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid=AppTabBar_DirectMessage_Link]'))
    )

    wait = WebDriverWait(driver, 20)

    driver.get('https://x.com/explore/tabs/trending')
    time.sleep(15)


    trending_topics = set()

    xpath_template = '//*[@data-testid="trend"]//div[2]/span'

    while len(trending_topics) < 5:
        try:
            elements = driver.find_elements(By.XPATH, xpath_template)
            for element in elements:
                topic = element.text
                if topic and len(trending_topics) < 5 and topic not in trending_topics:
                    trending_topics.add(topic)
                    print(f"{topic}")
        except Exception as e:
            print(f"Error: {e}")
            pass


    # MongoDB connection
    client = pymongo.MongoClient("mongodb+srv://daberaoakshay1:6ufKPdL0R1iXg9dv@cluster0.7lpipcb.mongodb.net/")
    db = client.trending_data
    collection = db.trending_topics

    # Collecting additional information
    unique_id = str(uuid.uuid4())
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = socket.gethostbyname(socket.gethostname())

    # Preparing data to insert
    data_to_insert = {
        "_id": unique_id,
        "nameoftrend1": list(trending_topics)[0] if len(trending_topics) > 0 else None,
        "nameoftrend2": list(trending_topics)[1] if len(trending_topics) > 1 else None,
        "nameoftrend3": list(trending_topics)[2] if len(trending_topics) > 2 else None,
        "nameoftrend4": list(trending_topics)[3] if len(trending_topics) > 3 else None,
        "nameoftrend5": list(trending_topics)[4] if len(trending_topics) > 4 else None,
        "date_and_time": end_time,
        "ip_address": ip_address
    }

    # Inserting data into MongoDB
    collection.insert_one(data_to_insert)

finally:
    # Close the browser
    driver.quit()



