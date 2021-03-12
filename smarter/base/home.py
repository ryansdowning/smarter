import cv2

class Home:
    def __init__(self, rooms: list[Room], users: list[User]):
        self.rooms = rooms


class Room:
    def __init__(self, name: str, camera: Camera):
        self.name = name
        self.camera = camera


class User:
    def __init__(self, name: str):
        self.name = name


class Camera:
    def __init__(self, video: str):
        self.video = cv2.VideoCapture(video)

    def detect_faces(self) -> list:
        raise NotImplementedError