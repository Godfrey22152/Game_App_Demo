import os
import random
import json
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Load questions from the JSON file
with open('questions.json', 'r') as file:
    questions_data = json.load(file)

questions = questions_data.get('questions', [])

# Create a list of tuples containing (question, options)
question_option_pairs = [{'question': q['question'], 'options': q['options'], 'correct_option': q['correct_option']} for q in questions]

# Shuffle the questions and options together
random.shuffle(question_option_pairs)

@app.route('/')
def index():
    session['user_answers'] = [None] * len(question_option_pairs)
    return render_template('welcome.html')

@app.route('/start_round', methods=['GET', 'POST'])
def start_round():
    random.shuffle(question_option_pairs)  # Shuffle questions and options together
    session['question_option_pairs'] = question_option_pairs
    session['user_answers'] = [None] * len(question_option_pairs)
    return redirect(url_for('question', question_num=1))


@app.route('/question/<int:question_num>', methods=['GET', 'POST'])
def question(question_num):
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        user_answers = session.get('user_answers')  # Step 1: Retrieve user answers
        user_answers[question_num - 1] = user_answer  # Step 2: Update user answers
        session['user_answers'] = user_answers  # Step 3: Store updated user answers back into session
        next_question_num = question_num + 1


#        print(f"User selected answer for question {question_num}: {user_answer}")  # Add this line for debugging

        if next_question_num > 15:  # Display a maximum of 10 questions per round
            return redirect(url_for('results'))

        return redirect(url_for('question', question_num=next_question_num))

    question_option_pairs = session.get('question_option_pairs')

    if not question_option_pairs:
        return redirect(url_for('index'))  # Redirect to the index page if no questions available

    current_question_data = question_option_pairs[question_num - 1]
    question_key = current_question_data['question']
    options_list = current_question_data['options']

    return render_template('question.html', question_num=question_num, question=question_key,
                           options_list=options_list, next_question_num=question_num + 1)

@app.route('/results')
def results():
    user_answers = session.get('user_answers')
    question_option_pairs = session.get('question_option_pairs')

    if user_answers is None or question_option_pairs is None:
        return redirect(url_for('index'))

    # Get the correct answers for the current round
    correct_answers = [q['correct_option'] for q in question_option_pairs]

    # Calculate the score and retrieve question-answer pairs
    correct_guesses, question_answer_pairs = check_answers(user_answers[:15], correct_answers[:15])

    if len(correct_answers) == 0:
        score = 0
    else:
        score = int((correct_guesses / 15) * 100)  # Calculate the score based on the number of questions

    # Prepare data for displaying results
    results_data = []
    for question_num, (question, correct_ans, user_ans) in enumerate(question_answer_pairs, start=1):
        result = {
            'question_num': question_num,
            'question': question,
            'options': question_option_pairs[question_num - 1]['options'],
            'correct_option': correct_ans,
            'user_guess': user_ans,
            'is_correct': correct_ans == user_ans
        }
        results_data.append(result)

    return render_template('results.html', score=score, results_data=results_data)

def check_answers(user_answers, correct_answers):
    if len(user_answers) != len(correct_answers):
        return 0, []  # Return 0 if the lengths of user and correct answers lists don't match

    correct_guesses = sum(1 for user_ans, correct_ans in zip(user_answers, correct_answers) if user_ans == correct_ans)

    question_answer_pairs = [(q['question'], correct_ans, user_ans) for q, correct_ans, user_ans in zip(question_option_pairs, correct_answers, user_answers)]

    return correct_guesses, question_answer_pairs

if __name__ == '__main__':
    app.run(debug=True)


