
# weirdest place you've ever found lost keys?

freezer= ["ice cream", "ice cubes"]
hand= ["ring", "watch","keys"]
car= ["crumbs","empty coffee cups"]
doorknob= []
jacket= ["gloves"]

if "keys" in hand:
    # if a condition is true,
    # all lines underneath it are executed
    print(1)

elif "keys" in jacket:
    # elif will only run if the previous condition
    # was false
    print(2)

if "keys" in car:
    print(3)

else:
    print("Better take an Uber!")
