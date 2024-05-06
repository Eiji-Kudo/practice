# Use an official Python runtime as a parent image
FROM selenium/standalone-chrome:4.0

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Switch to root user, install Python and pip, then switch back to seluser
USER root
RUN apt-get update && apt-get install -y python3 python3-pip
USER seluser

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "app.py"]