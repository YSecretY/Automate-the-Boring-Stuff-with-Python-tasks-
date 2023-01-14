# re - allows to use regularly expressions
# pyperclip needs to be installed with pip (pip or pip3 install pyperclip), allows to use clipboard
import re, pyperclip


# Create a class where we have months as keys and number of days in them as values, for example: 1(Fabruary) - 31
# Number of days can be different, I have created it as in the task :)
class DaysInMonths:
    leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    non_leap = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def isLeap(year) -> bool:
    return year % 4 == 0 or year % 100 == 0

def isValidDate(day, month, year) -> bool:
    day, month, year = int(day), int(month), int(year)
    if year < 1000 or year > 3000:
        return False
    if isLeap(year):
        if month not in DaysInMonths.leap or day > DaysInMonths.leap[month] or day < 1:
            return False
    else:
        if month not in DaysInMonths.non_leap or day > DaysInMonths.non_leap[month] or day < 1:
            return False
    return True

# Create a regularly expression, that will find all the dates in format dd/mm/yyyy, for example: 15-12-2004 or 11/05/1465 or 01.03.1324
dateRegex = re.compile(r'''
    (\d{2})+ # first 2 digits
    (\s|-|\.|\/) # separator
    (\d{2})+ # second 2 digits
    (\s|-|\.|\/) # separator
    (\d{4})+ # last 4 digits
''', re.VERBOSE)


input_text = str(pyperclip.paste()) # Take a text from clipboard into input_text
matches = [] # Will contain answer as list of strings

# For each date, that in tuple format (like that: [('07', '-', '01', '-', '2005')]) we check if date is valid and if yes append the string with it to the matches
for groups in dateRegex.findall(input_text):
    day = groups[0]
    month = groups[2]
    year = groups[4]
    if isValidDate(day, month, year):
        date = '-'.join([day, month, year])
        matches.append(date)
        
# If we have something in matches, copy it to clipboard and print
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No dates found.')