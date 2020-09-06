# You have login and password as integer numbers stored in the code as login and password variables.
#  The user inputs two integers (the login and the password). If they match to one in the code - output "Login success",
#  if the password doesn't match, but logins match, output "Wrong password", if login is wrong,
#  output "No user with login XXXX found", where XXXX is the login, the user's just input.

# INPUT

# Two integers, the first - login, the second - password.

# OUTPUT

# "Login success" if both match, "Wrong password" if passwords do not match, but logins match and 
# "No user with login XXXX found" if logins do not match (XXXX is the login, the user has input).

# Sample Input 1:
# 100500 424242
# Sample Output 1:
# Login success

# Sample Input 2:
# 100500 311231
# Sample Output 2:
# Wrong password

# Sample Input 3:
# 21341 424242
# Sample Output 3:
# No user with login 21341 found
login = 100500
password = 424242
login_i, password_i= [int(x) for x in input().split()]
print(type(login_i))
if login_i==login:
    if password_i==password:
        print('Login success')
    else:
        print('Wrong password')
else:
    print('No user with login {0} found'.format(login_i))