import sys
import argparse

parser = argparse.ArgumentParser( description='split files at a given delimiter' )

parser.add_argument( "file", help='the file to search in' ) 
parser.add_argument( "delimiter", help='delimiter, in hex notation' )
parser.add_argument( "-v", "--verbose", action='store_true', help='verbose output' )
parser.add_argument( "-d", "--direct", action='store_true', help='directly use the delimiter (no hex)' )

args = parser.parse_args()

file = open( args.file, 'r' )
pattern = ( args.delimiter if args.direct else str( bytearray.fromhex( args.delimiter ) ) )

if args.verbose: print "Pattern: ", ' '.join( hex( ord( x ) )[2:] for x in pattern ) 

check = 0
while 1:
 byte = file.read( len( pattern ) )

 if args.verbose: print "checking", byte
 if byte == '':
  if args.verbose: print 'Nothing found'
  break

 if check > 0: #we need to check the next 'check' bytes
  if pattern[-check:] in byte[ :check ]: #we found the rest
   file.seek( -len( pattern ) + check, 1 ) #rewind to the end of the match
   break

 if pattern in byte: #"full" match, we're at the end of the match already
  break

 check = 0
 for offset in range( 1, len( pattern ) ):
  if pattern[:-offset] in byte:
   if args.verbose: print "found with offset", offset
   check = offset
   break

if args.verbose: print "found: " 

print file.read() 
