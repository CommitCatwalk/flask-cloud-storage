# app.py
from flask import Flask, render_template, request, redirect, url_for, flash # type: ignore
import os
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Simulated storage database
DB_FILE = 'files_db.json'


def get_files():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_files(files):
    with open(DB_FILE, 'w') as f:
        json.dump(files, f, indent=4)


@app.route('/')
def index():
    files = get_files()
    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload_file():
    filename = request.form.get('filename')
    file_size = request.form.get('filesize')

    if not filename:
        flash('Filename is required', 'error')
        return redirect(url_for('index'))

    files = get_files()
    # Check if file already exists
    for file in files:
        if file['name'] == filename:
            flash('File already exists', 'error')
            return redirect(url_for('index'))

    # Add new file
    files.append({
        'id': len(files) + 1,
        'name': filename,
        'size': file_size or '1 MB',
        'uploaded_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    save_files(files)
    flash('File uploaded successfully', 'success')
    return redirect(url_for('index'))


@app.route('/update/<int:file_id>', methods=['POST'])
def update_file(file_id):
    new_filename = request.form.get('new_filename')

    if not new_filename:
        flash('New filename is required', 'error')
        return redirect(url_for('index'))

    files = get_files()
    for file in files:
        if file['id'] == file_id:
            file['name'] = new_filename
            file['uploaded_at'] = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S") + " (updated)"
            save_files(files)
            flash('File updated successfully', 'success')
            break

    return redirect(url_for('index'))


@app.route('/delete/<int:file_id>')
def delete_file(file_id):
    files = get_files()
    files = [file for file in files if file['id'] != file_id]
    save_files(files)
    flash('File deleted successfully', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
