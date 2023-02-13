import smtplib
from email.message import EmailMessage
from src.consts import CREDENTIALS

class Email:
    """Class for sending emails using Gmail SMTP server."""
    
    def __init__(self):
        """Initialize the email class with the user's credentials."""
        self._username = CREDENTIALS["EMAIL"]
        self._password = CREDENTIALS["PASSWORD"]
        
    def send_message(self, rec_email, shop_url):
        """
        Send an email to the specified recipient with the given shop url.
        
        Args:
        - rec_email (str): The recipient's email address.
        - shop_url (str): The URL of the shop to include in the email body.
        
        Returns:
        - bool: True if the email was sent successfully, False otherwise.
        """
        msg = EmailMessage()
        msg['Subject'] = 'Ariel and Maor Project'
        msg['From'] = self._username
        msg['To'] = rec_email
        msg_body = """Hey, Thanks for using our  website!\nThe shop you chose is now Open\nlink: {}\nHave a nice meal!""".format(shop_url)
        msg.set_content(msg_body)
        print("sent message to {}".format(rec_email))
        try:
            smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
            smtp_obj.starttls()
            smtp_obj.login(self._username, self._password)
            smtp_obj.send_message(msg)
            smtp_obj.quit()
            return True
        except smtplib.SMTPException:
            print("Got into exception..")
            return False
        
    def __str__(self):
        return 'Email class for sending emails using Gmail SMTP server'
    
    def __repr__(self):
        return 'Email()'
