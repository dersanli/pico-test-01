from machine import ADC, Pin
import time

# Steering wheel potentiometer on GP26 (ADC0)
pot = ADC(Pin(26))

# Engine on/off switch on GP16, internal pull-up
# Switch connects GP16 to GND when on → reads LOW when on
engine_switch = Pin(16, Pin.IN, Pin.PULL_UP)

def read_steering():
    """Return pot value mapped to -32767..32767 for HID axis."""
    raw = pot.read_u16()  # 0..65535
    return raw - 32768

def engine_on():
    """Return True when engine switch is on (pin pulled LOW)."""
    return engine_switch.value() == 0

if __name__ == "__main__":
    while True:
        steering = read_steering()
        engine = engine_on()
        print(f"Steering: {steering:6d} | Engine: {'ON' if engine else 'OFF'}")
        time.sleep_ms(50)
