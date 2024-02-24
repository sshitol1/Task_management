from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY, task TEXT, assigned_to TEXT, priority TEXT, status TEXT, date_assigned TEXT, date_completed TEXT)''')
    conn.commit()
    conn.close()

init_db()

# Route for the homepage
@app.route('/')
def index():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks ORDER BY id DESC")
    tasks = c.fetchall()
    conn.close()
    return render_template('index.html', tasks=tasks)

# Route to add a new task
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    assigned_to = request.form['assigned_to']
    priority = request.form['priority']
    date_assigned = request.form.get('date_assigned', '')  # Optional field
    
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()
    c.execute("INSERT INTO tasks (task, assigned_to, priority, status, date_assigned, date_completed) VALUES (?, ?, ?, 'Pending', ?, '')",
              (task, assigned_to, priority, date_assigned))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
