# 🛡️ Advanced Data Validation & Serialization with Pydantic 

Welcome to the **Pydantic Basics & Use Cases** architecture repository. This module forms the structural core of my data engineering workflow, establishing strict programmatic data enforcement, sanitization and typing mechanics for building production-ready Machine Learning data pipelines.

This repository serves as a deep technical playbook, moving beyond generic type hinting to leverage **Pydantic V2’s native Rust-backed validation engine**. It documents structural patterns designed to intercept malformed data payloads, perform structural mutations, execute cross-field logical checks, compute runtime fields and filter complex serialized data outputs.

---

## 🏗️ Core Pillars & Technical Architecture

The codebase maps out six essential architectural patterns required to transform raw, untrusted data payloads into safe, highly predictable system structures:

1. **Explicit Metadata & Parameter Constraints (`Field()` & `Annotated`)**
   * **Strict Type Enforcement:** Utilizing `strict=True` to explicitly disable standard Python type coercion (e.g., blocking the string `"70.2"` from silently parsing into a floating-point `70.2`).
   * **Numeric and String Bounds:** Injecting validation controls directly into structural type wrappers using boundaries like `gt=0` (Greater than zero) or `max_length=50`.

2. **Granular Field-Level Handlers (`@field_validator`)**
   * **Pre-Parsing Interceptions (`mode='before'`):** Validating or massaging primitive inputs *before* Pydantic casts them into structural types (e.g., intercepting an integer to check range values).
   * **Post-Parsing Mutations (Default `mode='after'`):** Executing logical filtering on verified typed variables, allowing for input mutations like converting text to `.upper()` or parsing email domains.

3. **Multi-Field Cross-Validation (`@model_validator`)**
   * **Context-Aware Business Logic:** Evaluating multi-field records simultaneously by running the validation wrapper at the instance-level (`mode='after'`).
   * **Conditional Assertions:** Enforcing specific data entries based on separate field parameters—such as requiring a nested emergency contact string *only if* a patient's age variable exceeds 60 years.

4. **Runtime Property Computations (`@computed_field`)**
   * **Dynamic Property Layering:** Generating read-only attributes on top of data models without introducing structural debt or writing extra attributes directly to a database schema.
   * **On-The-Fly Metrics Calculation:** Automatically evaluating and outputting formulas (e.g., calculating real-time body mass index) during object execution.

5. **Nested Architectural Composition**
   * **Modular Schema Hierarchies:** Embracing decoupled database concepts by nesting independent models (`Address`) inside wrapping structural models (`Patient`), enabling multi-tiered sub-object confirmation.

6. **Granular Export Filters & Serialization**
   * **Memory-to-Storage Transmutation:** Leveraging Pydantic's underlying serialization layer via `.model_dump()` and `.model_dump_json()`.
   * **Dynamic Information Masking:** Excluding sensitive or out-of-scope fields dynamically during export (e.g., stripping out nested elements like `address -> state` programmatically).

---

## 💻 Code Reference Implementation Blueprint

The entire suite is architected across modular sub-scripts, demonstrating the following clean programmatic implementations:

### Advanced Field Validations & Structural Configuration
```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50, title='Patient Name', description='Full legal name')]
    age: int 
    weight: Annotated[float, Field(gt=0, strict=True)]
    email: EmailStr
    married: Optional[bool] = Field(default=None)
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def validate_email(cls, value: str) -> str:
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of: {', '.join(valid_domains)}")
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value: str) -> str:
        return value.upper()
