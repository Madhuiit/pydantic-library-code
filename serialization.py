from pydantic import BaseModel
class Address(BaseModel):
    city:str
    state:str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str = "Male"
    age:int
    address : Address

address_dict = {'city':'gurgaon','state':'haryana','pin':"12202"}

address1 = Address(**address_dict)

patient_dict = {'name':"Madhu",'age':25,'address':address1}
patient1 = Patient(**patient_dict)



temp = patient1.model_dump()
print(temp)
print(type(temp))

temp2  = patient1.model_dump_json()
print(temp2)

temp3 = patient1.model_dump(include=["name"])
print(temp3)

temp4 = patient1.model_dump(exclude=["name","gender"])
print(temp4)
temp5 = patient1.model_dump(exclude={'address':['state']})
print(temp5)

# exclude set dont print the defualt set values

temp6 = patient1.model_dump(exclude_unset=True)

print(temp6)





