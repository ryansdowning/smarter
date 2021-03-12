USERS = ('user1', 'user2', 'user3', 'user4')
ROOMS = ('room1', 'room2', 'room3', 'room4')

DEVICES = {
    'camera1': {'room': 'room1', 'ip': 'ip1'},
    'camera2': {'room': 'room2', 'ip': 'ip2'},
    'camera3': {'room': 'room3', 'ip': 'ip3'},
    'camera4': {'room': 'room4', 'ip': 'ip4'},
}

HUE_BRIDGE_IP = '192.168.'
if HUE_BRIDGE_IP is not None:
    from phue import Bridge
    HUE_BRIDGE = Bridge(HUE_BRIDGE_IP)
    HUE_BRIDGE.connect()
else:
    HUE_BRIDGE = None

