# Source: https://automatetheboringstuff.com/chapter3/
def collatz (number):
    if number % 2 == 0:
        result = number // 2
        print (result)
        return result
    else:
        result = 3 * number + 1
        print (result)
        return result

while True:
    try:
        userInput = int(input('Enter a number '))
        collatz(userInput)
    except:
        print('Please enter a number!')


