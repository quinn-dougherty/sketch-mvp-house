FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN export FLASK_APP=application:app
RUN export ZILLOW_KEY="X1-ZWz1827x6v9n9n_77v70"



ENTRYPOINT ["python"]
CMD ["application.py"]

