# Python REST API Programs

This repository contains simple Python programs including a REST API.

## Programs

### 1. add_numbers.py
A simple program to add two numbers.

**Usage:**
```bash
python add_numbers.py
```

**Features:**
- Interactive user input
- Supports integers and floating-point numbers
- Error handling for invalid inputs

---

### 2. rest_api.py
A simple REST API that displays "Hello World!" using Flask.

**Installation:**
```bash
pip install Flask
```

**Usage:**
```bash
python rest_api.py
```

The API will start on `http://localhost:5000`

**Available Endpoints:**

1. **Root endpoint** - Returns a greeting message
   ```
   GET http://localhost:5000/
   ```
   Response:
   ```json
   {
     "message": "Hello World!",
     "status": "success"
   }
   ```

2. **Hello endpoint** - Alternative greeting endpoint
   ```
   GET http://localhost:5000/hello
   ```
   Response:
   ```json
   {
     "greeting": "Hello World!",
     "method": "GET"
   }
   ```

3. **Personalized greeting** - Greet a specific person
   ```
   GET http://localhost:5000/api/greet/<name>
   ```
   Example: `http://localhost:5000/api/greet/John`
   Response:
   ```json
   {
     "message": "Hello John!",
     "status": "success"
   }
   ```

4. **Health check** - Check API status
   ```
   GET http://localhost:5000/health
   ```
   Response:
   ```json
   {
     "status": "healthy",
     "message": "API is running"
   }
   ```

**Testing the API:**

You can test the API using `curl`:
```bash
curl http://localhost:5000/
curl http://localhost:5000/hello
curl http://localhost:5000/api/greet/Python
curl http://localhost:5000/health
```

Or use any REST client like Postman, Insomnia, or Thunder Client.

---

## Requirements

- Python 3.7+
- Flask 2.3.3+

Install dependencies:
```bash
pip install -r requirements.txt
```

