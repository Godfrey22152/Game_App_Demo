import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

questions = {
    "0. Which year did Nigeria gain Independence?: ": "B",
    "1. Which year did Nigeria gain Independence?: ": "B",
    "2. What is the full meaning of INEC?: ": "A",
    "3. How many colours are there in a Rainbow?: ": "C",
    "4. What is the name of the Governor of Lagos state?: ": "D",
    "5. What is the name of the Presidential candidate of the Labour Party?: ": "C",
    "6. How many colours does Nigerian flag have?: ": "A"
}

options = [
    ["A. 1966", "B. 1960", "C. 1999", "D. 1976"],   
    ["A. 1966", "B. 1960", "C. 1999", "D. 1976"],
    ["A. Independent National Electoral Commission", "B. Independent National Electoral Council",
     "C. Independent National Electoral Cooperation", "D. International National Election Commission"],
    ["A. 4", "B. 5", "C. 7", "D. 6"],    
    ["A. Bola Ahmed Tinubu", "B. Prof. Yemi Osibanjo", "C. Adegboyega Oyetola", "D. Babajide Sanwo-Olu"],
    ["A. Ezenwo Nyesom Wike", "B. Atiku Abubakar", "C. Peter Gregory Obi", "D. Bola Ahmed Tinubu"],
    ["A. TWO Colours", "B. THREE Colours", "C. FOUR Colours", "D. ONE Colour"]
]

@app.route('/')
def index():
    session['user_answers'] = [None] * len(questions)
    return render_template('welcome.html')

@app.route('/question/<int:question_num>', methods=['GET', 'POST'])
def question(question_num):
    if request.method == 'POST':
        user_answer = request.form.get('answer')
        session['user_answers'][question_num - 1] = user_answer  # Update user's answer
        next_question_num = question_num + 1
        if next_question_num > 6:
            return redirect(url_for('results'))
        return redirect(url_for('question', question_num=next_question_num))

    return render_template('question.html', question_num=question_num, question=list(questions.keys())[question_num - 1],
                           options=options[question_num - 1], next_question_num=question_num + 1)

@app.route('/results')
def results():
    user_answers = session.get('user_answers')
    if user_answers is None:
        return redirect(url_for('index'))  # Redirect to the index page if user answers are not available

    correct_guesses = sum(1 for user_ans, correct_ans in zip(user_answers, questions.values()) if user_ans == correct_ans)
    score = int((correct_guesses / len(questions)) * 100)
    return render_template('results.html', score=score, questions=questions, user_answers=user_answers)

if __name__ == '__main__':
    app.run(debug=True)
