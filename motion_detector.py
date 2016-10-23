import RPi.GPIO as GPIO
class MotionDetector:

    motion_detection_callbacks = []
    pin = 17

    def __init__(self):	


        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.pin, GPIO.RISING, callback=self.on_state_changed, bouncetime=300)

    def on_state_changed(self, channel):

        value = GPIO.input(self.pin)

        for callback in self.motion_detection_callbacks:
                callback()

    def subcribe_to_detection(self, callback):
        self.motion_detection_callbacks.append(callback)

    def unsubcribe_from_detection(self, callback):
        self.motion_detection_callbacks.remove(callback)

    def dispose(self):
         GPIO.remove_event_detect(PinConfig.MotionDetectorInterruptPin)

