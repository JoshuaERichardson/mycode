#!/usr/bin/env python3

def main():    
    usr_name = input("Please enter your name:\n>")       
    usr_name = usr_name.title()    
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))
    
    modulus_math = usr_date%12
    year_of = [['monkey' , 'you are sharp, smart, curious, and mischievious.'], 
               ['rooster', 'you are hardworking, resourceful, courageous, and talented.'],
               [ 'dog', 'you are loyal, honest, cautious, and kind.'],
               [ 'pig', 'you are a symbol of wealth, honesty, and practicality.'],
               [ 'rat', 'you are artiatic, sociable, industrious, charming, and intelligent.'],
               [ 'tiger', 'you are courageous, enthusiastic, confident, charismatic, and a leader.'],
               [ 'ox', 'you are strong, thorough, determined, loyal, and reliable.'],
               [ 'rabbit', 'you are vigilant, witty, quick-minded, and ingenious.'],
               [ 'dragon', 'you are talented, powerful, lucky, and successfull'],
               [ 'snake', 'you are wise, like to work alone, and determined.'],
               [ 'horse', 'you are animated, active, and energetic.'],
               [ 'sheep', 'you are creative, resilient, gentle, mild-mannered, and shy.']]
    sign = year_of[modulus_math][0]
    info = year_of[modulus_math][1]
    print(f"{usr_name}, your zodiac sign is {sign}, {info}")

main()
