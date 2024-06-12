FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the essential files
COPY pyproject.toml poetry.lock ./

# Install Poetry and project dependencies
RUN pip install poetry
RUN poetry install --no-dev

# Copy the application code
COPY {{cookiecutter.project_slug}}/ {{cookiecutter.project_slug}}/

# Copy the entry script
COPY entrypoint.py .

# Ensure the scripts in the scripts directory can be executed
RUN chmod +x {{cookiecutter.project_slug}}/scripts/*

# Make the entry script executable
RUN chmod +x entrypoint.py

# Set PYTHONPATH
ENV PYTHONPATH=/usr/src/app

# Make ports available to the world outside this container (if necessary)
# EXPOSE 8080

# Set the entry point to the custom entry script
ENTRYPOINT ["python", "entrypoint.py"]
