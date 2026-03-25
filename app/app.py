from flask import Flask, render_template, request, redirect, url_for
from database import init_db, save_feedback, get_all_feedback

app = Flask(__name__, template_folder='../templates', static_folder='../static')

init_db()

@app.route('/', methods=['GET'])
def index():
    feedbacks = get_all_feedback()
    return render_template('index.html', feedbacks=feedbacks)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '').strip()
    feedback = request.form.get('feedback', '').strip()
    if name and feedback:
        save_feedback(name, feedback)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
