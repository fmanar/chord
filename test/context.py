# set up easy import of chord package
import os
import sys
# at top of path list, insert the directory above the one containing this file
sys.path.insert(0, 
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    )
# import package under this module
import chord