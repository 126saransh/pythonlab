# Q. Write a program to find out whether a given name is present in a list or not.

Names = ["Mayur","Sahil","Nishi","Kunal","Simran","Darshan"]
X = input("Enter Name to search: ")

if(X in Names):
    print("Name is Present...")
    exit
else:
    print("Name is not Present...")

# Output :    Enter Name to search: Sahil
#             Name is not Present...

#             Enter Name to search: Nishi
#             Name is Present...
