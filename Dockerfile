# Use an official Python runtime as the base image
FROM python:latest

# нужен чтобы логи нормально из контейнера вылезали
ENV PYTHONUNBUFFERED 1

# тоже можно поставить, все равно кеш питон кода в контейнере лишь место лишнее занимать будет
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt ./


# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port on which the application will run
EXPOSE 8000

# Set the command to run the application
#CMD ["python", "uvicorn main:app --reload"]
COPY wait-for-postgres.sh /wait-for-postgres.sh
RUN chmod +x /wait-for-postgres.sh