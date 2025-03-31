import calculator
import gameV2
import steps_calcV2
import shop_onlineV2


print("Привет! Меня зовут чат-бот Алекс!")
print("""Меню:
 1 - калькулятор
 2 - игра угадай число
 3 - конвертирование шагов из "в день" в "в неделю" и в "месяц"
 4 - онлайн магазин 
 5 - меню
 0 - завершить""")
choice = input("Номер действия ")

while choice != "0":
    if choice == "1":
        calculator.calculator()
    elif choice == "2":
        gameV2.guess_number()
    elif choice == "3":
        steps_calcV2.calc_steps()
    elif choice == "4":
        shop_onlineV2.shop_online()
    elif choice == "5":
      print("""Меню:
       1 - калькулятор
 2 - игра угадай число
 3 - конвертирование шагов из "в день" в "в неделю" и в "месяц"
 4 - онлайн магазин
 5 - меню
 0 - завершить""")
    else:
        print("Команда не найдена")
    choice = input("Номер действия:  ")




