from pydantic import BaseModel
class Address(BaseModel):
    city:str
    state:str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age:int
    address : Address

address_dict = {'city':'gurgaon','state':'haryana','pin':"12202"}

address1 = Address(**address_dict)

patient_dict = {'name':"Madhu",'gender':"Male",'age':25,'address':address1}
patient1 = Patient(**patient_dict)

print(patient1.address.pin)
print(patient1.address.city)
