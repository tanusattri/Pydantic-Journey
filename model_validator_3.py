from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Dict, Optional, Annotated

import pydantic

class Patient(pydantic.BaseModel):
    name: str
    email: pydantic.EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    
    @pydantic.model_validator(mode='after')
    def validate_emergency_contact(cls, value):
        if value.age>60 and 'emergency' not in value.contact_details:
            raise ValueError("Emergency contact details are required for patients above 60 years of age")
        return value

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient. allergies)
    print(patient.contact_details)
patient_info= {'name': 'John Doe', 'age': 30, 'weight': 70.2, 'email': 'john.doe@icici.com', 'linkedin_url': 'https://www.linkedin.com/in/johndoe', 'married': True, 'allergies': ['penicillin','dust'], 'contact_details': {'phone': '123-456-7890', 'emergency':'488563845643856'}} #Step2: Create a dictionary with patient information
patient1= Patient(**patient_info) # this is an object and ** is unpacking the dictionary
update_patient_data(patient1)
