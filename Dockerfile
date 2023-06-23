FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True


# Copy local code to the container image.
COPY . /src

# This is so that we bypass the need to cd into the src dir to run our commands
WORKDIR /src

# Install Python Requirements
RUN pip install -r requirements.txt

# Run this command to export environment variables
RUN if [ "$(uname)" == "Windows" ]; then set FLASK_APP=app; else export FLASK_APP=app; fi

EXPOSE 5000 

# docker run will run this command to start the app in localhost
CMD ["flask", "run", "--host=0.0.0.0"]