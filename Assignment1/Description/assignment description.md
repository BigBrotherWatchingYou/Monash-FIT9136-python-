# What this assignment is about
 write Python code for a simpleemulation of collecting user information from the console. Yourapplication should be able to ask the user to input username, passwordemail and postcode and save the information into a collection type.

# What information should be included
You should also include comments at the beginning of your program file, 
whichspecify your  <span style="color:red;">red  , your Student lD, the start date and the last modified date of theprogram, as well as with a high-level description of the program</span>. In-line commentswithin the program are also part of the required documentation.


# Assignment functions include
1. Get user input function
2. Encryption function
3. Generate user id function
4. Check username exist function
5. Authenticate username and password function
6. Add user to list function
7. Test function
8. Code encapsulation

# How it works like:
# run the test function here
usera_id_list = ["1234567", "2345678"]
usera_list = [["aaa","^^^&1&!!2!!&&&3&&&&3&!!3!!$$$"], 
              ["bbb", "^^^%1%%%2%%%%%2%%%%2%$$$"]]
usera_dict = {}
account_management(usera_id_list,usera_list,usera_dict)
Add user information and check
==============================
plz input username: aaa
username existed!: ccc
plz input password: @@@
 invaild letter_or_number_or_underscore  plz check
can only be [a-zA-z0-9_ :12345]
plz input email: aaa
 invaild email  plz check
must contain “@” and “.com”:ccc@ccc.com
plz input postcode: 9999
plz check postcode: 5432
plz check postcode: 3422
add more user(y to continue)? y
plz input username: ddd
plz input password: 234566
plz input email: ddd@ddd.com
plz input postcode: 3244
add more user(y to continue)? n
authentication of username and password
==================================
account name: ccc
account password: 12345
username password correct
account name: ddd
account password: 23456
username or password incorrect
account name: q
program quit
