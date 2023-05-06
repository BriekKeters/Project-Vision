from imageai.Detection import VideoObjectDetection
import cv2

camera = cv2.VideoCapture(0)
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("yolov3.pt")
detector.loadModel()

def forFrame(frame_number, output_array, output_count,returned_frame):
    cv2.imshow('webcam',returned_frame)
    for object in output_array:    
        print("Output for each object : ", object['name'])
    if cv2.waitKey(1) == 27:
            try:
                raise Exception
            except Exception:
                raise

def detect():
    try: detector.detectObjectsFromVideo(camera_input=camera,
                                    frames_per_second=30, 
                                    log_progress=True,
                                    save_detected_video=False,
                                    per_frame_function=forFrame,
                                    minimum_percentage_probability=30, 
                                    return_detected_frame=True)
    except: print("close")
        

def __main__():
    while True:
        detect()
        if input("close program: y/n? \n") == 'y':
            break

__main__()
cv2.destroyAllWindows()
