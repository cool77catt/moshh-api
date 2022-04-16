FROM python:3.9.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR src

ENV FLASK_APP "app.py"

ENTRYPOINT [ "python", "-m", "flask", "run", "--no-debugger", "--host", "0.0.0.0", "--port", "80" ]