def new_game2():
    questions = {"1. Which year did Nigeria gain Independence?: ": "B",
                 "2. What is the full meaning of INEC?: ": "A",
                 "3. What is the name of the Governor of Lagos state?: ": "D",
                 "4. What is the name of the Presidential candidate of the Labour Party?: ": "C",
                 "5. How many colours does Nigerian flag have?: ": "A"}
    options = [["A. 1966", "B. 1960", "C. 1999", "D. 1976"],
               ["A. Independent National Electoral Commission", "B. Independent National Electoral Council",
                "C. Independent National Electoral Cooperation", "D. International National Election Commission"],
               ["A. Bola Ahmed Tinubu", "B. Prof. Yemi Osibanjo", "C. Adegboyega Oyetola", "D. Babajide Sanwo-Olu"],
               ["A. Ezenwo Nyesom Wike", "B. Atiku Abubakar", "C. Peter Gregory Obi", "D. Bola Ahmed Tinubu"],
               ["A. TWO Colours", "B. THREE Colours", "C. FOUR Colours", "D. ONE Colour"]]


def welcome_Prompt():
    name = input("Welcome to Godfrey's Lab Current affairs test, What is your name?: \n").upper()
    welcome_prompt = input("Dear " +name+ " if ready for the Test enter Yes: ")
    welcome_prompt = welcome_prompt.upper()
    if welcome_prompt == "YES":
        print("The game begins!!!")
        return True
    else:
        print("Please check back later!")
        return False

#------------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter from the options (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses,guesses)


#---------------------------------
def check_answer(answer,guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0

#---------------------------------
def display_score(correct_guesses,guesses):
    print("----------------------------")
    print("RESULTS")
    print("----------------------------")

    print("ANSWERS: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("GUESSES: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("YOUR SCORE IS: " +str(score)+ "%")

#---------------------------------
def play_Again():

    response = input("Do you want to play again? (Yes or No): ")
    response = response.upper()
    if response == "YES":
        return True
    else:
        return False

questions = {"1. Which year did Nigeria gain Independence?: ": "B",
             "2. What is the full meaning of INEC?: ": "A",
             "3. What is the name of the Governor of Lagos state?: ": "D",
             "4. What is the name of the Presidential candidate of the Labour Party?: ": "C",
             "5. How many colours does Nigerian flag have?: ": "A"}
options = [["A. 1966","B. 1960","C. 1999","D. 1976"],
           ["A. Independent National Electoral Commission","B. Independent National Electoral Council","C. Independent National Electoral Cooperation","D. International National Election Commission"],
           ["A. Bola Ahmed Tinubu","B. Prof. Yemi Osibanjo","C. Adegboyega Oyetola","D. Babajide Sanwo-Olu"],
           ["A. Ezenwo Nyesom Wike","B. Atiku Abubakar","C. Peter Gregory Obi","D. Bola Ahmed Tinubu"],
           ["A. TWO Colours","B. THREE Colours","C. FOUR Colours", "D. ONE Colour"]]
welcome_Prompt()
new_game()


while play_Again():
    new_game()
print("Goodbye, Nice having you!!!")
