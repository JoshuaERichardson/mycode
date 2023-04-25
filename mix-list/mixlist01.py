#!/usr/bin/env python3

my_list = [ "192.168.0.5", 5060, "UP" ]

print("The second item in the list (port): " + str(my_list[1]) )

print("The last itme in the list (state): " + my_list[-1] )

print("\n\n\n\nChallenge: display only the IP addresses on screen")

iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# Do it dynamically:
for ip in iplist:
    # Note: Each IP MUST contain 3 '.'s.
    sep = str(ip).split('.')
    # Now each of the 4 sections MUST be integers
    result = True
    if len(sep) == 4:
        for i in sep:
            try:
                int(i)
            except:
                result = False
    else: result = False
    if result == True: print(ip + "\n")
  
