# Quiz Service with PostgreSQL

This project implements a web service using Python and PostgreSQL for a quiz application. The service allows users to request a specified number of random quiz questions from a public API and store them in a PostgreSQL database.

## Features

- Accepts POST requests with a JSON payload specifying the number of questions to retrieve.
- Fetches the requested number of random quiz questions from a public API.
- Stores the questions and their details in a PostgreSQL database.
- Ensures uniqueness of questions in the database.
- Provides the previously saved question as a response for subsequent requests.
- Supports data persistence using Docker volumes.

## Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   
2. Navigate to the project directory:
    ```
    cd quiz-service-postgresql
   
3. Build the Docker image and start the containers:
    ```
    docker-compose up --build
   
4. The service should now be running on http://localhost:8000. You can access the API using your preferred API testing tool (e.g., curl, Postman).

## API Usage
Send a POST request to http://localhost:8000/questions with the following JSON payload to retrieve quiz questions:

    {
    "questions_num": 5
    }

The response will contain the previously saved quiz questions, if available.

## Dependencies

- Python 3
- FastAPI
- SQLAlchemy
- psycopg2
- Docker (if using Docker for containerization)

## Contributing
Contributions to this project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.