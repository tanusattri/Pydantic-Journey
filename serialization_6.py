from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict
import pydantic


class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict= {'city':'gurgaon', 'state':'haryana', 'pin':'122001'}
address1= Address(**address_dict)
patient_info= {'name': 'John Doe', 'gender': 'male', 'age': 30, 'address': address1}
patient1= Patient(**patient_info)

temp= patient1.model_dump(exclude={'address':['state']}) #convert the patient1 object to a dictionary using model_dump() method
print(temp)
#print(type(temp))

#temp= patient1.model_dump_json() #convert the patient1 object to a json string using model_dump_json() method
#print(temp)
#print(type(temp))