# Query Service


# Building Docker Image

## Prerequisites

Before building the Docker image, make sure you have the following installed:

- [Docker](https://www.docker.com/)

## Build Process

1. Navigate to query-service/application

2. Build the Docker image using the following command:

    ```
    docker build -t query_service:latest .
    ```

 5. Once the build is complete, you can run a container based on the newly built image:

    ```
    docker run -p 8000:8000 query_service:latest
    ```

  
## Accessing the Application

After running the Docker container, you can access the Swagger UI navigating to [http://localhost:8000/docs](http://localhost:8000/docs) in your web browser.



# Requirements for Development

Before running the application, ensure you have the following prerequisites installed:

- Python client 3
- **Note: Python client 3.11 preferred.**

You can install Poetry using the following command:

```
pip install poetry
```
### Installation

- Navigate to the `./application/query-service` folder.

- Set up the virtual environment and package management using Poetry:

   ```
   poetry shell
   poetry install
   ```

### Run Application
To run the service, use Hypercorn with the following command:

```
hypercorn endpoints:app --bind 127.0.0.1:8000
```
## Accessing Swagger UI
Once the service is running, you can access the Swagger UI by navigating to [http://localhost:8000/docs](http://localhost:8000/docs).