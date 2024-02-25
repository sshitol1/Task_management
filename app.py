from flask import Flask, render_template, request, redirect
import pandas as pd

app = Flask(__name__)

# Suppose you have a list of tasks
tasks = [
    {'task': 'Task 1', 'assigned_to': 'Alice', 'priority': 'High', 'status': 'Incomplete', 'date_assigned': '2024-02-24', 'date_completed': None},
    {'task': 'Task 2', 'assigned_to': 'Bob', 'priority': 'Medium', 'status': 'Complete', 'date_assigned': '2024-02-23', 'date_completed': '2024-02-24'},
    # Add more tasks as needed
]

# Function to save tasks to an Excel file
def save_tasks_to_excel(tasks, filename):
    df = pd.DataFrame(tasks)
    df.to_excel(filename, index=False)

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    # Retrieve form data
    task = request.form.get('task')
    assigned_to = request.form.get('assigned_to')
    priority = request.form.get('priority')
    # Add more fields as necessary

    # Create a new task dictionary
    new_task = {
        'task': task,
        'assigned_to': assigned_to,
        'priority': priority,
        'status': 'Incomplete',
        'date_assigned': pd.Timestamp('today').strftime('%Y-%m-%d'),
        'date_completed': None
    }

    # Add the new task to the list of tasks
    tasks.append(new_task)

    # Save the tasks to an Excel file
    save_tasks_to_excel(tasks, 'tasks.xlsx')

    # Redirect to the home page
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
