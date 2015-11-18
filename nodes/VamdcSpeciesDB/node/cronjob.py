#!/usr/bin/python

import sys
import os
import traceback


def append_base_path(depth):
  import sys
  import os
  mypath=os.path.abspath(__file__)
  for i in range(0,depth):
    mypath=os.path.dirname(mypath)
  sys.path.append(mypath)
  return mypath


#Add path to settings.py to system path
append_base_path(2)

#Initialize django
import django
import settings
django.setup()


#Do the work on database
import node.update_functions as update
update.update_nodes()       #Search for new nodes in the registry&update registered ones
update.query_active_nodes() #Update species for nodes that are marked active