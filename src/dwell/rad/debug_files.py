"""A simple module to wrap the built in open and close functions so that it prints
OPENING and CLOSING every time a file is opened/closed, and can print out the list
of all open files if requested. This module can be used to track down file handle leaks.
"""

import __builtin__
openfiles = set()
oldfile = __builtin__.file
class newfile(oldfile):
    """Class to wrap the open file function"""
    def __init__(self, *args):
        self.x = args[0]
        print("*** OPENING {0} ***".format(str(self.x)))
        oldfile.__init__(self, *args)
        openfiles.add(self)

    def close(self):
        """wraps the close function"""
        print("*** CLOSING {0} ***".format(str(self.x)))
        oldfile.close(self)
        openfiles.remove(self)

oldopen = __builtin__.open
def newopen(*args):
    """The function to wrap the file/open commands, so that we can log the filenames being
    opened"""
    return newfile(*args)
__builtin__.file = newfile
__builtin__.open = newopen

def listOpenFiles():
    """Returns the list of open files"""
    return openfiles #

def printOpenFiles():
    """Prints the list of open files"""
    print ("*** {0} OPEN FILES: [{1}]".format((len(openfiles), ", ".join(f.x for f in openfiles))))