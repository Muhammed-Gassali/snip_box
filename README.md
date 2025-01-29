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


