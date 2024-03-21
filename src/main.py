import os

from flask import Flask, send_file, render_template, request, url_for, redirect

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

def query_string():
    # url example https://5000-monospace-first-app-with-flask-1710873799083.cluster-nxnw2gov3naqkvuxb437f67u5e.cloudworkstations.dev/query?param1=johann&param2=33
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return 'OK'

def page_not_found(err):
    # return render_template('404.html'), 404
    return redirect(url_for('index'))

def main():
    # app.run(debug=True, port=int(os.environ.get('PORT', 80)))
    app.add_url_rule('/query', view_func=query_string)
    app.register_error_handler(404, page_not_found)
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    main()
