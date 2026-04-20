from flask import Flask, request, render_template
import os

app = Flask(__name__, template_folder=os.path.dirname(__file__))

QUESTIONS = [
    {"id": 1, "text": "What is the capital of France?", "a": "Paris", "b": "London", "c": "Berlin", "answer": "a"},
    {"id": 2, "text": "Which planet is known as the Red Planet?", "a": "Earth", "b": "Mars", "c": "Jupiter", "answer": "b"},
    {"id": 3, "text": "What is 2 + 2?", "a": "3", "b": "4", "c": "5", "answer": "b"},
    {"id": 4, "text": "Which language is this website built with?", "a": "Python", "b": "Java", "c": "C++", "answer": "a"},
    {"id": 5, "text": "What color do you get by mixing red and white?", "a": "Pink", "b": "Green", "c": "Blue", "answer": "a"},
    {"id": 6, "text": "Which animal barks?", "a": "Cat", "b": "Cow", "c": "Dog", "answer": "c"},
    {"id": 7, "text": "Which month comes after June?", "a": "May", "b": "July", "c": "August", "answer": "b"},
    {"id": 8, "text": "How many legs does a spider have?", "a": "6", "b": "8", "c": "10", "answer": "b"},
    {"id": 9, "text": "What is the boiling point of water at sea level (°C)?", "a": "100", "b": "90", "c": "80", "answer": "a"},
    {"id": 10, "text": "Which gas do plants absorb?", "a": "Oxygen", "b": "Carbon Dioxide", "c": "Nitrogen", "answer": "b"},
]


@app.route('/')
def index():
    return render_template('index.html', questions=QUESTIONS, score=None, total=len(QUESTIONS))


@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for q in QUESTIONS:
        key = f"q{q['id']}"
        ans = request.form.get(key)
        if ans == q['answer']:
            score += 1
    return render_template('index.html', questions=QUESTIONS, score=score, total=len(QUESTIONS))


if __name__ == '__main__':
    app.run(debug=True)
