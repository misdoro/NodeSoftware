#!/usr/bin/python

import sys
import os
import traceback
from pprint import pprint


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



from export.export_functions import *

auxdict = export_aux_tables()
nodedict = export_nodes()
export_species(auxdict,nodedict)
export_species_names(auxdict)
export_species_nodes(nodedict)


