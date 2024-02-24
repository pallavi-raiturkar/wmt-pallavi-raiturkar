# Use an official Python 3.11 runtime as a base image
FROM python:3.11.8-bullseye

# Install curl and netcat
RUN apt-get update && apt-get install -y curl netcat

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any dependencies
RUN pip install --progress-bar off --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Set the environment variable to ensure output is sent straight to the terminal without being first buffered
ENV PYTHONUNBUFFERED 1

# Set the PYTHONPATH environment variable
ENV PYTHONPATH /app

# Copy the entrypoint script and make it executable
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh

# Use the entrypoint script to start the server and download the CSV
ENTRYPOINT ["entrypoint.sh"]






