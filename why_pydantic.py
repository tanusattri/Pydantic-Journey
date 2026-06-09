from pydantic import BaseModel, EmailStr, AnyUrl, Field 
from typing import List, Dict, Optional, Annotated
class Patient(BaseModel): #Step1: Define a Pydantic model (class)
    #name: str= Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='The name of the patient', example='John Doe')] #This is another way to define the field with validation using Annotated
    age: int 
    weight: Annotated[float, Field(gt=0, strict=True)] #This is another way to define the field with validation using Annotated, gt means greater than 0 and strict means it will not allow type coercion
    email: EmailStr
    linkedin_url: AnyUrl
    married: Optional[bool] = Field(default=None) #By default every field is required, but we can make it optional by using Optional and providing a default value of None
    allergies: Optional[List[str]]= None #This is done for 2 level validation that list contains string format data only
    contact_details: Dict[str, str] 

def insert_patient_data(patient: Patient): #Step3: Create a function to insert patient data, which takes a Patient object as an argument
    #if type(name)== str and type(age)== int: #Type Validation
        #if age<0: #Data Validation
            #raise ValueError("Age cannot be negative")
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.email)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("Inserted data successfully")
    #else:
        #raise TypeError("Incorrect data type for name or age")

#insert_patient_data("John Doe", 30) # This will work fine 
#insert_patient_data("John Doe", '30') # This will raise a TypeError

patient_info= {'name': 'John Doe', 'age': 30, 'weight': 70.2, 'email': 'john.doe@example.com', 'linkedin_url': 'https://www.linkedin.com/in/johndoe', 'married': True, 'allergies': ['penicillin','dust'], 'contact_details': {'phone': '123-456-7890'}} #Step2: Create a dictionary with patient information
#patient_info_invalid= {'name': 'John Doe', 'age': 'thirty'}
patient1= Patient(**patient_info) # this is an object and ** is unpacking the dictionary
#patient2= Patient(**patient_info_invalid) # this will raise a validation error
insert_patient_data(patient1) # This will work fine