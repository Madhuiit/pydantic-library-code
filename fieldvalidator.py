from pydantic import  BaseModel, EmailStr,AnyUrl,Field , field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight:float
    married : bool
    allergies : List[str]
    contact_detail : Dict[str,str]

    @field_validator('email')

    @classmethod
    def email_validator(cls,value):
        valid_domain = ['hdfc.com','icici.com']

        # abc@gmail.com
        domain_name = value.split("@")[-1]
        if domain_name  not in  valid_domain:
            raise  ValueError("Not a valid domain")
        
        return value
    @field_validator('name',mode="after")
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age')

    @classmethod
    def validate_age(cls,value):
        if  0 < value < 100:
            return value
        else:
            raise ValueError("age shoud be in between 0 and 100")
        



    


patient_info = {
    'name':'nitish', 'email':"abc@hdfc.com", 
    'linkedin':'http://linkidin.com/123','age':'30','weight':56.8,
    'married':True,
    'allergies':['plumix','dust'],
    'contact_detail':{'email':"abc@gmail.com",'phone':'2345678'}
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