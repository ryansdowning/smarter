import cv2
from smarter.config import HUE_BRIDGE
from phue import Bridge

class Home:
    def __init__(self, rooms: list[Room], users: list[User]):
        self.rooms = rooms


class Room:
    def __init__(self, name: str, devices: Dict[str, Device]):
        self.name = name
        self.devices = devices
        self.camera = devices['camera']


class User:
    def __init__(self, name: str):
        self.name = name


class Device:
    def __init__(self, id_: str):
        self.id = id_


class Camera(Device):
    def __init__(self, id_: str, video: str):
        super(Camera, self).__init__(id_)
        self.video = cv2.VideoCapture(video)

    def detect_faces(self) -> list:
        raise NotImplementedError

    def __str__(self):
        return f"Camera Device: {self.id_}"


class Light(Device):
    def __init__(self, id_: str, light_id: int):
        super(Camera, self).__init__(id_)
        self.light_id = light_id
        self.name = HUE_BRIDGE.get_light(self.light_id, 'name')

    def set_light(self, *args, **kwargs):
        return HUE_BRIDGE.set_light(self.light_id, *args, **kwargs)

    def __str__(self):
        return f"Light Device: {self.id_} with Light id: {self.light_id}"