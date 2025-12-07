# Command to create the requirements.txt file
pip freeze > requirements.txt
# Use a base Python image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy the requirements file and install dependencies
# We copy requirements.txt separately to leverage Docker caching
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /usr/src/app/

# Expose the port the Django app runs on
EXPOSE 8000

# Command to run the Django development server
# You may need to change 'your_project_name.wsgi' to your actual project's WSGI file path
# The 0.0.0.0 address is crucial for access from outside the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
