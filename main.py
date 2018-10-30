def collatz(number):

    if number % 2 == 0:
        result = number // 2
        print(result)
        return result
    else:
        result = number * 3 + 1
        print(result)
        return result

number = int(input("Type a number: "))

while number != 1:
    number = collatz(number)
