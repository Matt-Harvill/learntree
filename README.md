# Learning Tree

A simple Flask web application for tracking your learning journey in a tree-like structure.

## Setup

1. Make sure you have Python 3.7+ installed
2. Install the required dependencies using uv:
   ```bash
   uv sync
   ```

## Running the Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://localhost:5000`

## Features

- Add learning items with:
  - Name
  - Type of media
  - Date started
  - Optional date finished
  - Optional takeaways
  - Optional inspiration (parent item)
- View your learning items in a timeline
- See relationships between learning items

## Database

The application uses SQLite for data storage. The database file (`learning_tree.db`) will be automatically created when you first run the application.
