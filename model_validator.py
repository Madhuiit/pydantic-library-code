from pydantic import  BaseModel, EmailStr, model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight:float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]


    @model_validator(mode="after")

    def validate_emergency_contact(cls,model):
        if  model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("patient older then 60 must have an emergency contact number")
        
        return model
    


    


patient_info = {
    'name':'nitish', 'email':"abc@hdfc.com", 
    'linkedin':'http://linkidin.com/123','age':'63','weight':56.8,
    'married':True,
    'allergies':['plumix','dust'],
    'contact_details':{'email':"abc@gmail.com",'phone':'2345678','emergency':'234567'}
    }

patient1 = Patient(**patient_info) # validation perform -> type coercison

def update(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
   
    print("data is being updated ......")
    print("Data updated")
update(patient1)