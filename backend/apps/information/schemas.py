from datetime import datetime
from ninja import Schema


class RegisterCarBase(Schema):
    number: str
    title: str
    price: str
    created_date: datetime
    is_active: bool


class RegisterCar01(RegisterCarBase):
    class Config:
        orm_mode = True


class RegisterCar02(RegisterCarBase):
    class Config:
        orm_mode = True


class IssueCarBase(Schema):
    number: str
    title: str
    price: str
    created_date: datetime
    is_active: bool


class IssueCar01(IssueCarBase):
    class Config:
        orm_mode = True


class IssueCar02(IssueCarBase):
    class Config:
        orm_mode = True


class ConfirmationBase(Schema):
    number: str
    title: str
    price: str
    created_date: datetime
    is_active: bool


class ConfirmationOut(ConfirmationBase):
    class Config:
        orm_mode = True


class FaqBase(Schema):
    question_ru: str
    question_kg: str
    answer_ru: str
    answer_kg: str
    created_date: datetime
    is_active: bool


class FaqOUT(Schema):
    id: int
    question_ru: str
    question_kg: str
    answer_ru: str
    answer_kg: str

    class Config:
        orm_mode = True



