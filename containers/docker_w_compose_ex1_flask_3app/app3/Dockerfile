## https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker 

FROM python:3.9-slim

EXPOSE 8501

# Set working directory in the container
WORKDIR /app

# copy /app directory from local machine to /app directory in container
COPY /app /app

# install dependencies and updates
RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# install python dependencies for python
RUN pip3 install -r requirements.txt

# run the app
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]