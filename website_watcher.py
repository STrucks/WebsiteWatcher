import datetime
import os
import time

import requests
import smtplib
from email.message import EmailMessage


class WebsiteWatcher:

    def __init__(self):
        self.url = "https://www.hula-hoop-shop.eu/Hoopomania-Titan-Hoop-Hula-Hoop-mit-32-Magneten-31kg"
        self.active_div = self._get_relevant_div_as_text()

    def start(self):
        """
        This is the main function of the project. it will periodically check if the website changed.
        :return:
        """
        self._test_email()
        while True:
            try:
                current_div = self._get_relevant_div_as_text()
                if current_div != self.active_div:
                    print("Div has changed!!")
                    self._send_email_changed()
                    self.active_div = current_div
                else:
                    print("[%s] Div has not changed..." % datetime.datetime.now().strftime("%c"))
            except Exception as e:
                print("Something went wrong... More luck next time...")
            finally:
                time.sleep(300)

    def _get_relevant_div_as_text(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            http_text = response.text
            relevant_div = http_text[
                           http_text.find("<div id=\"artikelstamm\""):http_text.find("<div id=\"artikel_bilder\"")]
            return relevant_div
        else:
            print("%d: %s" % (response.status_code, response.text))
            return None

    def _send_email_changed(self):
        with open("email_template.txt") as fp:
             # Create a text/plain message
             msg = EmailMessage()
             msg.set_content(fp.read() + "\nTimestamp: %s" % datetime.datetime.now().strftime("%c"))

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = "TOP SECRET"
        msg['From'] = os.environ.get("SENDER")
        msg['To'] = os.environ.get("RECEIVER")


        # Send the message via our own SMTP server.
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()

    def _test_email(self):
        msg = EmailMessage()
        msg['Subject'] = "Application Start"
        msg['From'] = "chr@strucksilvanien.com"
        msg['To'] = os.environ.get("RECEIVER")

        # Send the message via our own SMTP server.
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()
