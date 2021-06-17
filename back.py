import time
import picamera

# ----global declarations----
picam = picamera.PiCamera()


# ----functions section----

def aux(value):
       print('valor seleccionado:', value)


# for start the preview
def previsualize():
    picam.start_preview(fullscreen=False, window=(30,30,800,540))
    time.sleep(10)
    picam.stop_preview()
    picam.close()


#for stop the preview
def stop_previsualize():
    picam.stop_preview()


#for full-screen
def start_fullscreen():
    picamera.preview_fullscreen = True


#for start a video recording
def start_record(video_name):
    picamera.start_recording()

#for stop a video recording
def stop_record():
    picamera.stop_recording(1)


#for brightness
def change_brightness(value):
    previsualize()
    picam.brightness = value


#for contrast
def change_contrast(value):
    previsualize()
    picam.contrast = value


#for saturation
def change_saturation(value):
    previsualize()
    picam.saturation = value


#for sharpness
def change_sharpness(value):
    previsualize()
    picam.sharpness = value



#for shutter speed
"""
this function will take the speed
and apply a convertion to milliseconds
"""
def change_shutter_speed(value):
    m = 1000
    previsualize()
    picam.shutter_speed = value*m
    

# for change the resolution

# w:width; h:height


def change_resolution(d):  # d : dimension
    picam.resolution = (2592, d)   # ----square resolution----
    previsualize()


 # for change the ISO


def change_iso(iso):
    picam.ISO = iso
    previsualize()


#for image rotation
"""----no documentation----"""


def change_rotation():
    pass
