import re
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import time
from threading import Thread
from src.db import ScrapingUrlsDB
from src.makeRequests import makeRequests

def get_urls_by_email(email):
    if is_valid_email(email):
        db = ScrapingUrlsDB()
        answer = db.get_urls_by_email(email)
        db.close()
        return answer
    else:
        return None


def create_request_db(email, url) -> bool:
    if is_valid_email(email):
        if is_valid_wolt_url(url):
            db = ScrapingUrlsDB()
            answer = db.insert_email_into_url(url, email)
            db.close()
            if answer:
                return True    
    return False


def is_valid_email(email: str) -> bool:
    # use a regular expression to check if the email address is in the correct format
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.search(regex, email):
        # the email address is in the correct format
        return True
    else:
        # the email address is not in the correct format
        return False


def is_valid_wolt_url(url: str) -> bool:
    # use a regular expression to check if the URL is in the correct format
    regex = r"https://wolt.com/[a-z]{2}/[a-z]{3}/[a-z-]+/[a-z0-9-]+"
    if re.search(regex, url):
        # the URL is in the correct format
        return True
    else:
        # the URL is not in the correct format
        return False


def is_future_orders(url_text) -> bool:
    try:
        future_order = url_text.find("div", attrs={"data-test-id" : "CartViewButtonInformationBlock"}).text
        if "סגור" in future_order:
            print("is future")
            return False
        print("Not closed")
        return True
    except Exception:
        print("Got exception..")
        return True 


def time_compare(hours_to_check: str) -> bool:
    try:
        now = time.strftime("%H:%M")
        
        hours_to_check = hours_to_check.split("–")
        opening_time_string = hours_to_check[0].replace(".", ":")
        closing_time_string = hours_to_check[1].replace(".", ":")
        if "00" <= closing_time_string.split(":")[0] < "06":
            closing_time_string = str(int(closing_time_string.split(":")[0]) + 24) + ":00" 

        # print(f"{opening_time_string=}, {closing_time_string=}, {now=}")
        if opening_time_string < now < closing_time_string:
            return True
        
        return False

    except Exception as e:
        return False   

        

def is_store_open(URL) -> bool:
    # Check if the URL is in Hebrew and convert it if necessary
    URL = URL.replace("/en/", "/he/") if "/he/" not in URL else URL

    # Send a GET request to the URL and check the response status
    response = requests.get(URL)
    if response.status_code != 200:
        return False

    # Parse the response HTML using BeautifulSoup
    soup = bs(response.text, "lxml")

    # Find the store information button and extract the store status and time
    inspect_data = soup.find("button", attrs={"data-test-id": "venue-information-button"})
    store_info = inspect_data.text.split(":")
    is_open = store_info[0]
    store_time = store_info[1].strip()

    # Check if the store is open and if the time is correct
    if "פתוח" in is_open and time_compare(store_time):
        # Check if the store accepts future orders
        print("there's open")
        if is_future_orders(soup):
            return True

    return False


def start_scanning():
    make_requests = makeRequests()
    # if make_requests._db_threaded is None:
    t = Thread(target=make_requests.start_schedule)
    t.daemon = True
    t.start()
    
if __name__ == "__main__":
    pass