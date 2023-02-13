from src.db import ScrapingUrlsDB
from src.myMail import Email
from modules import helpers
from threading import Thread
from time import sleep
import schedule

class makeRequests:
    """A class for sending emails to a list of recipients based on a set of URLs.

    The class uses the ScrapingUrlsDB class to interact with a database that contains
    the URLs and email addresses, the myMail class to send the emails, and the helpers
    module to check whether a store associated with a given URL is open.
    """
    def __init__(self):
        """Initializes the makeRequests class by instantiating the required objects
        and retrieving the list of URLs and email addresses from the database.
        """
        self._db_threaded = None      
        self._email = Email()
        self._threads = []

    
    def json_of_emails(self, db_conn: ScrapingUrlsDB):
        """Retrieves a list of email addresses for each URL from the database
        and stores them in a dictionary.

        Returns:
            A dictionary where each key is a URL and the associated value is a list
            of email addresses associated with the URL.
        """
        json_emails = dict()
        for url in db_conn.get_list_of_urls():
            json_emails[url] = db_conn.get_emails_by_url(url)
        
        return json_emails
    
    def send_mail_if_open(self):
        """Iterates through the list of URLs and sends an email to the list of email
        addresses associated with each URL for which the store is open.

        The method uses the is_store_open function from the helpers module to check
        whether a store is open. If the store is open, the method sends an email to
        the list of email addresses associated with the URL, and then deletes the
        associated row from the database.
        """
        for url in self._db_threaded.get_list_of_urls():            
            try:
                is_open = helpers.is_store_open(url)
                if is_open is True:
                    for mail in self.json_of_emails(self._db_threaded)[url][0].split(","):
                        print(mail)
                        self._threads.append(Thread(target=self._email.send_message, args=(mail, url)))
                        self._db_threaded.delete_row_by_url(url)
                    self.start_threads()    
                else:
                    self._db_threaded.update_last_checked_by_url(url)
            except KeyError as e:
                print("Got error", e)
                continue
        sleep(5)
    
    def start_threads(self):
        """Starts all threads in the _threads instance variable and then waits for them to finish.

        This method iterates through the list of threads, starts each thread, and then waits
        for each thread to finish before moving on to the next thread. Once all threads have
        finished, the _threads list is emptied.
        """
        try: 
            for thread in self._threads:
                print("send mail..")            
                thread.start()
            for thread in self._threads:
                thread.join()
            self._threads = []
        except Exception as e:
            print(f"Got error in threads {e}")
            self._threads = []
            pass
    
    def start_schedule(self):
        print("Started scanning..")
        self._db_threaded = ScrapingUrlsDB()
        schedule.every(10).seconds.do(self.send_mail_if_open)
        while True:
            schedule.run_pending()
            sleep(10)