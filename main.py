questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]

player_name = input("Расскажи как тебя зовут: ")

ready = input(f"Привет, {player_name.title()}! "
              f"Предлагаю проверить свои знания английского! "
              f"Набери 'ready', чтобы начать! ")

score = 0
right_answer = 0

if ready.lower() == "ready":
    print(f"{player_name.title()}, начинаем тренировку!")
    for i in range(len(questions)):
        life = 3
        while life > 0:
            answer = input(questions[i])
            if answer == answers[i]:
                print("Ответ верный!")
                right_answer += 1
                score += life * 10
                break
            life -= 1
            if life > 0:
                print(f"Осталось попыток: {life}, попробуйте еще раз!")
            else:
                print(f"Неправильно. Правильный ответ: {answers[i]}")

    percent = round(right_answer / len(questions) * 100)
    print(f"Вот и все,{player_name.title()}! "
          f"Вы ответили на {right_answer} вопросов из {len(questions)} верно, "
          f"вы набрали {score} баллов, "
          f"это {percent} процентов!")
else:
    print("Кажется, вы не хотите играть. Очень жаль.")
