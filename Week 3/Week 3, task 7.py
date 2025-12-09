print("Program starting")
print("Testing decision structures. . .")

value=int(input("Insert an integer:")

print("Options: ")
print("1-Multi branched decision")
print("2-Multiple independent if statements")
print("0-Exit program")

if option ==1:
          if value>=400:
              value=value +44
          elif value>=200:
              value=value+22
          elif value>=100:
              value=value+11
print(f"Result is {value}")

elif option ==2:
  if value>=400:
    value=value+44
  if value>=200:
    value=value +22
  if value>=+11:
    value=value+11

print(f"Result is {value}")

elif option==0:
  print("Exitting program . . .")

else:
  print("Unknown option, try again")

print("Program ending.")
