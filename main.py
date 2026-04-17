import time
from machine import Pin, ADC

steering = ADC(Pin(28))
buttons = [Pin(p, Pin.IN, Pin.PULL_UP) for p in (16, 17, 18, 19)]

def read_steering(samples=8):
    raw = sum(steering.read_u16() for _ in range(samples)) // samples
    return raw - 32768

while True:
    btn_states = ' | '.join(f"K{i+1}: {'PRESSED' if b.value() == 0 else 'released'}" for i, b in enumerate(buttons))
    print(f"Steering: {read_steering():6d} | {btn_states}")
    time.sleep_ms(100)
