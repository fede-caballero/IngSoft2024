FROM python:3
COPY . /usr/src/app
COPY app/requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]