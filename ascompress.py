#!/usr/bin/env python

"""converts an ascii string to a list of hex words, one byte per character. hex words start with 0x"""

__author__ = "S0lll0s"
__copyright__ = "Sol Bekic, 2013"
__license__ = "GPL"
__version__ = "1.1.0"

import sys

def ascompress( string ):
 res = ""
 l = len( string )
 
 if l % 2 == 1:
 	string += chr( 0 )
 for i in range( 0, l, 2 ):
  res += '{:#x}{:02x}, '.format( ord( string[i] ), ord( string[i+1] ) )
 #if l != len( string ):
 # res += '{:#'
 return res


if __name__ == "__main__":
 while True:
  print( ascompress( raw_input( 'string: ' ) ) )
