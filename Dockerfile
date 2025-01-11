FROM python:3.10

COPY . /cat_bot

WORKDIR /cat_bot

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]