#!/usr/bin/env python

"""concatenates text line-by-line"""

__author__ = "S0lll0s"
__copyright__ = "Sol Bekic, 2013"
__license__ = "GPL"
__version__ = "1.0.0"

def concat_text( files, seperator=' ' ):
    return '\n'.join( [
        seperator.join(  [
            (string.splitlines()[i] if i <= string.count('\n') else '')
            for string in files
        ] )
        for i in range( max([string.count('\n') for string in files ]) + 1 )
    ] )

if __name__ == "__main__":
 import argparse

 parser = argparse.ArgumentParser( description='concatenate files line-by-line' )

 parser.add_argument( "files", metavar='file', nargs='+', help='the files to concatenate' ) 
 parser.add_argument( "-s", "--seperator", default=' ', help='seperator string' )

 args = parser.parse_args()

 print concat_text( [ open( file, 'r' ).read() for file in args.files ], args.seperator )
