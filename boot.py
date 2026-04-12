import sys

try:
    import hid_gamepad
    hid_gamepad.gamepad = hid_gamepad.init()
except Exception as e:
    with open('boot_error.log', 'w') as f:
        sys.print_exception(e, f)
