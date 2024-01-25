#!/usr/bin/env python

## Simple talker that send mails by means of a relay that listens the "chatter" topic.
## Be carefull, the struct of json objecti must be as indicated next:
##    eg: '{ "to" : "garthim.uma@gmail.com", "subject" : "test", "body" : "This is a test. bye. V" }'

import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    mail = '{ "to" : "garthim.uma@gmail.com", "subject" : "test", "body" : "This is a test. bye. V" }'
    rospy.loginfo(mail)
    pub.publish(mail)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass