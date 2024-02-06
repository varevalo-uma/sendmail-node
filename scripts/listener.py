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
userid = 'youremail@gmail.com'
passwd = 'yourpassword'

# SMTP Server data
server = 'smtp.gmail.com' # domain or ip
port = 587  # for starttls


def callback(msg):

    try:
        #rospy.loginfo('\njson object:\n' + msg.data)

        # parse the json object
        data = json.loads(msg.data)

        # Prepare the message
        email            = MIMEText(data['body'])
        email['From']    = formataddr( (data['robot'], userid) )
        email['To']      = data['to']
        email['Subject'] = data['subject']

        # Create a SMTP client
        smtp = smtplib.SMTP(server, port)

        # Create a secure SSL context
        smtp.starttls(context = ssl.create_default_context())

        smtp.login(userid, passwd) # login to the server

        #rospy.loginfo('\nmessage:\n' + email.as_string())
        smtp.send_message(email) # send the email

    except Exception as e:
        rospy.logerr(e) # print any error messages

    finally:
        smtp.quit()



if __name__ == '__main__':

    try:
        rospy.Subscriber('chatter', String, callback) # listening at /chatter

        rospy.init_node('listener')

        # Set the SMTP server data above if you don't use ROS params.
        userid = rospy.get_param('~userid', userid)
        passwd = rospy.get_param('~passwd', passwd)
        server = rospy.get_param('~server', server)
        port   = rospy.get_param('~port', port)

    except Exception as e:
        rospy.logerr(e) # print any error messages

    else:
        rospy.spin() # waiting for new messages

