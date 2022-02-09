# username and password

# correct variables to log in.
# normally they are stored in a database.
secretUsername = "bob"
secretPassword = "1234"

# input a username and password.

username = input("Enter username: ")
password = input("Password: ")


if username == secretUsername and password == secretPassword:
    print("Correct username and password")
else:
    print("Error")

