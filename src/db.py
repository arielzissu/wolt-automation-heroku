import sqlite3
from datetime import datetime


class ScrapingUrlsDB:
    def __init__(self):
        # self.con = sqlite3.connect('../database/wolt.db')
        self.con = sqlite3.connect('./database/wolt.db')
        cur = self.con.cursor()

        # Create table
        cur.execute('''CREATE TABLE IF NOT EXISTS scraping_urls
                    (URL UNIQUE, emails, lastChecked)''')
        self.con.commit()

    def insert_email_into_url(self, shop_url: str, rec_email: str) -> bool:
        """
        Insert the given email into the given shop url in the database.
        
        Args:
        - shop_url (str): The shop URL to insert the email into.
        - rec_email (str): The email to insert into the shop URL.
        
        Returns:
        - bool: True if the email was inserted successfully, False otherwise.
        """
        if not shop_url or not rec_email:
            return False
        
        try:
            cur = self.con.cursor()
            
            # Check if the shop URL exists in the database
            if self.is_url_exists_in_db(shop_url):
                # Check if the email is already registered to the shop URL
                cur.execute('''SELECT * FROM scraping_urls WHERE URL=? AND emails LIKE ?''', (shop_url, '%' + rec_email + '%'))
                if cur.fetchone():
                    return False
                else:
                    # Update the shop URL with the given email
                    cur.execute('''UPDATE scraping_urls SET emails=emails || ',' || ? WHERE URL=?''', (rec_email, shop_url))
                    self.con.commit()
                    return True
            else:
                # Insert the shop URL and email into the database
                now = datetime.now()
                cur.execute('''INSERT INTO scraping_urls VALUES (?, ?, ?)''', (shop_url, rec_email, now))
                self.con.commit()
                return True
        except sqlite3.Error:
            print("Database connection failed.")
            return False

    def is_url_exists_in_db(self, shop_url: str) -> bool:
        """
        Check if the given shop URL exists in the database.
        
        Args:
        - shop_url (str): The shop URL to check.
        
        Returns:
        - bool: True if the shop URL exists in the database, False otherwise.
        """
        try:
            cur = self.con.cursor()
            cur.execute('''SELECT * FROM scraping_urls WHERE URL=?''', (shop_url,))
            if cur.fetchone():
                return True
            else:
                return False
        except sqlite3.Error:
            return False
    
    
    def get_urls_by_email(self, email: str):
        """
        Get a list of URLs that are associated with the given email in the database.
        
        Args:
        - email (str): The email address to get URLs for.
        
        Returns:
        - list: A list of URLs that are associated with the given email.
        """
        cur = self.con.cursor()
        cur.execute('''SELECT URL FROM scraping_urls WHERE emails LIKE ?''', ('%' + email + '%',))
        return [row[0] for row in cur.fetchall()]

    
    def get_list_of_urls(self):
        cur = self.con.cursor()
        cur.execute('''SELECT URL FROM scraping_urls''')
        return [row[0] for row in cur.fetchall()]
    
    def get_emails_by_url(self, url):
        cur = self.con.cursor()
        cur.execute('''SELECT emails FROM scraping_urls WHERE URL=?''', (url,))
        return [row[0] for row in cur.fetchall()]

    def delete_row_by_url(self, url):
        cur = self.con.cursor()
        cur.execute('''DELETE FROM scraping_urls WHERE URL=?''', (url,))
        self.con.commit()
        
    def get_last_check(self, url):
        cur = self.con.cursor()
        cur.execute('''SELECT lastChecked from scraping_urls WHERE URL=?''', (url,))
        return [row[0] for row in cur.fetchall()]

    def update_last_checked_by_url(self, url):
        cur = self.con.cursor()
        print("updated {}".format(url))
        cur.execute('''UPDATE scraping_urls SET lastChecked=? WHERE URL=?''', (datetime.now(), url))
        self.con.commit()

    def close(self):
        self.con.close()
        

        
def testing():
    db = ScrapingUrlsDB()
    
    # Test inserting a new shop URL and email into the database
    # assert db.insert_email_into_url('http://www.example1.com', 'test1@example.com') == True

    # # Test inserting a new shop URL and email into the database
    # assert db.insert_email_into_url('http://www.example2.com', 'test2@example.com') == True

    # # Test inserting an existing shop URL and new email into the database
    # assert db.insert_email_into_url('http://www.example1.com', 'test3@example.com') == True

    # # Test inserting an existing shop URL and existing email into the database
    # assert db.insert_email_into_url('http://www.example1.com', 'test3@example.com') == False

    # # Test inserting a new shop URL and existing email into the database
    # assert db.insert_email_into_url('http://www.example3.com', 'test3@example.com') == True

    # # Test checking if an existing shop URL exists in the database
    # assert db.is_url_exists_in_db('http://www.example1.com') == True

    # # Test checking if a non-existent shop URL exists in the database
    # assert db.is_url_exists_in_db('http://www.example4.com') == False

    print(db.get_urls_by_email("test3@example.com"))
    db.close()


if __name__ == '__main__':
    testing()
    
