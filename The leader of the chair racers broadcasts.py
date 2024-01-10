import random
import pyttsx3
govorilka = pyttsx3.init()
govorilka.setProperty(name='voice', value='ru')
govorilka.runAndWait()
response = ["Сырки говорят, что это возможно.", "Лавровый листочек сообщает,что это маловероятно", "Хомяк возражает", "Хлеб склоняется к тому, что это невозможно", "Возрадуйся, котики дают положительный ответ", "Тапочки говорят что, это положительный знак."]
question = ["Что тебя привело сюда, что за вопрос тебя терзает?", "Что на столь важно, что заставило тебя потревожить Великие Носки, смертный?!", "Тебе повезло, Величайшие Коты сегодня в расположении духа чтобы ответить на твой вопрос."]
ball = ["⚝", "❊", "ℤ", "⚶", "♡"]
game = True
while game is True:
    a=random.randint(0, 2)
    b=random.randint(0, 5)
    govorilka.say("хлебеш")
    govorilka.runAndWait()
    print(f"_/({ball[random.randint(0, 4)]})/_")
    print(question[a])
    govorilka.say(question[a])
    govorilka.runAndWait()
    quest = input()
    govorilka.say("Вы спросили"+quest)
    print("Ответ гадалки:")
    if quest.lower()=="выход":
        game = False
    print(response[b])
    govorilka.say(response[b])
    govorilka.runAndWait()
    print("-"*50)