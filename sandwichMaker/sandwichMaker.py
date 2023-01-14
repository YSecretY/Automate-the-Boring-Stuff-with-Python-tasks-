# pyinputplus allows to use clever input, which is essential to save time and avoid bugs (needs to be installed with pip)
import pyinputplus as pyip

# class with food prices
class Prices:
    bread = {"wheat": 7, "white": 5, "sourdough": 8}
    protein = {"chicken": 14, "turkey": 19, "ham": 3, "tofu": 20}
    cheese = {"cheddar": 14, "Swiss": 15, "mozarella": 17}
    vegetables = {"mayo": 4, "mustard": 3, "lettuce": 8, "tomato": 5}

total_price = 0

# ask user for user preferences and count total_price
print('Would you like some bread?')
response = pyip.inputYesNo()
if response == 'yes':
    response = pyip.inputMenu(['wheat', 'white', 'sourdough'])
    total_price += Prices.bread[response]

print('What about the protein?')
response = pyip.inputYesNo()
if response == 'yes':
    response = pyip.inputMenu(['chicken,', 'turkey', 'ham', 'tofu'])
    total_price += Prices.protein[response]

print('Cheese maybe?')
response = pyip.inputYesNo()
if response == 'yes':
    print('What particularly would you like: ')
    response = pyip.inputMenu(['cheddar', 'Swiss', 'mozarella'])
    total_price += Prices.cheese[response]

print('Vegetables?')
response = pyip.inputYesNo()
if response == 'yes':
    response = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'])
    total_price += Prices.vegetables[response]
    
print('How many sandwichese do you like?')
response = pyip.inputInt(min = 1)
total_price *= response

# show total_price
print(f'Ok, thank you! The total price of your order is: {total_price}')