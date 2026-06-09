from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict
import pydantic

from model_validator_3 import update_patient_data

class Patient(pydantic.BaseModel):
    name: str
    email: pydantic.EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculated_bmi(self)-> float:
        bmi= round(self.weight/(self.height**2),2)
        return bmi
    
    def update_patient_data(patient: Patient):
        print(patient.name)
        print(patient.email)
        print(patient.age)
        print(patient.weight)
        print(patient.height)
        print(patient.married)
        print(patient. allergies)
        print(patient.contact_details)
        print("BMI",patient.calculated_bmi)

patient_info= {'name': 'John Doe', 'age': 30, 'weight': 70.2, 'height': 1.75, 'email': 'john.doe@icici.com', 'linkedin_url': 'https://www.linkedin.com/in/johndoe', 'married': True, 'allergies': ['penicillin','dust'], 'contact_details': {'phone': '123-456-7890', 'emergency':'488563845643856'}} #Step2: Create a dictionary with patient information
patient1= Patient(**patient_info) # this is an object and ** is unpacking the dictionary
update_patient_data(patient1)