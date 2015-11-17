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

#print append_base_path(4)
print append_base_path(2)




import django

import settings
django.setup()

#from django.contrib import admin

#from nodes.VamdcSpeciesDB.node.models import *

import node.update_functions

node.update_functions.process_species('CDMS')