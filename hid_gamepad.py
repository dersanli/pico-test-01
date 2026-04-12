import struct
from usb.device.hid import HIDInterface

# HID descriptor: 1 signed 16-bit axis (steering) + 1 button (engine)
_DESCRIPTOR = bytes([
    0x05, 0x01,        # Usage Page (Generic Desktop)
    0x09, 0x05,        # Usage (Gamepad)
    0xA1, 0x01,        # Collection (Application)
    0xA1, 0x00,        #   Collection (Physical)
    0x09, 0x30,        #     Usage (X axis)
    0x16, 0x01, 0x80,  #     Logical Minimum (-32767)
    0x26, 0xFF, 0x7F,  #     Logical Maximum (32767)
    0x75, 0x10,        #     Report Size (16 bits)
    0x95, 0x01,        #     Report Count (1)
    0x81, 0x02,        #     Input (Data, Variable, Absolute)
    0x05, 0x09,        #     Usage Page (Button)
    0x19, 0x01,        #     Usage Minimum (1)
    0x29, 0x01,        #     Usage Maximum (1)
    0x15, 0x00,        #     Logical Minimum (0)
    0x25, 0x01,        #     Logical Maximum (1)
    0x75, 0x01,        #     Report Size (1 bit)
    0x95, 0x01,        #     Report Count (1)
    0x81, 0x02,        #     Input (Data, Variable, Absolute)
    0x75, 0x07,        #     Report Size (7 bits padding)
    0x95, 0x01,        #     Report Count (1)
    0x81, 0x03,        #     Input (Constant) - padding to full byte
    0xC0,              #   End Collection
    0xC0,              # End Collection
])

class GamepadHID(HIDInterface):
    def __init__(self):
        super().__init__(_DESCRIPTOR)
        self._report = bytearray(3)  # 2 bytes steering + 1 byte button

    def send_gamepad(self, steering, engine_on):
        struct.pack_into('<h', self._report, 0, steering)
        self._report[2] = 0x01 if engine_on else 0x00
        if not self.busy():
            self.send_report(self._report)


gamepad = None  # Set by boot.py before main.py runs

def init():
    import usb.device
    gamepad = GamepadHID()
    usb.device.get().init(gamepad, builtin_driver=True)
    return gamepad
