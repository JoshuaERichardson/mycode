#!/usr/bin/python3

import pprint
import requests

AOIF_BOOKS = 'https://www.anapioficeandfire.com/api/books'

def main():
    gotresp = requests.get(AOIF_BOOKS)

    # Decode
    got_dj  = gotresp.json()

    pprint.pprint(got_dj)

if __name__  == "__main__":
    main()


