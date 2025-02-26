from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/questions', methods=['GET'])
def get_questions():
    questions = [
        {
        "question": "What is the largest continent by land area?",
        "options": ["Africa", "Asia", "Europe", "North America"],
        "correctOption": 1,
        "points": 10
        },
        {
        "question": "Which is the longest river in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "correctOption": 1,
        "points": 10
        },
        {
        "question": "Which country has the largest population?",
        "options": ["India", "United States", "China", "Indonesia"],
        "correctOption": 2,
        "points": 10
        },
        {
        "question": "What is the capital city of Australia?",
        "options": ["Sydney", "Melbourne", "Brisbane", "Canberra"],
        "correctOption": 3,
        "points": 10
        },
        {
        "question": "Which desert is the largest in the world?",
        "options": ["Sahara", "Gobi", "Arabian", "Kalahari"],
        "correctOption": 0,
        "points": 10
        },
        {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "South Korea", "Japan", "Thailand"],
        "correctOption": 2,
        "points": 10
        },
        {
        "question": "What is the smallest country in the world by land area?",
        "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
        "correctOption": 1,
        "points": 30
        },
        {
        "question": "Which ocean is the largest by surface area?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "correctOption": 3,
        "points": 20
        },
        {
        "question": "Mount Everest is located in which mountain range?",
        "options": ["Rockies", "Andes", "Himalayas", "Alps"],
        "correctOption": 2,
        "points": 20
        },
        {
        "question": "Which country has the most natural lakes?",
        "options": ["United States", "Canada", "Russia", "Brazil"],
        "correctOption": 1,
        "points": 30
        },
        {
        "question": "Which European country is divided into departments?",
        "options": ["Germany", "France", "Italy", "Spain"],
        "correctOption": 1,
        "points": 30
        },
        {
        "question": "What is the longest mountain range in the world?",
        "options": ["Rocky Mountains", "Andes", "Himalayas", "Alps"],
        "correctOption": 1,
        "points": 10
        },
        {
        "question": "What is the capital city of Canada?",
        "options": ["Toronto", "Vancouver", "Montreal", "Ottawa"],
        "correctOption": 3,
        "points": 30
        },
        {
        "question": "Which island country is located southeast of India?",
        "options": ["Sri Lanka", "Maldives", "Indonesia", "Philippines"],
        "correctOption": 0,
        "points": 30
        },
        {
        "question": "Which river flows through Paris?",
        "options": ["Thames", "Danube", "Seine", "Rhine"],
        "correctOption": 2,
        "points": 20
        }
    ]
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=False, port=8080)