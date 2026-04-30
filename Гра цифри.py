import random
time_limit = 4
operations = ["+", "-", "*", "/"]
print("Гра швидко напиши відповідь на приклади !")

while time_limit>0:
    a=random.randint(1,10)
    b=random.randint(1,10)
    sign=random.choice(operations)
    if sign == "+":
        correct_answer = a + b
    elif sign == "-":
        correct_answer = a - b
    elif sign == "*":
        correct_answer = a * b
    print(f"Скільки буде {a} {sign} {b}")
    user_answer=float(input("Відповідь   "))
    if float(user_answer) == correct_answer:
        print("красава")
        time_limit-=1
    else:
        print(f"Помилка правильна відповідь була{correct_answer}")

    if time_limit==0:
        print("Гра закінчена! Ти молодець.")
        exit()



