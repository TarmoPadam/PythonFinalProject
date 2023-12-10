## Table of Contents

-   [Table of Contents](#table-of-contents)
-   [Introduction](#introduction)
    -   [Installation](#installation)
-   [Working with Branches and Trello](#working-with-branches-and-trello)

## Introduction

This is a SDA final project for online shopping service with front and back office written in Django.

### Installation

1. **Clone the Repository and cd into it:**

    ```bash
    git clone https://github.com/EimantasBlazevicius/PythonRemoteEE19.git

    cd PythonRemoteEE19
    ```

2. **Create or Active your virtual environment(mac/windows):**

    Mac

    ```bash
    Create: python3 -m venv venv
    Activate: source venv/bin/activate
    ```

    Windows

    ```bash
    Create: python -m venv venv
    Activate: venv/Scripts/activate
    switch branch to "developer"
    ```

3. **Install the Requirements:**
    ```bash
    pip install -r requirements.txt
    ```
5. **Do the Migrations:**
    ```bash
    python manage.py makemigraitons
    python manage.py migrate
    ```
6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Working with Branches and Trello

1. **Get the ticket number**

    - Go to the Trello board and find the ticket you are working on.
    - The ticket number is the number in the title of the ticket starting with RR-, complete ticket number example is RR-0001.

2. **Create a new branch**

    - Create a new branch with the ticket type and the ticket number.
    - Example: feature/RR-0001, fix/RR-0001
    - In the VS Code click on the dev or main branch button, from the top menu select "Create a new branch from..." and select dev after that enter the name of the new branch(e.g.: feature/RR-0001).

3. **Committing and pushing changes**

    - After you have made changes to the code you need to commit and push them to the repository.
    - Click on the source control button in the left menu.
    - In the top menu click on the plus button to stage all changes.
    - Enter a commit message in a format of
        ```bash
        feature(scope):RR-0001: message
        ```
        and click on the check mark to commit the changes.
    - Click on the three dots in the top menu and select "Push" OR click Sync changes button.

4. **Creating a pull request**

    - After you have pushed your changes to the repository you need to create a pull request.
    - Go to the repository on GitHub and click on the "Pull requests" tab.
    - Click on the "New pull request" button.
    - Select the dev branch as the base branch and your branch as the compare branch.
    - Click on the "Create pull request" button.
    - Add a title to the pull request in the following format:
        ```bash
        feature(scope):RR-0001: message
        ```
    - Add a description to the pull request that should be a URL to the ticket in the Trello board.
    - Mark your self as an assignee.
    - Add at least 3 team mates and the teacher as reviewers.
    - Click on the "Create pull request" button.
    - Add the ticket to the "Code review" column on the Trello board.

5. Once Pull request is approved and merged to the dev branch, you can move the ticket to "Ready for QA" column on the Trello board.
6. If the ticket will not pass the QA it will be return to "TO DO" board and assigned to the developer that was working on that ticket originally. Follow the process from step 3.
7. Once ticket pass the QA it will occur in the "Done" column in the Trello board.
