#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
    print() - display data to std out"""


def main():

    # pause the program and wait for the user to provide input
    user_input = input("Please enter an IPv4 IP address:")

    # display the input back to the user.
    print("You told me the IPv4 address is: " + user_input)
    
    # asking user for 'vendor name'
    vendor = input("Please input the vendor name: ")
    print(vendor)


# This calls main:
main()
