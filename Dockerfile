FROM python:3.10.13-slim

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py /app/

# Copy requirements.txt separately to leverage Docker cache
COPY requirements.txt /app/

# install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

