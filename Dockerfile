FROM python

WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip
RUN apt install -y tree

COPY requirements.txt .
RUN pip install -r requirements.txt

# CMD ["python", "main.py"] # こいつを使いこなせるようになりたい