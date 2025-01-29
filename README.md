# snip_box
The short note-saving app features two database models: Tag and ShortNote. The Tag model contains a unique title field, while the ShortNote model includes fields for the title and note details, along with two auto-filled date fields for creation and updates. Additionally, the ShortNote model has two foreign key fields to establish relationships with the Tag model and the default user model. Each short note is always connected to these two relational models, ensuring organized and efficient note management

All APIs in the application utilize JWT (JSON Web Token) authentication to secure data and ensure that only authorized users can access or modify their notes. 

Users can perform various operations, including creating, reading, deleting, and listing short notes, as well as listing and managing tags. Additionally, users can view all short notes associated with a specific tag.

## Installation

To run this project, you will need to install Python, Django, Django REST Framework, and the Django REST Framework JWT package. Exact versions and packages mentioned in requirements.txt

## Authentication

The standard DRF JWT API endpoints are used for token creation and refresh:

*   `/api/token/`:  Use this endpoint to obtain a new JWT. You'll need to provide your username and password in the request body.
*   `/api/token/refresh/`: Use this endpoint to refresh an existing JWT. You'll need to provide a refresh token in the request body.

A user with the username `gassali` and password `haigassali` has already been created. You can use these credentials to obtain a token.

## User Creation

A separate API endpoint is provided for creating new users:

*   `/api/create-user/`: This endpoint allows you to register a new user.  You will need to provide the required user details (e.g., username, password, email) in the request body.

{
    "username": "gassali",
    "password": "haigassali"
}

You can choose to either use the existing `gassali` user or create a new user using the registration API.  After obtaining a JWT, you can use it in the `Authorization` header of subsequent requests to access protected endpoints.  The token should be included as a Bearer token:

## steps to deploy project using Docker

1. install docker from docker website
2. create dockerfile. create a dockerfile without any extension in your project root directory. it will create docker image for this project
3. create .dockerignore file in the root directory to exclude unnecessary files from the Docker image. it is like git ignore file.
4. create docker compose file - create docker-compose.yml file in project root directory for database integration and other services.
5. build docker image by running `docker-compose build` command.
6. run docker container using `docker-compose up` command. This command will start our Django application and any other services defined in the `docker-compose.yml` file.
7. migrate database by using `docker-compose exec web python manage.py migrate`
8. manage static file  by running `docker-compose exec web python manage.py collectstatic` like we run `python manage.py collectstatic`
9. we can access docker container in default port `http://localhost:8000`
10. we can kill containers press `Ctrl + C` like we are doing in terminal or we can done by running `docker-compose down` command.

