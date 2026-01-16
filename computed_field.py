from pydantic import  BaseModel, EmailStr, computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight:float
    height:  float
    married : bool
    allergies : List[str]
    contact_details : Dict[str,str]


    # @model_validator(mode="after")

    # def validate_emergency_contact(cls,model):
    #     if  model.age > 60 and 'emergency' not in model.contact_details:
    #         raise ValueError("patient older then 60 must have an emergency contact number")
        
    #     return model

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/self.height**2 ,2)

       


    


    


patient_info = {
    'name':'nitish', 'email':"abc@hdfc.com", 
    'linkedin':'http://linkidin.com/123','age':'63','weight':56.8,
    'height': 1.72,
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
    print(patient.bmi)
   
    print("data is being updated ......")
    print("Data updated")
update(patient1)