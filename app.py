from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure the SQLite Database
# Database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///files.db'
# Disable modification tracking
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for storing files


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    size = db.Column(db.String(50), nullable=False)
    uploaded_at = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<File {self.name}>"


# Initialize the database (create the table if it doesn't exist)
with app.app_context():
    db.create_all()


@app.route('/')
def index():
    files = File.query.all()  # Query all files from the database
    return render_template('index.html', files=files)


@app.route('/upload', methods=['POST'])
def upload_file():
    filename = request.form.get('filename')
    file_size = request.form.get('filesize')

    if not filename:
        flash('Filename is required', 'error')
        return redirect(url_for('index'))

    # Check if file already exists
    existing_file = File.query.filter_by(name=filename).first()
    if existing_file:
        flash('File already exists', 'error')
        return redirect(url_for('index'))

    # Add new file to the database
    new_file = File(
        name=filename,
        size=file_size or '1 MB',
        uploaded_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    db.session.add(new_file)
    db.session.commit()
    flash('File uploaded successfully', 'success')
    return redirect(url_for('index'))


@app.route('/update/<int:file_id>', methods=['POST'])
def update_file(file_id):
    new_filename = request.form.get('new_filename')

    if not new_filename:
        flash('New filename is required', 'error')
        return redirect(url_for('index'))

    file_to_update = File.query.get(file_id)  # Get file by ID
    if file_to_update:
        file_to_update.name = new_filename
        file_to_update.uploaded_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S") + " (updated)"
        db.session.commit()
        flash('File updated successfully', 'success')

    return redirect(url_for('index'))


@app.route('/delete/<int:file_id>')
def delete_file(file_id):
    file_to_delete = File.query.get(file_id)  # Get file by ID
    if file_to_delete:
        db.session.delete(file_to_delete)
        db.session.commit()
        flash('File deleted successfully', 'success')

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
