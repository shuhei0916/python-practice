FROM python

RUN apt-get update
RUN pip install --upgrade pip
RUN apt install -y tree

# WORKDIR /app
