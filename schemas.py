from pydantic import BaseModel

# Create contact Schema (Pydantic Model)
class ClientRequest(BaseModel):
    name: str
    phone: int
    