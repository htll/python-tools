#!/usr/bin/env python

"""scans URLs from stdio for the <title> tag and uptime"""

__author__ = "S0lll0s"
__copyright__ = "Sol Bekic, 2013"
__license__ = "GPL"
__version__ = "1.0.0"

import socks
import socket
import re
import sys

def getaddrinfo( *args ):
 return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

def split_proxy( data ):
 stuff = data.split(':')
 if len( stuff ) != 2:
  raise argparse.ArgumentTypeError( "Not a valid proxy" )
 return ( stuff[0], int( stuff[1] ) )

if __name__ == "__main__":
 import argparse

 parser = argparse.ArgumentParser( description='scan URLs <title> tag' )
 parser.add_argument( "-s", "--socks", help='connect via a SOCKS4 Proxy', metavar="IP:PORT", type=split_proxy )

 args = parser.parse_args()

 if args.socks:
  socks.setdefaultproxy( socks.PROXY_TYPE_SOCKS4, *args.socks )
  socket.socket = socks.socksocket
  socket.getaddrinfo = getaddrinfo

import urllib2

def get_title( url ):
 try:
  res = urllib2.urlopen( url )
  if res.getcode() != 200:
   return ( res.getcode, "error" )
  match = re.search( r"<title>(.*)</title>", res.read() )

  if match == None:
   return ( 200, "None" )
  return ( 200, match.group( 1 ) )
 except Exception:
  return ( -1, "Error Connecting" )

if __name__ == "__main__":
 while True:
  url = sys.stdin.readline()
  if not url:
   break
  res = get_title( url )
  if res[0] == 200:
   print "{}: {}".format( url.strip(), res[1] )
  else:
   print "{}: Error {}: {}".format( url.strip(), *res )