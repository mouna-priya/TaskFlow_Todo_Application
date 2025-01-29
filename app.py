from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

MONGO_URI = "mongodb://root:example@mongo:27017/"
client = MongoClient(MONGO_URI)
db = client['todo_db']
tasks_collection = db.tasks

# Home page - Display tasks
@app.route('/')
def index():
    tasks = list(tasks_collection.find())  # Fetch all tasks
    return render_template('index.html', tasks=tasks)

# Add task
@app.route('/add', methods=['POST'])
def add_task():
    description = request.form['task_description']
    date = request.form['task_date']
    time = request.form['task_time']

    task = {
        'task_description': description,
        'task_date': date,
        'task_time': time,
        'done': False  # Default task status is not done
    }
    tasks_collection.insert_one(task)
    return redirect(url_for('index'))

# Edit task
@app.route('/edit/<task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if request.method == 'POST':
        description = request.form['task_description']
        date = request.form['task_date']
        time = request.form['task_time']

        tasks_collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {
                'task_description': description,
                'task_date': date,
                'task_time': time
            }}
        )
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

# Delete task
@app.route('/delete/<task_id>')
def delete_task(task_id):
    tasks_collection.delete_one({"_id": ObjectId(task_id)})
    return redirect(url_for('index'))

# Mark task as completed or not
@app.route('/check/<task_id>', methods=['POST'])
def check_task(task_id):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    new_status = request.form.get('done') == 'on'  # Toggle the 'done' status
    tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"done": new_status}}
    )
    return redirect(url_for('index'))

# Clear all tasks
@app.route('/clear_all')
def clear_all():
    tasks_collection.delete_many({})
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
