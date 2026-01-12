import evdev
import numpy as np
import RPi.GPIO as GPIO
import time

# --- GPIO setup ---
GPIO.setmode(GPIO.BOARD)

# Servo setup (steering)
GPIO.setup(11, GPIO.OUT)
servo = GPIO.PWM(11, 50)  # 50 Hz
servo.start(0)

# DC motor setup (differential)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
pinOneMotor_PWM = GPIO.PWM(29, 10000)  # 10 kHz
pinTwoMotor_PWM = GPIO.PWM(31, 10000)
pinOneMotor_PWM.start(0)
pinTwoMotor_PWM.start(0)

# --- Helper function ---
def map_value(value, in_min, in_max, out_min, out_max):
    return np.interp(value, [in_min, in_max], [out_min, out_max])

# Motor control functions
def forward(speed):
    GPIO.output(31, False)
    pinOneMotor_PWM.ChangeDutyCycle(speed)

def backward(speed):
    GPIO.output(29, False)
    pinTwoMotor_PWM.ChangeDutyCycle(speed)

# --- Controller setup ---
device = evdev.InputDevice("/dev/input/event2")  # replace with your actual device

try:
    for event in device.read_loop():
        if event.type == evdev.ecodes.EV_ABS:
            # Steering (left stick X-axis)
            if event.code == evdev.ecodes.ABS_X:
                angle = round(map_value(event.value, 0, 65535, 2, 12))
                servo.ChangeDutyCycle(angle)
                print(f"Steering angle: {angle}")

            # Right Trigger - Forward
            elif event.code == evdev.ecodes.ABS_GAS:
                speed = round(map_value(event.value, 0, 1023, 0, 100))
                forward(speed)
                print(f"Forward speed: {speed}%")

            # Left Trigger - Backward
            elif event.code == evdev.ecodes.ABS_BRAKE:
                speed = round(map_value(event.value, 0, 1023, 0, 100))
                backward(speed)
                print(f"Backward speed: {speed}%")

except KeyboardInterrupt:
    pass
finally:
    # Stop PWM and cleanup GPIO
    servo.stop()
    pinOneMotor_PWM.stop()
    pinTwoMotor_PWM.stop()
    GPIO.cleanup()
