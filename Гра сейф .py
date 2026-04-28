import random
secret_code=(random.randint(1,100))
code_length=len(str(secret_code))
attempts= 5
print(f"Сейф заблокований напиши його код! {code_length} його довжина")
while attempts > 0:
   guess=int(input("Нпиши його код"))
   if guess == secret_code:
       print("вхід здійснено")
       exit()

   elif guess <= secret_code:
       attempts -= 1
       print(f"Не вправильно залишилось {attempts} спроб код більший!")
   else:
       print(f"Не вправильно залишилось {attempts} спроб код менший!")
       attempts -= 1

