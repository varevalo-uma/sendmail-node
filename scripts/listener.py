#!/usr/bin/env python

## Send emails by means of a Google Account.

import rospy
from std_msgs.msg import String

from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr
import json
import smtplib, ssl


# Google credentials
from_addr = "your@email.com"
password = "yourpassword"

# SMTP Server
server = "smtp.gmail.com" # domain or ip
port = 587  # for starttls

def callback(data):

    rospy.loginfo(rospy.get_caller_id() + " " + data.data)

    # parse the mail message
    email = json.loads(data.data)

    to_addr = email["to"]

    # Prepare the message
    message = MIMEText(email["body"])
    message['Subject'] = email["subject"]
    message['From'] = formataddr( (email["robot"], from_addr) )
    message['To'] = to_addr

    # Try to log in to server and send the email
    try:

        # Create a secure SSL context
        ctx = ssl.create_default_context()

        # Create a SMTP client
        smtp = smtplib.SMTP(server, port)

        smtp.starttls(context = ctx) # secure the connection

        smtp.login(from_addr, password)

        #print("\nmessage: \n", message.as_string())
        smtp.send_message(message)

    except Exception as e:

        # Print any error messages to stdout
        print(e)

    finally:
        smtp.quit()


def listener():

    rospy.init_node('listener')

    rospy.Subscriber("chatter", String, callback) # listening at /chatter

    # waiting for new messages
    rospy.spin()


if __name__ == '__main__':
    try :
        listener()
    except rospy.ROSInterruptException :
        pass
