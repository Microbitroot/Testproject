# Use the official Python image from Docker Hub
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the diceroller.py file into the container
COPY diceroller.py .

# Command to run when the container starts
CMD ["python", "./diceroller.py"]
