# Use the official Python image from the Docker Hub
FROM python:3.11-bullseye

# Create a non-root user and set up the home directory
RUN useradd --create-home --home-dir /home/category_ms category_ms

# Set the working directory
WORKDIR /home/category_ms

# Create the app directory with root permissions
RUN mkdir -p /home/category_ms/app

# Change the ownership of the app directory to the non-root user
RUN chown -R category_ms:category_ms /home/category_ms/app

# Switch to the non-root user
USER category_ms

# Set environment variables
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1
ENV PATH=$PATH:/home/category_ms/.local/bin

# Copy the application code to the app directory
COPY ./app ./app

# Copy the main application file to the working directory
COPY ./app.py .

# Add and install the requirements
ADD requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5003

# Run the application
CMD [ "python", "./app.py" ]
