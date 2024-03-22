# Flask Application Docker Project
This project provides a Dockerized setup for running a Flask web application with a SQLite database. It includes instructions for building and running the Docker container.

## Prerequisites
Before you begin, ensure you have the following installed:


 #### Docker: Install Docker
 #### Python 3.x: Install Python

## Getting Started
Clone this repository to your local machine:

```bash
git clone https://github.com/Kinderdll/flask-app.git
```
Navigate to the project directory:
```bash
cd flask-docker-project
```
Build the Docker image:

```bash
docker build -t flask-app .
```
Run the Docker container:

```bash
docker run --name my_flask_app -p 9000:9000 flask-app
```
Access the application in your web browser at http://localhost:9000.

## Directory Structure

* data/: Contains database migration scripts.
* tests_app.py: Contains unit tests for the application.
* Dockerfile: Defines the Docker image configuration.
* requirements.txt: Lists the Python dependencies for the application.
* templates/: Contains html files for python application
* main.py : Contains core application logic
* models.py : Contains Model used by Database
* GitHub/workflows/main.yml : Contains github actions ci/cd config logic
 
## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License - see the LICENSE file for details.

