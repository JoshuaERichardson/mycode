#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginsuccess = 0

ip = []

# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -]" in line:
            if "Authorization failed" in line:
                loginfail+=1
                # Split the string on "_" and then grab the last word
                ip.append(line.split(" ")[-1][:-1])

            elif "POST" in line or "GET" in line: loginsuccess+=1

        


print("The number of failed log in attempts is", loginfail)
print("The number of successful log in attempts is", loginsuccess)
print("The failed IP's:",*ip, sep="\t\t")
