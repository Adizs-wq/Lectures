from uuid import uuid4
from pydantic import BaseModel, Field, EmailStr, AnyHttpUrl, SecretStr, UUID4

class User(BaseModel):
    id: UUID4 = Field(default_factory=uuid4,desription="User ID")
    email: EmailStr = Field(defalt = ..., description="User Email")
    name: str = Field(default = ..., description="User Name")
    age: int = Field(default = ..., description="User Age")
    personal_website: AnyHttpUrl = Field(default = ..., description="User Personal Website")
    password: SecretStr = Field(default = ..., description="User Password")


if __name__ == "__main__":
    user: User = User(
        email = "example@example.com",
        name = "John Doe",
        age = 30,
        personal_website = "https://example.com",
        password = SecretStr("password")
    )
    print(user)