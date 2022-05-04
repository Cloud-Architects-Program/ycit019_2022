# Official Python Alpine Base image using Simple Tags
# Image contains Python 3 and pip pre-installed, so no need to install them

FROM python:3.9.5-alpine3.12

# Specify Working directory
WORKDIR /usr/src/app

# COPY requirements.txt /usr/src/app/
COPY requirements.txt ./

# Install Python Flask used by the Python app
RUN pip install --no-cache-dir -r requirements.txt

# Copy files required for the app to run
COPY app.py ./
COPY templates/index.html ./templates/

# Make a record that the port number the container should be expose is:
EXPOSE 5000

# run the application
CMD ["python", "./app.py"]
