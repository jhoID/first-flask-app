import os

from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        'titulo': 'Index',
        'bienvenida': 'Saludos'
    }
    return render_template('index.html', data=data)

def main():
    app.run(debug=True, port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
