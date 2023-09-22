import os
import random  # Import the random module
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

questions = {
    "Which year did Nigeria gain Independence?: ": "B",
    "What is the full meaning of INEC?: ": "A",
    "How many colours are there in a Rainbow?: ": "C",
    "What is the name of the Governor of Lagos state?: ": "D",
    "What is the name of the Presidential candidate of the Labour Party?: ": "C",
    "How many colours does Nigerian flag have?: ": "A",
    "What is the significance of October 1st in Nigeria's history?: ": "C",
    "Which Nigerian writer won the Nobel Prize in Literature?: ": "B",
    "What was the name of the Nigerian civil war that occurred from 1967 to 1970?: ": "C",
    "Which natural resource is a major contributor to Nigeria's economy?: ": "C",
    "Who was Nigeria's first military Head of State?: ": "A",
    "Which river is the longest in Nigeria?: ": "A",
    "Which Nigerian city is known for its annual Carnival?: ": "C",
    "Who is often referred to as the 'Father of Nigerian Literature'?: ": "B",
    "In which year did Nigeria become a Republic?: ": "B",
    "Which Nigerian athlete won the Long Jump gold medal at the 2008 Beijing Olympics?: ": "B",
    "What is the significance of the Niger Delta region in Nigeria?: ": "C",
    "Which Nigerian leader initiated the 'War Against Indiscipline' campaign in the 1980s?: ": "D",
    "What event led to the establishment of the Nigerian Stock Exchange?: ": "A",
    "Who was Nigeria's first female combat helicopter pilot?: ": "D",
    "Which Nigerian state is known as the GATEWAY STATE?: ": "A",
    "Who was Nigeria's first president?: ": "C",
    "In what year did Nigeria adopt the Naira as its official currency?: ": "C",
    "Which Nigerian state is known as the CENTRE OF COMMERCE?: ": "B",
    "What is the name of the highest mountain in Nigeria?: ": "B",
    "Which Nigerian environmental activist and writer won the Goldman?: ": "C",
    "Nigeria hosted the Commonwealth Games in which year?: ": "C",
    "Which Nigerian musician released the hit album SUPERSTAR in 2011?: ": "A",
    "Which Nigerian city is known for its historic city walls and is a UNESCO World Heritage Site?: ": "A",
    "Which Nigerian author wrote the novel: HALF OF A YELLOW SUN, depicting the Biafran War?: ": "D",
    "In what year was the University of Ibadan, Nigeria's first university, founded?: ": "C",
    "Nigeria has several UNESCO World Heritage Sites. Which site is known for its ancient terracotta sculptures?: ": "A",
    "Nigeria has had female finance ministers. Who was the first woman to hold this position?: ": "B",
    "Nigeria's fashion industry has gained recognition. Which Nigerian fashion designer is known for the WAKANDA FOREVER outfit?: ": "C",
    "Nigeria's film industry has produced many acclaimed movies. Which Nigerian film was the first to be submitted for the Best International Feature Film category at the Oscars?: ": "D",
    "Nigeria is known for its traditional textiles. Which fabric is famous for its bright colors and intricate patterns?: ": "A",
    "Nigeria is known for its diverse wildlife. Which of the following is not a native animal to Nigeria?: ": "B",
    "Nigeria has made strides in the tech industry. Which Nigerian entrepreneur is known for founding the online payment platform Flutterwave?: ": "B",
    "Which Nigerian physicist was the first African to win a Nobel Prize in Physics?: ": "A",
    "What deadly infectious disease was eradicated in Nigeria in 2020?: ": "D",
    "Nigeria's entertainment industry includes a thriving comedy scene. Which Nigerian comedian is known as Basketmouth?: ": "A",
    "Which festival is known for its colorful masquerades and is celebrated by the Igbo people?: ": "B",
    "Which Nigerian musician is known as the: Pentecostal Voice of Nigeria?: ": "C",
    "What is the name of Nigeria's largest natural gas producing company?: ": "A",
    "Nigeria's natural resources include solid minerals. What mineral is known as the BLUE GEM and is often found in Jos, Plateau State?: ": "A",
    "Which Nigerian entrepreneur is known for founding the online shopping platform Konga?: ": "A",
    "Which Nigerian film director is known for movies like 'The Wedding Party' and 'King of Boys'?: ": "C",
    "What do the two horses on the Nigerian Coat of Arm represent?: ": "D",
    "What is the name of the first man to buy a car in Nigeria?: ": "A",
    "How many Local Governments does Nigeria have?: ": "C"
}

options = [
    ["A. 1950", "B. 1960", "C. 1970", "D. 1980"],
    ["A. Independent National Electoral Commission", "B. Independent National Electoral Council",
     "C. Independent National Electoral Cooperation", "D. International National Election Commission"],
    ["A. 4", "B. 5", "C. 7", "D. 6"],
    ["A. Bola Ahmed Tinubu", "B. Prof. Yemi Osibanjo", "C. Adegboyega Oyetola", "D. Babajide Sanwo-Olu"],
    ["A. Ezenwo Nyesom Wike", "B. Atiku Abubakar", "C. Peter Gregory Obi", "D. Bola Ahmed Tinubu"],
    ["A. TWO Colours", "B. THREE Colours", "C. FOUR Colours", "D. ONE Colour"],
    ["A. National Youth Day", "B. Democracy Day", "C. Independence Day", "D. Human Rights Day"],
    ["A. Chinua Achebe", "B. Wole Soyinka", "C. Chimamanda Ngozi Adichie", "D. Ben Okri"],
    ["A. War of Unity", "B. War of Independence", "C. Biafra War", "D. Niger Delta Conflict"],
    ["A. Coffee", "B. Cocoa", "C. Oil", "D. Diamonds"],
    ["A. Yakubu Gowon", "B. Olusegun Obasanjo", "C. Ibrahim Babangida", "D. Muhammadu Buhari"],
    ["A. Niger River", "B. Benue River", "C. Osun River", "D. Lagos River"],
    ["A. Abuja", "B. Lagos", "C. Calabar", "D. Enugu"],
    ["A. Wole Soyinka", "B. Chinua Achebe", "C. Buchi Emecheta", "D. Chimamanda Ngozi Adichie"],
    ["A. 1960", "B. 1979", "C. 1999", "D. 2010"],
    ["A. Blessing Okagbare", "B. Chioma Ajunwa", "C. Mary Onyali", "D. Gloria Alozie"],
    ["A. Major trading hub", "B. Center of political power", "C. Oil production", "D. Cultural heritage site"],
    ["A. Shehu Shagari", "B. Ibrahim Babangida", "C. Yakubu Gowon", "D. Muhammadu Buhari"],
    ["A. Oil boom of the 1970s", "B. Independence Day", "C. The end of colonial rule", "D. The Great Depression"],
    ["A. Funmilayo Ransome-Kuti", "B. Ngozi Okonjo-Iweala", "C. Olufunke Oshonaike", "D. Tolulope Arotile"],
    ["A. Ogun", "B. Lagos", "C. Osun", "D. Oyo"],
    ["A. Yakubu Gowon", "B. Olusegun Obasanjo", "C. Nnamdi Azikiwe","D. Shehu Shagari"],
    ["A. 1960", "B. 1975", "C. 1973", "D. 1980"],
    ["A. Lagos", "B. Kano", "C. Ogun", "D. Abuja"],
    ["A. Aso Rock", "B. Chappal Waddi", "C. Olumo Rock", "D. Zuma Rock"],
    ["A. Nnimmo Bassey", "B. Chimamanda Ngozi Adichie", "C. Ken Saro-Wiwa", "D. Wangari Maathai"],
    ["A. 2002", "B. 2010", "C. 2003", "D. 2014"],
    ["A. Wizkid", "B. Burna Boy", "C. Davido", "D. Olamide"],
    ["A. Kano", "B. Ibadan", "C. Benin City", "D. Enugu"],
    ["A. Chinua Achebe", "B. Wole Soyinka", "C. Odo Godfrey", "D. Chimamanda Ngozi Adichie"],
    ["A. 1950", "B. 1952", "C. 1948", "D. 1953"],
    ["A. Sukur Cultural Landscape", "B. Aso Rock", "C. Osun-Osogbo Sacred Grove", "D. Ogbunike Caves"],
    ["A. Ngozi Okonjo-Iweala", "B. Oby Ezekwesili", "C. Kemi Adeosun", "D. Nenadi Usman"],
    ["A. Lisa Folawiyo", "B. Deola Sagoe", "C. Duro Olowu", "D. Mai Atafo"],
    ["A. King of Boys", "B. October 1 ", "C. The Wedding Party", "D. Lionheart"],
    ["A. Ankara", "B. Aso Oke", "C. Adire", "D. Kente"],
    ["A. Lion", "B. Panda", "C. Elephant", "D. Leopard"],
    ["A. Jason Njoku", "B. Iyinoluwa Aboyeji", "C. Olugbenga Agboola", "D. Seun Onigbinde"],
    ["A. Akinwande Olumide Babatunde Soyinka", "B. Philip Emeagwali", "C. Gift Ijioma", "D. Chike Obi"],
    ["A. Malaria", "B. Tuberculosis", "C. HIV", "D Polio"],
    ["A. Bright Okpocha", "B. Ayo Makun (AY)", "C. Bovi Ugboma", "D. Ali Baba"],
    ["A. Durbar Festival", "B. Ofala Festival", "C. Argungu Fishing Festival", "D. Eyo Festival"],
    ["A. Fela Kuti", "B. Ebenezer Obey", "C. Tope Alabi", "D. Sunny Ade"],
    ["A. Nigerian Liquefied Natural Gas (NLNG)", "B. Shell Nigeria", "C. ExxonMobil Nigeria", "D. Chevron Nigeria"],
    ["A. Sapphire", "B. Emerald", "C. Ruby", "D. Diamond"],
    ["A. Sim Shagaya", "B. Iyinoluwa Aboyeji", "C. Bosun Tijani", "D. Seun Onigbinde"],
    ["A. Kunle Afolayan", "B. Tunde Kelani", "C. Kemi Adetiba", "D. Lancelot Oduwa Imasuen"],
    ["A. Peace", "B. Power", "C. Strength", "D. Dignity"],
    ["A. Bob Jensen", "B. Tunde Kelani", "C. Fela Kuti", "D. Odo Godfrey"],
    ["A. 775", "B. 776", "C. 774", "D. 773"]
]


shuffled_questions = list(questions.keys())  # List of question keys

@app.route('/')
def index():
    return render_template('welcome.html')


@app.route('/start_round', methods=['GET', 'POST'])
def start_round():
    random.shuffle(shuffled_questions)  # Shuffle the questions
    session['shuffled_questions'] = shuffled_questions
    return redirect(url_for('question', question_num=1))


@app.route('/question/<int:question_num>', methods=['GET', 'POST'])
def question(question_num):
    shuffled_questions = session.get('shuffled_questions')

    if not shuffled_questions or question_num > 10:
        return redirect(url_for('results'))

    question_key = shuffled_questions[question_num - 1]
    options_index = list(questions.keys()).index(question_key)

    return render_template('question.html', question_num=question_num, question=question_key,
                           options=options[options_index], next_question_num=question_num + 1)

@app.route('/results')
def results():
    shuffled_questions = session.get('shuffled_questions')

    if not shuffled_questions:
        return redirect(url_for('index'))

    correct_answers = [questions[q] for q in shuffled_questions[:10]]
    score = 0

    if correct_answers:
        score = int((len(correct_answers) / 10) * 100)

    return render_template('results.html', score=score, shuffled_questions=shuffled_questions[:10])


if __name__ == '__main__':
    app.run(debug=True)
