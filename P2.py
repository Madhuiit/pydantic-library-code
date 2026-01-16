from pydantic import  BaseModel, EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight:float
    married : bool
    allergies : List[str]
    contact_detail : Dict[str,str]
 
def insert_in_database(patient: Patient):
    print()