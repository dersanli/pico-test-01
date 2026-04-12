from machine import ADC, Pin

# Accelerator slide potentiometer on GP27 (ADC1)
pot = ADC(Pin(27))

def read_accelerator(samples=8):
    """Return averaged pot value mapped to -32767..32767 for HID axis."""
    raw = sum(pot.read_u16() for _ in range(samples)) // samples
    return 32767 - raw
