# amai_nime_backend
Backend for AmaiNime

To start backend:

1) Clone this repository in your directoty
2) Install librarias:

FastAPI: pip install fastapi["standard"] or pip install "fastapi[standard]"

Uvicorn: pip install uvicorn or uvicorn["standard"] or "uvicorn[standard]"
   




To use:

Start server, use:

uvicorn main:app --reload

it will be open on host localhost:8000 or 127.0.0.1:8000

To get anime, use:

localhost:8000/api/get_anime/{id}

