def main():


    sam_winchester = {
        'Nickname': ['Sam', 'Sammy', 'B---h', 'Moose'],
        'Species': ['Human', 'Ghost', 'Rabid'],
        'Gender': 'Male',
        'Occupation': ['Hunter', 'Witch-in-training',
                    ['Former Undergraduate',
                    'Former law school applicant']],
        'Family Members': {'Parents': {'Mother': 'Mary Winchester',
                        'Father': 'John Winchester'},
                        'Siblings': {'Younger Brother': 'Adam Milligan'}},
        }

    # Print a script that addds a key value pair

    sam_winchester.update( { 'Weakness' : 'Demon Blood' } )

    # Verify:
    print(sam_winchester,"\n\n\n\n")

    # Print a list of all keys in the dictionary:
    print(list(sam_winchester.keys()), "\n\n\n\n")

    # Ask for user input, have them choose of the the keys that was printed and save as choice:
    while(True):
        choice = input("Choose one of the keys by typing it out: ")
        if choice in list(sam_winchester.keys()):
            print(f"You chose { choice }!  The values: { sam_winchester[choice]}\n\n\n")
            break
    

    # Now list out all keys in numeric order and allow the user to pick one:
    keylist = list(sam_winchester.keys())
    while(True):
        print(f"Please select from one of the following numbers:\n")
        for i in range(len(keylist)):
            print(f"{i+1}: {keylist[i]}\n")
        num_input = input("Please select a number: \n")
        try:
            num_input = int(num_input)
            if 0 <= num_input <= len(keylist)-1:
                key = keylist[num_input-1]
                print(f"You chose: { key }!  The values: { sam_winchester[key] }")
                break
        except:
            print("Errrr...... You chose wrong.  Try again.")


main()