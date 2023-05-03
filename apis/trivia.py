#!/usr/bin/env python3
#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests

URL= "https://opentdb.com/api.php"

all_cat = requests.get("https://opentdb.com/api_category.php").json()
all_cat = all_cat['trivia_categories']

def main():

    while(True):
        try:
            q_number = input("How many questions would you like to answer?  At least 3, but no more than 20\n > ")
            print(q_number)
            q_number = int(q_number)
            if q_number < 3 or q_number > 20:
                print("Your number is out of bounds")
            else:
                break
        except:
            print("You did not input a proper number.  Try again")
    while(True):
        try:
            print("Please select between the following categories using the corresponding number")
            message = ""
            for i in range(len(all_cat)):
                if(i%4 == 0): 
                    print(message)
                    message = ""
                message += f'{all_cat[i]["id"]}: {all_cat[i]["name"]}\t'
            q_cat = input("Please choose one of the above numbers\n > ")
            q_cat = int(q_cat)
            print(q_cat)
            if q_cat < 0 or q_cat > int(all_cat[-1]["id"]): 
                print("Your number is out of bounds")
            else:
                break
        except:
            print("You did not input a proper number.  Try again.")
    while(True):
        try:
            q_diff = input("Select a difficulty:\n1.\tEasy\n2.\tMedium\n3.\tHard\n > ")
            q_diff = int(q_diff)
            if q_diff < 1 or q_diff > 3: 
                print("Your number is out of bounds")
            else:
                break
        except:
            print("You did not input a proper number.  Try again.")
    while(True):
        try:
            q_type = int(input("Select a type:\n1.\tMultiple Choice\n2.\tTrue/False\n > "))
            if q_type < 1 or q_diff > 2: 
                print("Your number is out of bounds")
            else:
                break
        except:
            print("You did not input a proper number: Try again.")

    # Now build the URL!
    URL_number = f'amount={q_number}'
    URL_cat = f'category={q_cat}'
    if q_diff == 1 : URL_diff = "difficulty=easy"
    if q_diff == 2 : URL_diff = "difficulty=medium"
    if q_diff == 3 : URL_diff = "difficulty=hard"
    URL_type = "type=multiple" if q_type == 1 else "type=boolean"

    built_url = f'{URL}?{URL_number}&{URL_cat}&{URL_diff}&{URL_type}&encode=url3986'
    print(built_url)
   # data = requests.get(built_url).json()
   # print(data)



    # data will be a python dictionary rendered from your API link's JSON!
#    data= requests.get(URL).json()

if __name__ == "__main__":
    main()
