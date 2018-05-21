#!/usr/bin/python3
import argparse
import requests
import sys
unreachable=[]
def status(url):
    try:
        req=requests.get(url,timeout=5)
        if req.status_code!=200:
            unreachable.append(url)
    except requests.exceptions.ConnectionError:
        unreachable.append("%s is giving connection refused, check dns and port is listening" %url)
    except TimeoutError:
        unreachable.append("%s is timed out, check for accessbility of the url" %url)
    except Exception:
        print("Something is fisshy with %s, have you added http:// or https:// in the url" %url)

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Get the url list for checking response code")
    parser.add_argument("-u", "--url", help="Enter the url's seprated by comma you wish to check",required=True)
    urls=parser.parse_args().url.split(',')
    for url in urls:
        status(url)
    if unreachable:
        print("The following url's are DOWN: " + str(unreachable) )
        sys.exit(2)
    else:
        print("All Good!!")
        sys.exit(0)
