import random
import time

questions = [
    ("Viss bagātākais cilvēks pasaulē? (atbildi raksti ar mazajiem burtiem)", "bernards arnaults"),
    ("Viss vērtīgākais uzņēmums pasaulē?", "apple"), 
    ("Uzraksti šī jēdziena vārdu: Izplatītākais vīrišķais dzimumhormons?", "testosterons"),
    ("Kā sauc 7.A grupas vielas?", "halogēni"),
    ("Zemeslodes gaisa apvalks?", "atmosfēra"),
    ("Telpa kurā gandrīz nav vielu?", "vakuums"),
    ("Ko nozīmē splendid? (1 vārds)", "lieliski"),
    ("ko nozīmē exquizit taste?", "izsmalcināta garša"),
    ("Tauta kurā nebija valdniecība?", "barbari"),
    ("Eiropas mūzikas stils laika periodā no 1750. gada līdz 1820?", "klasicisms"),
    ("Garākā upe pasaulē?", "amazone"),
    ("Sociālā mediju platforma ar vissvairāk aktīvajiem lietotajiem?", "facebook")
    
]

def play_game():
    random.shuffle(questions)
    score = 0
    total_time = 0
    for i, (question, answer) in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question}")
        start_time = time.time()
        user_answer = input("Your answer: ")
        end_time = time.time()
        time_taken = end_time - start_time
        total_time += time_taken
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
            if time_taken < 15:
                print("You answered quickly!")
            elif time_taken > 30:
                print("You took too long to answer!")
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {answer}")
    print(f"\nGame Over! You got {score} out of {len(questions)} questions correct.")
    print(f"Total time taken: {total_time:.2f} seconds.")

play_game()