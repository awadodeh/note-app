FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
RUN pip install sqlalchemy
COPY ./app /app/app

# docker build -t backend --no-cache .
# docker run backend