# authd written in python

I needed authd for IRC but couldn't get the one supplied with centos 7 to work correctly so I wrote my own.

Works well enough to get you to IRC. Lots of features probably missing...

# Installation

1. Install xinetd
2. copy auth to /etc/xinetd.d
3. mkdir -p /opt/authd
4. copy in.authd.py to /opt/authd
5. chmod a+x /opt/authd/in.authd.py
6. Enable & start xinetd.service

If you have selinux enabled, you probably need to set correct security context:

`chcon system_u:object_r:inetd_child_exec_t:s0 /opt/authd/in.authd.py`
