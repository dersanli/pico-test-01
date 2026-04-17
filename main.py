import time
from machine import Pin, ADC
import hid_gamepad

steering = ADC(Pin(28))
buttons = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (16, 17, 18, 19)]

def read_steering(samples=8):
    raw = sum(steering.read_u16() for _ in range(samples)) // samples
    return raw - 32768

while True:
    s = read_steering()
    btn_bits = sum((1 << i) for i, b in enumerate(buttons) if b.value() == 0)
    hid_gamepad.gamepad.send_gamepad(s, btn_bits)
    time.sleep_ms(16)
