
# 🐳 FastAPI Hello World in Docker

This is a beginner-friendly project that demonstrates how to run a simple **FastAPI** application inside a **Docker container**.

The app provides a basic API that returns a hello message, and includes auto-generated documentation using Swagger UI and ReDoc.

---

## 🧱 Project Structure

```

fastapi-hello/
├── app/
│   └── main.py             # FastAPI application code
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker instructions
└── README.md               # Project documentation

````

---

## 🚀 Getting Started

### 📦 Prerequisites

- [Docker](https://www.docker.com/) installed on your machine

---

### 🏗️ 1. Build the Docker Image

```bash
docker build -t fastapi-hello .
````

> `# This command creates a Docker image named "fastapi-hello" using the Dockerfile.`

---

### ▶️ 2. Run the Docker Container

```bash
docker run -d -p 8000:8000 fastapi-hello
```

> `# This runs the container and maps port 8000 of your machine to port 8000 inside the container.`

---

### 🌐 3. Access the API

* Open your browser and go to:
  👉 [http://localhost:8000](http://localhost:8000)

You should see a JSON response:

```json
{
  "message": "Hello from FastAPI and Docker!"
}
```

---

### 📚 4. API Documentation (Auto-generated by FastAPI)

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc UI: [http://localhost:8000/redoc](http://localhost:8000/redoc)

> `# These are interactive docs generated automatically from your FastAPI code.`

---

## 🧠 What You'll Learn

* How to build and run a containerized Python web app
* Using FastAPI to create lightweight APIs
* Exposing Docker container ports
* Accessing auto-generated Swagger documentation

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE)

---

## ✨ Author

Created with ❤️ by [Your Name](https://github.com/yourusername)

```

---

Let me know if you’d like to:
- Add **Docker Compose** version  
- Add **SQLite/PostgreSQL integration**  
- Add **unit tests with pytest**  

I can help you expand this project step-by-step.
```
