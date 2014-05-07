#!/usr/bin/env python
""" Python tool that gets your external IP. Checks different sites until one works. """

from __future__ import print_function
import urllib2
import sys

def usage():
    print ("Usage: running " + sys.argv[0] + " will try to find a good host from a built in list automatically, ")
    print("however you can specify your own host to use by using the -u or --url")
    print("Example: " + sys.argv[0] + " -u http://ip.telize.com/")
        
def getIP(URL):
    try:
        IP=urllib2.urlopen(URL).read()
        print(IP)
        sys.exit(0)
    except urllib2.URLError:
        return
    except ValueError:
        print ("Invalid URL! (Did you forget to include the http:// at the beginning of the URL?)")
        sys.exit(1)

if __name__ == '__main__':
    try:
        if ((sys.argv[1] == "-h") or (sys.argv[1] == "--help")):
            usage()
    except IndexError:
        pass 
    try: 
        if ((sys.argv[1] == "-u") or (sys.argv[1] == "--url")):
            getIP(sys.argv[2])
            print("ERROR: Specified host is down", file=sys.stderr)
            sys.exit(1)
    except IndexError:
        getIP("http://whatismyip.akamai.com/")
        getIP("http://curlmyip.com")
        getIP("http://ip.telize.com/")
        getIP("http://tnx.nl/ip")
        getIP("http://myip.dnsomatic.com/")
        getIP("http://ident.me/")
        getIP("http://ifconifg.me/ip")
        getIP("http://icanhazip.com/")
        print("ERROR: couldn't find good host", file=sys.stderr)
        sys.exit(1)
