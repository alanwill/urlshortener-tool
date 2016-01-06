#!/usr/bin/env python

# coding: utf-8
from __future__ import (absolute_import, division, print_function, unicode_literals)

import sys

from oauth2client import client
from googleapiclient import sample_tools

def main(argv):
    service, flags = sample_tools.init(
        argv, 'urlshortener', 'v1', __doc__, __file__,
        scope='https://www.googleapis.com/auth/urlshortener')

    try:
        url = service.url()

        longurl = raw_input('Enter the URL to be shortened: ')
        body = {'longUrl': longurl }
        resp = url.insert(body=body).execute()

        print ("")
        print ("Shortened URL:   " + resp['id'])
        print ("Long URL:        " + resp['longUrl'])

    except client.AccessTokenRefreshError:
        print ("The credentials have been revoked or expired, please re-run the application to re-authorize")

if __name__ == '__main__':
    main(sys.argv)
