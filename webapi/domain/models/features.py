from pydantic import BaseModel

class Features(BaseModel):
    screen_size: str
    internal_memory: str
    front_camera: str
    rear_camera: str
    nfc: bool
    unlock: str
