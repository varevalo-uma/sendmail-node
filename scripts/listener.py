#!/usr/bin/env python

## Simple listener that send mails using postfix & mailutils & google.
## You can send emails easyly from command line as indicated next:
##    eg. rostopic pub /chatter std_msgs/String '{data: "{ \"to\": \"garthim.uma@gmail.com\", \"subject\":\"test\", \"body\":\"hey\"}"}'

import rospy
from std_msgs.msg import String
import json
import subprocess

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " %s", data.data)
    email = json.loads(data.data)
    #print(email["to"])
    #print(email["subject"])
    #print(email["body"])
    cmd = 'echo "' + email["body"] + '" | mail -s "' + email["subject"] + '" ' + email["to"]
    #print(cmd)
    subprocess.run(cmd, shell=True)


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
