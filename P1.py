from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name :Annotated[str,Field(max_length=50, title="name of the  patiendt ",description="give the  name of the patient", examples=["Nitesh","Ram"])]
    email : EmailStr
    linkedin : AnyUrl
    age:  int = Field(gt=0,lt=120)
    weight: Annotated[float,Field(ge=0,stric = True)]
    married : Annotated[bool,Field(default=None,description="Is the patient married or not")]
    allergies : Annotated[Optional[List[str]],Field(default=None,max_length=5)]
    contact_detail : Dict[str ,str]
    

def inser_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient1.married)
    print("inserted")

def update(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("name added and   have been updated ")
patient_info = {'name':'nitish', 'email':"abc@gmail.com", 'linkedin':'http://linkidin.com/123','age':30,'weight':56.8,'allergies':['plumix','dust'],'contact_detail':{'email':"abc@gmail.com",'phone':'2345678'}}




patient1 = Patient(**patient_info)

inser_patient(patient1)
update(patient1)


