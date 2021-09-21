# Use an official Python runtime as a parent image
FROM python:3
WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt


# Make port  available to the world outside this container
EXPOSE 


ENV NAME Cloud-Computing-k8s-Acceptance
CMD python app.py

