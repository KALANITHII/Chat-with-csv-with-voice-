# PandasAI Chainlit Project

This project integrates PandasAI with Chainlit to create an interactive chat interface for analyzing CSV data. Users can upload a CSV file and then ask questions about the data using natural language.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features

- Interactive chat interface powered by Chainlit
- CSV file upload functionality
- Natural language querying of CSV data using PandasAI
- Display of data preview upon file upload

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10+
- pip (Python package manager)

## Installation

1. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. Install the required packages:
   ```
   pip install chainlit pandas pandasai python-dotenv
   
   or 
   
   pip install -r requirements.txt 
   ```

4. Create a `.env` file in the project root and add any necessary environment variables (e.g., API keys for PandasAI if required).

## Usage

1. Run the Chainlit application:
   ```
   chainlit run app.py
   ```

2. Open your web browser and navigate to `http://localhost:8000` (or the URL provided in the terminal).

3. Upload a CSV file when prompted.

4. Start asking questions about your data in natural language.

## How It Works

This project consists of a single Python file (`app.py`) that sets up a Chainlit chat interface with two main components:

1. **File Upload and Initialization** (`@on_chat_start`):
   - Prompts the user to upload a CSV file.
   - Reads the uploaded file using pandas.
   - Initializes a PandasAI Agent with the loaded data.
   - Displays a preview of the data (first few rows).

2. **Message Handling** (`@on_message`):
   - Retrieves the PandasAI Agent from the user session.
   - Sends the user's message to the Agent for processing.
   - Displays the Agent's response in the chat interface.

The application uses the following main libraries:
- `chainlit` for the chat interface and file handling.
- `pandas` for reading and manipulating CSV data.
- `pandasai` for natural language processing of data-related queries.