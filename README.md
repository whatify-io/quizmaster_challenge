### QuizMaster Challenge

Welcome! This challenge is designed to assess your Python, React, and web development abilities, 
specifically focusing on the following skills:
- Django (Python web framework)
- React (JavaScript library for building user interfaces)
- MongoDB (NoSQL database)
- Docker (Containerization platform)
- API integration and communication between frontend and backend

The task is intentionally unconventional and involves a slightly complex setup, requiring you to quickly learn basic Docker concepts.

### Prerequisites and Tooling
Before getting started, make sure your machine is equipped with the following:

- Docker: Install Docker Desktop for Windows or Mac, or Docker Engine for Linux.
- Git: Install Git for version control.
- IDE/Text Editor: Use your preferred text editor or IDE for Python and JavaScript development (e.g., Visual Studio Code, PyCharm, or Sublime Text).
- Basic knowledge of Python, React, and MongoDB is required.

In case you have any issues with the setup, please reachout to us!

### Project Structure
This repository contains code for a Docker setup with 3 containers:

- Frontend: This is the React development server running on http://localhost:3000. The source code for this can be found in the src/app directory.
- Backend: This is the backend container running a Django instance on http://localhost:8000.
- Database: This is a MongoDB instance running on port 27017. Django views have pre-written code to connect to this MongoDB instance.
We strongly recommend you review the Dockerfile and docker-compose.yml files. 
Demonstrating your understanding of the setup will be a significant advantage.


# Setup
1. Clone this repository
```
git clone https://github.com/whatifyio/quizmaster_challenge.git
```
2. Change into the cloned directory and set the environment variable for the code path. Replace `path_to_repository` appropriately.
```
export WHATIFY_CODEBASE_PATH="{path_to_repository}/test/src"
```
3. Build container (you only need to build containers for the first time or if you change image definition, i.e., `Dockerfile`). This step will take a good amount of time.
```
docker-compose build
```
4. Once the build is completed, start the containers:
```
docker-compose up -d
```
5. Once complete, `docker ps` should output something like this:
```
CONTAINER ID   IMAGE               COMMAND                  CREATED         STATUS         PORTS                      NAMES
e445be7efa61   adbrew_test_api     "bash -c 'cd /src/re…"   3 minutes ago   Up 2 seconds   0.0.0.0:8000->8000/tcp     api
0fd203f12d8a   adbrew_test_app     "bash -c 'cd /src/ap…"   4 minutes ago   Up 3 minutes   0.0.0.0:3000->3000/tcp     app
884cb9296791   adbrew_test_mongo   "/usr/bin/mongod --b…"   4 minutes ago   Up 3 minutes   0.0.0.0:27017->27017/tcp   mongo
```
6. Check that you are able to access http://localhost:3000 and http://localhost:8000/todos
7. If the containers in #5 or #6 are not up, we would like you to use your debugging skills to figure out the issue. Only reach out to us if you've exhausted all possible options. 
The `app` container may take a good amount of time to start since it will download all package dependencies.

# Tips
1. Once containers are up and running, you can view container logs by executing `docker logs -f --tail=100 {container_name}` Replace `container_name` with `app` or `api`(output of `docker ps`)
2. You can enter the container and inspect it by executing `docker exec -it {container_name} bash` Replace `{container_name}` with `app` or `api` (output of `docker ps`)
3. Shut all containers using `docker-compose down`
4. Restart a container using `docker restart {container_name}`


# Task
When you run `localhost:3000`, you would see 2 things:
1. A form with a TODO description textbox and a submit button. On this form submission, the app should interact with the Django backend (`POST http://localhost:8000/todos`) and create a TODO in MongoDB.
2. A list with hardcoded TODOs. This should be changed to reflect TODOs in the backend (`GET http://localhost:8000/todos`).
3. When the form is submitted, the TODO list should refresh again and fetch latest list of TODOs from MongoDB.

# Instructions
1. All React code should be implemented using [React hooks](https://reactjs.org/docs/hooks-intro.html) and should not use traditional stateful React components and component lifecycle method.
2. Do not use Django's model or SQLite DB. Persist and retrieve all data from the mongo instance. A `db` instance is already present in `views.py`.
3. We are looking for developers who have strong fundamentals and can ramp up fast. We expect you to learn and grasp basic React Hooks/Mongo/Docker concepts on the fly.
4. Do not submit your solution as a PR since this is a public repo and there are other candidates taking the same test. Send us a link to your repo privately.
5. If you are able to complete the test, we will have a live walkthrough of your code and ask questions to check your understanding.

### End Goal
The primary objective of this challenge is to create a simple Quiz application that allows users to view, create, and take quizzes. The application should communicate with a Django backend to store and retrieve quiz data from a MongoDB database.
Keep in mind that while the challenge aims to test your ability to create a functional application, you need not chase optimization or implement advanced features. Focus on creating a working solution that demonstrates your understanding of the core technologies involved and your ability to work with them effectively.
The code quality in your solution should be production-ready - error handling, abstractions, well-maintainable and modular code.

Good luck!
