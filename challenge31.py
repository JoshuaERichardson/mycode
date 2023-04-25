#!/usr/bin/env python3

def main():
    wordbank= ["indentation", "spaces"]

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']
    
    wordbank.append(4)

    print(wordbank)

    while(True):
        num = input("gimme # b/t 0 and 20 plz:\n")
        try:
            num = int(num)
            if 0 <= num <= 20: break
        except:
            continue

    print(tlgstudents)    
    tlgstudents.pop(num)
    print(tlgstudents)


main()
