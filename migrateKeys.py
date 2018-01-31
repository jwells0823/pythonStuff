#!/usr/bin/python
#Written by: jamie.wells@logisticare.com
#parses the ssh config file, determines if you need to add a key for no password ssh
#   adds the keys to the servers that are missing the key. You may need to type your
#   password multiple times.

import subprocess
import sys

#file location, full complete path
FILENAME="/Users/jamie.wells/.ssh/config"
file = open(FILENAME, "r")

userId=""
thisHost=""
COMMAND="ls .ssh"

#find the hosts
for aLine in file:
   value=aLine.split()
   if len(value) >0: #length is more than zero, there is data here.

      if value[0] == "Host":
         thisHost=value[1]

      if value[0] == "User":
         userId=value[1]

      if len(thisHost)>0:
         print "accessing server %s@%s" % (userId, thisHost)
         p1=subprocess.Popen(["ssh", "%s" % thisHost, COMMAND], 
                           shell=False,
			   stdout=subprocess.PIPE,
			   stderr=subprocess.PIPE)
         result = p1.stdout.readlines()
         if result == []:
            error = p1.stderr.readlines()
            print >>sys.stderr, "ERROR: %s" % error
         else:
            print result
         userId=""
         thisHost=""
      
