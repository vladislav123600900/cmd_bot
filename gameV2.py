from random import randint

def guess_number():
    max_number = int(input("Введите сложность игры"))
    win_number = (randint(1, max_number))
    user_number = int(input("Число:"))
    while user_number != win_number:
        print("Неверно.",end=" ")
        if user_number > win_number:
            print("Ваше число больше!")
        else:
            print("Ваше число меньше!")
        user_number = int(input("Попробуйте еще раз: "))
    print(f"Поздравляем! Победа!\nВы отгадали!")


if __name__ == "__main__":
    guess_number()
    