# To-do-Calendar
To do list with a calendar

# FILE TREE:
- /src : Code directory
    - /View: Contain views:
        - calendar_view.py
        - todo_app.py
    - /Controller: Contain controllers:
        - friends_controller.py
        - tag_controller.py
        - task_action_controller.py
        - task_controller.py
        - user_controller.py
    - /Models: Contain models:
        - friends_model.py
        - tag_model.py
        - task_action_model.py
        - task_model.py
        - user_model.py
    - friends.py
    - main.py
    - tag.py
    - task.py
    - user.py
    - utils.py
- /Test : Test directory
    - friends_controller_test.py
    - tag_controller_test.py
    - task_action_controller_test.py
    - task_controller_test.py
    - user_controller_test.py

- /DB : Database files
    - create_db.py : Script to recover the DB to a consistent state in case of bugs (it erases all DB users, tags and tasks and creates new ones)
    - to_do_calendar_test.db : DB of the App


- /public/img : Logos of the App
    - logo_sm.ico
    - LOGO.png

# Features
## Task
- create
- edit
- delete
- show description
## Calendar
- View tasks and their tags in the calendar
## tags
- create
- manage color
- assign to tasks
## user
- login
- register
## Other
- Consistent tasks and tags in database
