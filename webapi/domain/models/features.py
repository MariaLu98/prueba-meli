from dataclasses import dataclass

@dataclass
class Features:
    screen_size: str
    internal_memory: str
    front_camera: str
    rear_camera: str
    nfc: bool
    unlock: str
