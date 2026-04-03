#!/usr/bin/env python3
"""
Simple REST API program to display "Hello World!" using FastAPI
"""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create a FastAPI application instance
app = FastAPI(
    title="Hello World API",
    description="A simple REST API that displays Hello World!",
    version="1.0.0"
)


@app.get("/", response_class=JSONResponse)
async def hello():
    """Return a simple greeting"""
    return {
        "message": "Hello World!",
        "status": "success"
    }


@app.get("/hello", response_class=JSONResponse)
async def hello_endpoint():
    """Alternative hello endpoint"""
    return {
        "greeting": "Hello World!",
        "method": "GET"
    }


@app.get("/api/greet/{name}", response_class=JSONResponse)
async def greet_person(name: str):
    """Greet a specific person"""
    return {
        "message": f"Hello {name}!",
        "status": "success"
    }


@app.get("/health", response_class=JSONResponse)
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "API is running"
    }


if __name__ == '__main__':
    import uvicorn
    print("Starting FastAPI REST API Server...")
    print("Visit http://localhost:8000 to see 'Hello World!'")
    print("API documentation available at http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
</content>
<parameter name="filePath">/Users/sureshvelusamy/PyCharmMiscProject/fastapi_rest_api.py
