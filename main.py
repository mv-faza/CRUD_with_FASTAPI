from fastapi import FastAPI, status, HTTPException
from database import Base, engine
from sqlalchemy.orm import Session
import models
import schemas


# Create the database
Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/contacts", status_code=status.HTTP_201_CREATED)
async def create_contact(details: schemas.ClientRequest):
    
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ContactInfo database model
    contactdb = models.ContactInfo(name = details.name, phone = details.phone)
    
    # add it to the session and commit it
    session.add(contactdb)
    session.commit()

    # grab the id given to the object from the database
    id = contactdb.id

    # close the session
    session.close()

    # return the id
    return f"created contact with id {id}"

@app.delete("/contacts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_contact(id: int):
     # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the given id
    delete_contact = session.query(models.ContactInfo).get(id)

    # if given id exists, delete it from the database. Otherwise raise 404 error
    if delete_contact:
        session.delete(delete_contact)
        session.commit()
        session.close()
    else:
        raise HTTPException(status_code=404, detail=f"contact with id {id} not found")

    return None

@app.get("/contacts/{id}")
async def read_contact(id:int):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get the name with the given id
    user = session.query(models.ContactInfo).get(id)

    # close the session
    session.close()

    if not user:
        raise HTTPException(status_code=404, detail=f"user with id {id} not found")

    return user

@app.put("/contacts/{id}")
async def updatte_contact(id: int, name: str, phone: int):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get item with the given id
    edit_info = session.query(models.ContactInfo).get(id)

    # update contact info 
    if edit_info:
        edit_info.name = name
        edit_info.phone = phone
        session.commit()

    # close the session
    session.close()

    # check if contact with given id exists. If not, raise exception and return 404 not found response
    if not edit_info:
        raise HTTPException(status_code=404, detail=f"contact with id {id} not found")

    return edit_info

@app.get("/contacts")
async def read_contact():
     # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # get all contacts
    contacts_list = session.query(models.ContactInfo).all()

    # close the session
    session.close()

    return contacts_list