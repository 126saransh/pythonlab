# Write a program to fill in a letter template given below with name and date: 
# letter = ''' Dear <|Name|>  You are selected  <|Date|> '''

Name = input("Enter your Name: ")
Date = input("Enter Date: ")
print("''' Dear " + Name + "\n You are selected" + "\n" + Date + "'''") 

# Output: Enter your Name: Saransh Jain
#         Enter Date: 10-10-2021
#         ''' Dear Saransh Jain
#             You are selected
#             09-10-2021'''
