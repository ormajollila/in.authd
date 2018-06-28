#!/bin/python

# Add \r to all prints because original ircd seems to expect it.

import sys, os, re

def main():

  if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
  else:
    query = sys.stdin.readline()
  
  query = query.strip().split(',')
  
  if len(query) == 2:
    query_local_port = query[0]
    query_remote_port = query[1]
  
    # Accept only int
    try:
      query_local_port = int(query_local_port)
      query_remote_port = int(query_remote_port)
      
    except:
      print "%s , %s : ERROR : INVALID-PORT\r" % (str(query_local_port), str(query_remote_port))
      sys.exit(1)

    uid = get_connection_uid(query_local_port, query_remote_port)
    
    if uid:
      username = get_username(uid)
      
      if username:
        print "%s , %s : USERID : UNIX : %s\r" % (str(query_local_port), str(query_remote_port), str(username))

      else:
        print "%s , %s : ERROR : NO-USER\r" % (str(query_local_port), str(query_remote_port))

    else:
      print "%s , %s : ERROR : NO-USER\r" % (str(query_local_port), str(query_remote_port))
      
  else:
    print "0 , 0 : ERROR :INVALID-PORT\r"

#
# Get connection user id
#
# Parameters: query_local_port, query_remote_port
# Returns: uid if possible, else -1
#
# 
def get_connection_uid(query_local_port, query_remote_port):

  uid = False

  # Try to open connection details.
  ports = []
  try:
    if os.path.isfile("/proc/net/tcp"):
      ports.extend(open("/proc/net/tcp", "r").readlines())
    if os.path.isfile("/proc/net/tcp6"):
      ports.extend(open("/proc/net/tcp6", "r").readlines())
      
  except:
    print "%s , %s : ERROR : UNKNOWN-ERROR\r" % (str(query_local_port), str(query_remote_port))
    sys.exit(1)
    
  for line in ports:


    # Tidy up line
    line = re.sub(r'([a-zA-Z0-9])\s+', r'\1 ', line.strip()).split(' ')
    
    if len(line) > 11:
    
      if len(line[1].split(":")) > 1:
        tcp_local_port = line[1].split(':')[1]
        tcp_remote_port = line[2].split(':')[1]
  
        try:
          tcp_local_port = int(tcp_local_port, 16)
          tcp_remote_port = int(tcp_remote_port, 16)
          
        except:
          pass
        
        if tcp_local_port == query_local_port and tcp_remote_port == query_remote_port:
          uid = line[7]
          
  return uid
  
#
# Get username by uid
#
# Paramers: uid
# Returns: username if possible, else -1
#
def get_username(uid):

  username = False

  try:
    fp = open("/etc/passwd", "r")
    
  except:
    sys.exit(1)
    
  for line in fp:
    line = line.split(':')
    if line[2] == uid:
      username = line[0]
      break
      
  fp.close()

  return username
  
main()