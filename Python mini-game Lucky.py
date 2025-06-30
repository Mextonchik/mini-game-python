import random
print("Привет! Это мини-игра, где тебе нужно выбрать одну цифру от 1 до 9, и если ты угадаешь задуманную заранее цифру - ты выиграл! Удачи!")
game = True
while game:
   lucky = int(input("Введите цифру: "))
   for i in range(1):
      num = random.randint(1, 9)
   if lucky == num:
      print("Вы выиграли, так держать!")
   else: 
      print("Не угадали, повезёт в другой раз!")     