import random

print("Загадай число от 0 до 100")

num = random.randint(0, 100)

num_range = [0, 100]

answer = False

while answer != True:
    guess = input("Ваше число: " + str(num) + "?\n1. Да\t2. Нет\n")
    if guess == "1":
        print("Ха, жалкий людишка. Я угадал! И так будет всегда")
        answer = True
        
    elif guess == "2": 
        temp = input("Ваше число больше или меньше " + str(num) + "?\n1.Меньше\t2.Больше\n")
        if temp == "1":
            num_range[1] = num
            num = sum(num_range) // len(num_range)
        elif temp == "2":
            num_range[0] = num
            num = sum(num_range) // len(num_range)
        else:
            print("Я вас не понял, введите «М» или «Б»")
    else:
        print("Я вас не понял, введите «Да» или «Нет»")