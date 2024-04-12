from ninja import Schema


class RegistrationInput(Schema):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


class RegisterOUT(Schema):
    id: int
    username: str
    password: str
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class LoginInput(Schema):
    username: str
    password: str
