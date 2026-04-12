import time
import hid_gamepad
from steering import read_steering, engine_on
from accelerator import read_accelerator

while True:
    try:
        hid_gamepad.gamepad.send_gamepad(read_steering(), read_accelerator(), engine_on())
    except Exception:
        pass
    time.sleep_ms(16)  # ~60hz
