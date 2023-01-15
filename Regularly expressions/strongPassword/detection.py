import re, pyinputplus as pyip

def isStrongPassword(password) -> bool:
    amountRegex = re.compile(r'''
        (\d){8,} # check if there are 8+ elements in the password
    ''', re.VERBOSE)
    size = bool(amountRegex.findall(password))
    digit = bool(re.search(r'\d', password)) # check if there is at least 1 digit in password
    lower_letter = bool(re.search(r'[a-z]', password)) # check if there is at least one lowercase letter
    upper_letter = bool(re.search(r'[A-Z]', password)) # check if there is at least one uppercase letter
    return size and digit and lower_letter and upper_letter # if all of them return true the result is true, else - false



user_password = pyip.inputPassword()

print(isStrongPassword(user_password))