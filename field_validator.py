from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        valid_domains= ['hdfc.com','icici.com']
        #abc@gmail.com
        domain_name= value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of the following: {', '.join(valid_domains)}")
        return value
    
    @field_validator('name' )
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age',mode='before')
    @classmethod
    def validate_age(cls, value):
        if 0<value<100:
            return value
        else:
            raise ValueError("Age must be between 0 and 100")

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient. allergies)
    print(patient.contact_details)
patient_info= {'name': 'John Doe', 'age': 30, 'weight': 70.2, 'email': 'john.doe@icici.com', 'linkedin_url': 'https://www.linkedin.com/in/johndoe', 'married': True, 'allergies': ['penicillin','dust'], 'contact_details': {'phone': '123-456-7890'}} #Step2: Create a dictionary with patient information
patient1= Patient(**patient_info) # this is an object and ** is unpacking the dictionary
update_patient_data(patient1)