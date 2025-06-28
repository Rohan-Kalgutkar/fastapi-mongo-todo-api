from pydantic import BaseModel, Field

class Todo(BaseModel):
    name: str = Field(..., description="Name of the todo item")
    description: str = Field(..., description="Description of the todo item")
    completed: bool = Field(default=False, description="Completion status of the todo item")
    
    