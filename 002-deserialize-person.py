from pydantic import BaseModel, ValidationError
from utils import separator

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

    @property
    def display_name(self):
        return f"{self.first_name} {self.last_name}"
    
data = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30
}

# Works, but is not recommended
separator()

print("Instantiate the model the incorrect way using a dictionary")
p1 = Person(**data)
print(repr(p1))
separator()

print("Instantiate the model the correct way using a dictionary")
p2 = Person.model_validate(data)
print(repr(p2))
separator()

print("Instiantiate the model from a dictionary in a way that fails validation")
try:
    p3 = Person.model_validate({"first_name": "John", "last_name": "Doe", "age": "thirty"})
except ValidationError as ex:
    print(ex)
    separator()

print("Instantiate using json")
p4 = Person.model_validate_json('''
{
    "first_name": "John",
     "last_name": "Doe",
     "age": 30
}
''')
print(repr(p4))
separator()

print("Instiantiate the model from json in a way that fails validation")
try:
    p5 = Person.model_validate_json('''{"first_name": "John"}''')
except ValidationError as ex:
    print(ex)
    separator()