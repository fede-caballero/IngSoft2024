FROM python:3.11-bullseye

ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/category_ms/.local/bin


RUN useradd --create-home --home-dir /home/category_ms category_ms

WORKDIR /home/category_ms-ms

USER category_ms
RUN mkdir app

COPY ./app ./app
COPY ./app.py .

ADD requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5003

CMD [ "python", "./app.py" ]

