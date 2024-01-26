#!/usr/bin/env python

## This node sends mails by means of sendmail, which is listening the "chatter" topic.
## Be careful, the struct of json object must be as indicated next:
##    eg: email = '{ 
##          "robot" : "name",
##          "to" : "to@example.com", 
##          "subject" : "Hi!",
##          "body" : "This is a test. bye. V"
##      }'

import rospy
from std_msgs.msg import String


def talker():

    pub = rospy.Publisher('chatter', String)
    rospy.init_node('talker', anonymous=True)

    email = "{ \
        'robot' : 'name', \
        'to' : 'to@example.com', \
        'subject' : 'Hi!', \
        'body' : 'This is a test. bye. V' \
    }"
    rospy.loginfo(email)

    pub.publish(email)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
