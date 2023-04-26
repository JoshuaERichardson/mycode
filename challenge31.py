#!/usr/bin/env python3

def main():
    wordbank= ["indentation", "spaces"]

   tlgstudents= ["Brandon", "Caleb", "Cat", "Chad the Beardulous", "Chance", "Chris", "Jessica", "Jorge", "Joshua", "Justin", "Lui", "Stephen"]
    
    wordbank.append(4)

    print(wordbank)

    while(True):
        num = input("gimme # b/t 0 and 11 plz:\n")
        try:
            num = int(num)
            if 0 <= num <= 20: break
        except:
            continue

    print(tlgstudents)    
    student_name = tlgstudents.pop(num)
    print(tlgstudents)


    print(f"{student_name.title()} always uses <4> <spaces> to indent.")



main()
