# Decomplexify

Decomplexify is a powerful tool designed to help students understand and build complex systems using an intuitive, agent-based modeling framework. The app provides a no-code/low-code interface for defining models and agents using a cucumber like instruction set developed through Python's behave package. 

---

## Table of Contents

1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
   - [Back-End Setup (Flask)](#back-end-setup-flask)
   - [Front-End Setup (React)](#front-end-setup-react)
4. [Running the Application](#running-the-application)
7. [License](#license)

---

## Features

- Define agent-based models using a Gherkin-style grammar.
- Dynamic grid rendering with customizable dimensions.
- Real-time data fetching and interactive controls.
- Modern UI with support for light and dark themes.
- Detailed error handling and feedback.

---

## Technologies Used

- **Back-End**: Python, Flask
- **Front-End**: React (TypeScript), Material-UI
- **Database**: SQLite (or any other supported DB backend)
- **Others**: Docker, Axios

---

## Setup Instructions

### Back-End Setup (Flask)

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/decomplexify.git
   cd decomplexify/instruction_set
   ```

2. Set up a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask API:

   ```bash
   python api.py
   ```

   The back-end will now be running at `http://localhost:3001`.

#### Running with Docker

1. Build the Docker image:

   ```bash
   docker build -t decomplexify-backend .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 3001:5000 decomplexify-backend
   ```

   The back-end will now be running at `http://localhost:3001`.

---

### Front-End Setup (React)

1. Navigate to the front-end directory:

   ```bash
   cd ../web-abms
   ```

2. Install the dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
   npm start
   ```

   The front-end will now be running at `http://localhost:3000`.

4. Install required packages through NPM (if not installed):

   ```bash
   npm install react react-router-dom @mui/material @emotion/react @emotion/styled papaparse file-saver xlsx
   ```

## Running the Application

### Back-End

1. Ensure the Flask back-end API is running.
   - If using a virtual environment:
     ```bash
     source venv/bin/activate    # On Windows: venv\Scripts\activate
     python api.py
     ```
     The API will run on `http://localhost:3001`.
   - If using Docker:
     ```bash
     docker run -p 3001:3001 decomplexify-backend
     ```
     The API will run on `http://localhost:3001`.

### Front-End

1. Navigate to the front-end directory:
   ```bash
   cd web-abms
   ```

2. Start the React development server:
   ```bash
   npm start
   ```

   The front-end will run on `http://localhost:3000`.

### Full Application

Once both the back-end and front-end servers are running:
- Visit `http://localhost:3000` in your browser to access Decomplexify.
- Ensure the back-end API is correctly connected at `http://localhost:3001`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.