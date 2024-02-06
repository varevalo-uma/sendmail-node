#!/usr/bin/env python

## This node sends emails by means of sendmail, which is listening the "chatter" topic.
## Be careful, the struct of json object must be as indicated below:
##    eg: email = '{ 
##          "robot" : "name",
##          "to" : "to@example.com", 
##          "subject" : "Hi!",
##          "body" : "Some text. Bye!. V"
##      }'

import rospy
from std_msgs.msg import String


if __name__ == '__main__' :

    try:
        pub = rospy.Publisher('chatter', String, queue_size = 10)

        rospy.init_node('talker', anonymous = True)

        # email encapsulated as json object
        email = '{ "robot": "name",\
            "to": "to@example.com",\
            "subject": "Hi!",\
            "body": "Some text. Bye!. V"\
        }'

        #rospy.loginfo('\njson object:\n' + email)
        pub.publish(email)


    except Exception as e:
        rospy.logerr(e) # print any error messages

