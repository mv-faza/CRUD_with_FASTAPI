 Current task I got from one of the my technical interview

 ![image](https://user-images.githubusercontent.com/80515538/159109610-8c232eeb-6c04-4f11-8c27-6e1f16580a51.png)


 In order to see how It works you should do this steps:

 ![gif](https://user-images.githubusercontent.com/80515538/159109543-7dd79163-c007-42d0-bb30-5f94a7e62e58.gif)

1) Activate virtual environment - venv
        
								1) Open command line
        
								2) type: venv\scripts\activate

2) Open terminal and run following code:
        
								1) uvicorn main:app --reload
        
								2) you should see output like this
      ![image](https://user-images.githubusercontent.com/80515538/159109746-5c88319e-04d8-4ad3-990b-c08c54dab18f.png)

3) Open browser and go to http://127.0.0.1:8000/docs you will see build in Swagger UI 
        ![image](https://user-images.githubusercontent.com/80515538/159106889-08862363-f758-4b5a-9dad-b3e63d373f8e.png)

4) Go and try it out! You can create new contact, see all contacts, search by id or update and delete by id. 
