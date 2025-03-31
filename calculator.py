def add(number_1, number_2):
    return f"{number_1} + {number_2} = {number_1 + number_2}"

def sub(number_1, number_2):
    return f"{number_1} - {number_2} = {number_1 - number_2}"

def mul(number_1, number_2):
    return f"{number_1} * {number_2} = {number_1 * number_2}"

def div(number_1, number_2):
    if number_2 == 0:  # Проверка деления на ноль
        return "На ноль делить нельзя"
    return f"{number_1} / {number_2} = {number_1 / number_2}"

def pr(number_1, number_2):
    return number_2 / 100 * number_1

def calculator():
    operation = input("Действие (+, -, *, /, %). Для завершения нажмите 0:  ")
    while operation != "0":
        temp = input("Введите первое число: ")
        if "/" in temp:
             temp = temp.split("/")
             number_1 = int(temp[0])/int(temp[1])
        else: 
            number_1 = float(temp)

        temp = input("Введите первое число: ")
        if "/" in temp:
             temp = temp.split("/")
             number_2 = int(temp[0])/int(temp[1])
        else: 
            number_2 = float(temp)
        
        if operation == "+":
            print(add(number_1, number_2))
        elif operation == "-":
            print(sub(number_1, number_2) )
        elif operation == "*":
            print(mul(number_1, number_2) )
        elif operation == "/":
            print(div(number_1, number_2) )
        elif operation == "%":
            print(pr(number_1, number_2) )
        else:
            print("Действие не найдено!")
        operation = input("Действие (+, -, *, /). Для завершения нажмите 0:  ")

if __name__ == "__main__":
    calculator()


