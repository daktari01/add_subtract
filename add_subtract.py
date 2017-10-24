def add(num1, num2):
    if (type(num1) == int and type(num2) == int):
        return num1 + num2
    else:
        raise TypeError("Enter only integers")

def subtract(num1, num2):
    if (type(num1) == int and type(num2) == int):
        return num1 - num2
    else:
        raise TypeError("Enter only integers")

if __name__ = '__main__':
    main()
