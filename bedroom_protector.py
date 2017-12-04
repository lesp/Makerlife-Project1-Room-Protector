import picamera
from gpiozero import MotionSensor, Buzzer
from datetime import datetime

pir = MotionSensor(17)
camera = picamera.PiCamera()
alarm = Buzzer(27)

stream = picamera.PiCameraCircularIO(camera, seconds=20)
camera.start_recording(stream, format='h264')
try:
    while True:
        camera.wait_recording(1)
        if pir.motion_detected == True:
            print("RECORDING")
            alarm.on()
            camera.wait_recording(10)
            stream.copy_to(str((datetime.now()))+'.h264')
            alarm.off()
finally:
    camera.stop_recording()
    print("Recording Stopped")
