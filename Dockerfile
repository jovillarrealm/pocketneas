# Use Python 3.11 base image
FROM python:3.11.2

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /usr/src/app

# Copy and install dependencies
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Install Flask
RUN pip install -r requirements.txt
ENV FLASK_RUN_PORT=80
# Expose the required port
EXPOSE 80


# Run the application
CMD ["flask", "run"]




