#!/usr/bin/python3

import requests

AOIF = 'https://www.anapioficeandfire.com/api'

def main():
    gotresp = requests.get(AOIF)

    #Decode
    got_dj = gotresp.json()

    print(got_dj)

    ## display only the keys
    print(got_dj.keys())

if __name__ == "__main__":
    main()
