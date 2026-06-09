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
print(patient1)
print(patient1.address)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin)