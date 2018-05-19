#!/usr/bin/python3
import argparse
import requests
import sys
unreachable=None
def status(url):
    try:
        req=requests.get(url)
        if req.status_code!=200:
            unreachable.append(url)
        #return req.status_code
    except Exception:
        print("Something is fisshy with "+url)
        sys.exit(3)
if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Get the url list for checking response code")
    parser.add_argument("-u", "--url", help="Enter the url's seprated by comma you wish to check",required=True)
    urls=parser.parse_args().url.split(',')
    #print(urls)
    for url in urls:
        status(url)
    if unreachable:
        print("The following url's are DOWN: " +unreachable)
        sys.exit(2)
    else:
        print("All Good!!")
        sys.exit(0)
