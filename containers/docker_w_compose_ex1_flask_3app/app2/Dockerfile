FROM python:3.7-alpine
## add bash so can use bash commands/go into container
RUN apk update && apk add bash 

# set working directory with env varialbes 
WORKDIR /code
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=5002

# copy files into working directory
COPY . .

# install dependencies
RUN pip install -r requirements.txt

# run the app and expose the default port for flask 
EXPOSE 5002
CMD ["flask", "run"]