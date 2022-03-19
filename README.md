Current task I got from one the my technical interview

![image](https://user-images.githubusercontent.com/80515538/159109610-8c232eeb-6c04-4f11-8c27-6e1f16580a51.png)


In order to see how It works you should do this steps:

![gif](https://user-images.githubusercontent.com/80515538/159109543-7dd79163-c007-42d0-bb30-5f94a7e62e58.gif)

1) Activate virtual environment - venv
        1) Open command line
        2) type: venv\scripts\activate
2) Open terminal and run following code:
        1) uvicorn main:app --reload
        2) you should see output like this
                  INFO:     Will watch for changes in these directories: ['C:\\Users\\user\\Desktop\\CRUD_with_FASTAPI']
                  INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
                  INFO:     Started reloader process [10760] using statreload
                  WARNING:  The --reload flag should not be used in production on Windows.
                  INFO:     Started server process [5848]
                  INFO:     Waiting for application startup.
                  INFO:     Application startup complete.
3) Open browser and go to http://127.0.0.1:8000/docs you will see build in Swagger UI 
        ![image](https://user-images.githubusercontent.com/80515538/159106889-08862363-f758-4b5a-9dad-b3e63d373f8e.png)
4) Go and try it out! You can create new contact or see all contacts or search by id, update and delete by id. 
