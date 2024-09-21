from pydantic import ValidationError, BaseModel
from utils import separator

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}"

# Basic model instance creation
p1 = Person(first_name="John", last_name="Doe", age=21)
print(repr(p1))
print(repr(p1.model_fields))
separator()

# Access properties
print(f"Display Name: {p1.display_name}")
separator()

# Fails validation because all required fields are not passed in
try:
    Person(last_name="Doe")
except ValidationError as ex:
    print(ex)
    separator()

# Fails validation because age is a string instead of int
try:
    Person(first_name="John", last_name="Doe", age="twenty")
except ValidationError as ex:
    print(ex)
    separator()

# How to break encapsulation (oops)
p1.age = "twenty"
print(repr(p1))
p1.age = 21 # change it back
separator()