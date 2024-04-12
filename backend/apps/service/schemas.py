from ninja import Schema


class CalculatorCarSchema(Schema):
    id: int
    car: str


class CalculatorVolumeSchema(Schema):
    id: int
    volume: str


class CalculatorYearSchema(Schema):
    id: int
    year: str


class CalculatorEngineSchema(Schema):
    id: int
    engine: str


class CalculatorStatusSchema(Schema):
    id: int
    status: str


class CalculatorAllListSchema(Schema):
    id: int
    car: CalculatorCarSchema
    volume: CalculatorVolumeSchema
    year: CalculatorYearSchema
    engine: CalculatorEngineSchema
    status: CalculatorStatusSchema
    sum: str

    class Config:
        orm_mode = True


