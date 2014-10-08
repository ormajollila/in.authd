# authd written in python

I needed authd for IRC but couldn't get the one supplied with centos 7 to work correctly so I wrote my own.

Works well enough to get you to IRC. Lots of features probably missing...

# Installation

1. Install xinetd
2. copy auth to /etc/xinet.d
3. mkdir -p /opt/authd
4. copy in.authd.py to /opt/authd
5. Enable & start xinetd.service

