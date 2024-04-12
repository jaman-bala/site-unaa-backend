from ninja import Schema


class StreamSchema(Schema):
    id: int
    title: str
    rtsp_url: str

    class Config:
        orm_mode = True