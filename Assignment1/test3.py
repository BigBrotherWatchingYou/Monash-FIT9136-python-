a = 'Fuck123@#'
k = "m"


result =''
for char in a:
    result += chr((ord(char)) ^ ord(k))



print(result)