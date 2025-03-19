# Cloud Storage Simulator 

A Flask-based web application that simulates a cloud storage system with basic CRUD operations.

## Features

- Upload files (simulated by entering a filename)
- View a list of stored files
- Update existing files
- Delete files
- Responsive design

## Tech Stack

- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Vercel

## Live Demo

Visit the live application: [Cloud Storage Simulator](https://cloud-storage-simulator.vercel.app)

## Local Development

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/cloud-storage-simulator.git
   cd cloud-storage-simulator
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Run the application:
   ```
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
cloud-storage-simulator/
├── app.py                # Main Flask application
├── files_db.json         # JSON file storing the simulated files
├── requirements.txt      # Python dependencies
├── vercel.json           # Vercel deployment configuration
├── static/
│   └── css/
│       └── styles.css    # CSS styles
└── templates/
    └── index.html        # HTML template
```

## Deployment

This application is configured for deployment on Vercel with the included `vercel.json` configuration file.

## License

MIT