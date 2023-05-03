#!/usr/bin/python3                                                                                                                                                                                                                  
import pprint
import requests



AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"
AOIF_CHAR = 'https://www.anapioficeandfire.com/api/characters/'
AOIF_HOUSES = 'https://www.anapioficeandfire.com/api/houses/?pagesize=1000'

def main():
    ## Send HTTPS GET to the API of ICE and Fire books resource
    gotresp = requests.get(AOIF_BOOKS)

    ## Decode the response
    got_dj = gotresp.json()

    for singlebook in got_dj:
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")
        # print ISBN
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")



    # Challenge 1: Return the houses affiliated with the character looked up, along with a list of books they appear in:
    #User input:
    got_charToLookup = input("pick a number between 1 and 1000 to return info on a GoT character! ")
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    # Decode
    got_dj = gotresp.json()
    pprint.pprint(got_dj)

    books = got_dj['books']
    print(books)

    houses = requests.get(AOIF_HOUSES).json()
    # Find the houses:
    for house in houses:
        this = got_charToLookup
        members = house['swornMembers']
        for member in members:
            that = member.split('/')[-1]
            if this == that:  print (house['name'])

    

    
    # Challenge 2: Print the names of EVERY SINGLE GoT char to a file.
    # One loop:
#    page_characters = requests.get(AOIF_CHAR).json()
 #   for character in page_characters:
#        print(character["name"])
    # Then get the next response:
  #  headerlinks = requests.links['next']
#    print(headerlinks)
    


if __name__ == "__main__":
    main()
