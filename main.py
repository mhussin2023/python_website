from flask import Flask, request, render_template_string

app = Flask(__name__)

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

TEMPLATE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <title>Simple MCQ Quiz</title>
</head>
<body>
  <h1>MCQ Quiz (10 questions)</h1>
  {% if score is not none %}
    <h2>Your score: {{score}} / {{total}}</h2>
    <a href="/">Try again</a>
  {% else %}
    <form method="post" action="/submit">
      {% for q in questions %}
        <div style="margin-bottom:12px;">
          <strong>{{loop.index}}. {{q.text}}</strong><br>
          <label><input type="radio" name="q{{q.id}}" value="a"> a) {{q.a}}</label><br>
          <label><input type="radio" name="q{{q.id}}" value="b"> b) {{q.b}}</label><br>
          <label><input type="radio" name="q{{q.id}}" value="c"> c) {{q.c}}</label><br>
        </div>
      {% endfor %}
      <button type="submit">Submit</button>
    </form>
  {% endif %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE, questions=QUESTIONS, score=None, total=len(QUESTIONS))

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for q in QUESTIONS:
        key = f"q{q['id']}"
        ans = request.form.get(key)
        if ans == q['answer']:
            score += 1
    return render_template_string(TEMPLATE, questions=QUESTIONS, score=score, total=len(QUESTIONS))

if __name__ == '__main__':
    app.run(debug=True)
