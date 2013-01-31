"""A dictionary class that ignores case."""

class CaselessDict(dict):
    """A dictionary with case-free keys:
        
    All keys are converted to lower case, values are unchanged,
    otherwise it behaves as a dictionary.

    >a=CaselessDict.CaselessDict()
    >a["one"]=1.0
    >print a["one"]
    1.0
    >a["One"]=2.0
    >print a["one"]
    2.0
    
    This dictionary is used by the netcdf library to allow 
    access to netcdf variables without using the strictly
    correct case. It might fail if the NetCDF file has 
    multiple variables distinguished only by case, 
    but don't do that!
        
    """
    def __init__(self, other=None):
        if other is not None:
        # Doesn't do keyword args
            if isinstance(other, dict):
                for key, val in other.items():
                    dict.__setitem__(self, key.lower(), val)
            else:
                for key, val in other:
                    dict.__setitem__(self, key.lower(), val)
        super(CaselessDict, self).__init__()
        
    def __getitem__(self, key):
        """Read dictionary element
         
        Arguments:
        
        * key -- The key whose value is returned
         
        Output:
        
        * The value corresponding to the key, or an exception.
        """
        try:
            if key is None: 
                raise KeyError
            return dict.__getitem__(self, key.lower())
        except AttributeError as exception:
            print("AttributeError:{key}".format(key=key))
            raise exception
     
    def __setitem__(self, key, value):
        """Write dictionary element
         
         Arguments:
         
         * key -- The key whose value is set
         * value -- the value to set
         
         Output:
         
         * Nothing
         """
            
        if key is None: 
            raise KeyError
        dict.__setitem__(self, key.lower(), value)
     
    def __contains__(self, key):
        """Dicionary key search
         
        Arguments:
        
        * key -- The key to search for
        
        Output:
        
        * True if key exists, otherwise false
        """
        if key is None: 
            return False
        return dict.__contains__(self, key.lower())
     
    def has_key(self, key):
        """Dictionary key search
        
        Arguments:
        
        * key -- The key to search for
         
        Output:
        
        * true if key exists, otherwise false
        """
        if key is None: 
            return False
        return dict.has_key(self, key.lower())
     
    def get(self, key, def_val=None):
        """Dictionary read with a default value
        
        Arguments:
        
        * key -- The key whose value is returned
        * def_val -- The optional default value
         
        Output:
        
        * The value corresponding to the key, or a default value if the 
          key does not exist.
        """
        if key is None: 
            return None
        return dict.get(self, key.lower(), def_val)
     
    def setdefault(self, key, def_val=None):
        """Dictionary write with a default value
 
        Writes the def_val into key if key doesn't exist
            
        Arguments:
        
        * key -- The key whose value is written
        * def_val -- The value to writ
 
        Output:
        
        * The value of key, or the default value
        """
              
        if key is None: 
            raise KeyError
        return dict.setdefault(self, key.lower(), def_val)
     
    def update(self, other):
        """Dictionary update, adds other dictionary to this dictionary
             
        Arguments:
        
        * other -- A dictionary to be added
        
        Output:
        
        * None
             
        """
        for key, val in other.items():
            dict.__setitem__(self, key.lower(), val)
     
     
    def pop(self, key, *args):
        """Dictionary pop, remove an entry and return its value
             
        Arguments:
        
        * key -- The key whose value is popped
        * def_val -- A default value if none exists
        
        Output:
        
        * The value corresponding to key
        """
        return dict.pop(self, key.lower(), *args)

            
     
    def copy(self):
        """Shallow Copy a dictionary 
        
        Output:
        * A copy of the dictionary
        """    
        new = CaselessDict()
        for key in self.keys():
            new[key] = self[key]
        return new
 
def fromkeys(iterable, value=None):
    """Setup a dicionary with a keylist and default value
    
    Arguments:

    * iterable -- A list of keys to initialize
    * value -- a default value to use
    
    Output:
    
    * A caseless dicionary
    """
    data = CaselessDict()
    for key in iterable:
        data[key] = value
    return data
    
