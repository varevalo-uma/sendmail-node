# sendmail

## Some info

E-mail continues being a good solution for receiving info from many apps. Everybody has a mail client in his desktop, laptop, or smartphone, so you do not need additional tools for that purpose. So, why do we not use e-mail for sending updates about the status of a mobile robot that, for example, explores a building for hours :-)?.

This package contains a python script that uses the [stmplib](https://docs.python.org/es/3/library/smtplib.html) for sending the messages. The only requirement is having an e-mail account, and the configuration data of the SMTP server of your e-mail provider. You can deploy your own mail solution using, as for example, [postfix](https://www.postfix.org/) or another, but the easiest way is to use platforms as Google or Outlook that provide that service.

## The code

The main script, called `listener.py`, implements a simple SMTP client that connects to the Google SMTP servers. So, if you wish to test the script as it is, you must count with a valid Google Account, and the option "Allow less secure apps" activated.

If you have not done that before, you can follow these steps:
- [Create a new Google account](https://accounts.google.com/signup).
- Turn [Allow less secure apps to ON](https://myaccount.google.com/lesssecureapps). Be aware that this makes it easier for others to gain access to your account.

Once you have the configuration data of your SMTP server (ie, domain, and port), the e-mail user, and the password for sending mails from less secure apps, you must include that information in the `listener.py` file as follow:

### listener.py

```
...

# Google credentials
from_addr = "my.email.address@gmail.com"
password = "my.email.password"

# Configuration data for Google SMTP server
server = "smtp.gmail.com" # domain or ip
port = 587  # for starttls

...

```

Observe that the connection is secure; I create a valid SSL credentials for securing the communications.

Finally, how does the script work? `listener.py` provides a (std_msgs.msg) String subscriber, called `/chatter`, as channel for receiving the messages, and conveniently routes them to the SMTP server. The e-mail body, the sender, the recipient address, and the subject must be encapsulated as a JSON object with the following set of pairs attribute-value:

```
email = '{ 
	"robot" : "name",
	"to" : "to@example.com",
	"subject" : "Hi!",
	"body" : "This is a test. bye. V"
	}'
```

The package contains the script `talker.py` as proof of usage. Next, you will find the source:

### talker.py

```
#!/usr/bin/env python

import rospy
from std_msgs.msg import String

pub = rospy.Publisher('chatter', String, queue_size = 10)
rospy.init_node('talker', anonymous=True)

email = '{\
	"robot" : "name",\
	"to" : "varevalo@uma.es",\
	"subject" : "Hi!",\
	"body" : "This is a test. bye. V"\
}'
# rospy.loginfo(email)

pub.publish(email)
```

Finally, for testing both scripts you can use the following commands (I suppose you know to deployl a ROS node from sources):

```
$ roscore
$ rosrun sendmail listener.py &
$ rosrun sendmail talker.py
```

Many improvements can be done: additional validations on the JSON object format, SMTP data configurable via ROS params, rich HTML messages (MIME support), attached files,... but that, for future releases :-D. 

## License

[Creative Commons by 4.0 deed (CC4)](https://creativecommons.org/licenses/by/4.0/).
