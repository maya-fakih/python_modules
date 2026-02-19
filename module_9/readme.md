*This project has been created as part of the 42 curriculum by mfakih.*


Pydantic Models & Validation
A quick guide to data validation in Python

What is Pydantic?
Data validation library that enforces types at runtime. No more guessing if that "int" is actually a string.

Core Concepts
BaseModel
The foundation. Inherit from it to create validated data structures.

python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

# "30" → 30 automatically
user = User(name="Alex", age="30")  # ✅ Works
Field()
Add extra validation rules beyond type hints.

python
from pydantic import BaseModel, Field

class Product(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    price: float = Field(gt=0, le=10000)  # >0, ≤10000
    in_stock: bool = Field(default=True)
Validation Errors
Pydantic collects all errors before raising.

python
try:
    user = User(name=123, age="old")  
except ValidationError as e:
    print(e.errors())  # Shows both errors at once
Enums
Restrict values to a predefined set.

python
from enum import Enum

class Rank(str, Enum):  # str = JSON friendly
    CAPTAIN = "captain"
    COMMANDER = "commander"

user.rank = Rank.CAPTAIN  # ✅
user.rank = "general"      # ❌ ValidationError
Model Validator
Validate rules involving multiple fields.

python
from pydantic import BaseModel, model_validator

class Order(BaseModel):
    items: int
    price: float

    @model_validator(mode="after")
    def check_total(self):
        if self.items * self.price > 1000:
            raise ValueError("Order too expensive")
        return self
Nested Models
Models inside models. Validation happens recursively.

python
class CrewMember(BaseModel):
    name: str
    active: bool

class Mission(BaseModel):
    name: str
    crew: List[CrewMember]  # Each member validated

# If any crew member is invalid → whole mission fails
Key Number Constraints
Short	Meaning	Example
gt	greater than (>)	Field(gt=0)
ge	greater or equal (>=)	Field(ge=18)
lt	less than (<)	Field(lt=100)
le	less or equal (<=)	Field(le=10)
Quick Reference: V1 vs V2
V1 (old)	V2 (new)
.dict()	.model_dump()
.json()	.model_dump_json()
parse_obj()	.model_validate()
@validator	@field_validator
@root_validator	@model_validator
class Config	model_config = ConfigDict()
Why Use Pydantic?
Type safety at runtime

Self-documenting code

Automatic parsing (strings → ints/datetime)

Clear error messages

Nested validation built-in

"Type hints that actually enforce themselves."

