import os

from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    courses = ['PHP', 'Python', 'Rust', 'JavaScript']
    # courses = []
    data = {
        'title': 'Here we go',
        'greetings': 'greetings',
        'courses': courses,
        'number_courses': len(courses)
    }

    return render_template('index.html', data=data)

@app.route('/contacto/<nombre>/<int:age>')
def contacto(nombre, age):
    data = {
        'title': 'Contact',
        'name': nombre,
        'age': age
    }
    return render_template('contacto.html', data=data)

def main():
    # app.run(debug=True, port=int(os.environ.get('PORT', 80)))
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
