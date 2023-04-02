# QuizMaster Challenge

Welcome! This challenge is designed to assess your Python, React, and web development abilities, 
specifically focusing on the following skills:
- Django (Python web framework)
- React (JavaScript library for building user interfaces)
- MongoDB (NoSQL database)
- Docker (Containerization platform)
- API integration and communication between frontend and backend

The task is intentionally unconventional and involves a slightly complex setup, requiring you to quickly learn basic Docker concepts.

## Prerequisites and Tooling
Before getting started, make sure your machine is equipped with the following:

- Docker: Install Docker Desktop for Windows or Mac, or Docker Engine for Linux.
- Git: Install Git for version control.
- IDE/Text Editor: Use your preferred text editor or IDE for Python and JavaScript development (e.g., Visual Studio Code, PyCharm, or Sublime Text).
- Basic knowledge of Python, React, and MongoDB is required.

In case you have any issues with the setup, please reachout to us!

## Project Structure
This repository contains code for a Docker setup with 3 containers:

- Frontend: This is the React development server running on http://localhost:3000. The source code for this can be found in the src/app directory.
- Backend: This is the backend container running a Django instance on http://localhost:8000.
- Database: This is a MongoDB instance running on port 27017. Django views have pre-written code to connect to this MongoDB instance.
We strongly recommend you review the Dockerfile and docker-compose.yml files. 
Demonstrating your understanding of the setup will be a significant advantage.


## Setup
1. Clone this repository
```
git clone https://github.com/whatify-io/quizmaster_challenge.git
```
2. Change into the cloned directory

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
CONTAINER ID   IMAGE                           COMMAND                  CREATED          STATUS          PORTS                                 NAMES
ad8ea8390e6e   quizmaster_challenge-frontend   "docker-entrypoint.s…"   29 minutes ago   Up 15 seconds   0.0.0.0:3000->3000/tcp                quizmaster_challenge-frontend-1
f6c39b0ddec9   quizmaster_challenge-backend    "python manage.py ru…"   29 minutes ago   Up 15 seconds   0.0.0.0:8000->8000/tcp                quizmaster_challenge-backend-1
6d422b666750   mongo:6.0                       "docker-entrypoint.s…"   29 minutes ago   Up 16 seconds   27017/tcp, 0.0.0.0:27018->27018/tcp   quiz_mongo
```
6. Check that you are able to access http://localhost:3000 and http://localhost:8000/todos
7. If the containers in #5 or #6 are not up, we would like you to use your debugging skills to figure out the issue. 
Only reach out to us if you've exhausted all possible options.
The `quizmaster_challenge-frontend` container may take a good amount of time to start since it will download all package dependencies.

# Tips
1. Once containers are up and running, you can view container logs by executing `docker logs -f --tail=100 {container_name}` 
   Replace `container_name` with `quizmaster_challenge-backend` or `quizmaster_challenge-frontend`(output of `docker ps`)
2. You can enter the container and inspect it by executing `docker exec -it {container_name} bash`.
   Replace `container_name` with `quizmaster_challenge-backend` or `quizmaster_challenge-frontend`(output of `docker ps`)
3. Shut all containers using `docker-compose down`
4. Restart a container using `docker restart {container_name}`


# Task
When you run `localhost:3000`, you would see a banner saying QuizMaster.
In the backend(views.py) you will see placeholder implementation of APIs for:
- getting all quizzes
- getting a quiz by id
- creating a quiz
- submitting a quiz and getting score

Your task is to create frontend components and connect it with these APIs.
On the backend, you can save all data in mongodb using the mongo client that
is created in `db_accessor.py`.
While creating the frontend, do not focus a lot on aesthetics but on core functionality.  
The code quality in your solution should be production-ready - error handling, abstractions, well-maintainable and modular code.

An example implementation would be:
- Follow http://skote-v-light.react.themesbrand.com/job-grid to show all quizzes in a grid.
- Have a "Create Quiz" button on top which opens up a form to create a quiz. 
  You can assume the quiz would have 5 questions, each with 4 options out of which there is 1 correct option.
  Once the question and options are filled, you can click on "Submit" which should call the right API
  on backend to save the quiz in database and redirect to the home page.
- Have a button on the quiz tile to "Take a Quiz" which loads all the questions and options for it in a form.
  The form has a "Submit" button which submits the quiz with selection options to backend which then
  evaluates the scoring and returns the score to user.

# Instructions
1. All React code should be implemented using [React hooks](https://reactjs.org/docs/hooks-intro.html) and should not use traditional stateful React components and component lifecycle method.
2. Do not use Django's model or SQLite DB. Persist and retrieve all data from the mongo instance. A database instance is already present in `db_accessor.py`.
3. We are looking for developers who have strong fundamentals and can ramp up fast. We expect you to learn and grasp basic React Hooks/Mongo/Docker concepts on the fly.
4. Do not submit your solution as a PR since this is a public repo and there are other candidates taking the same test. Send us a link to your repo privately.
5. If you are able to complete the test, we will have a live walkthrough of your code and ask questions to check your understanding.
