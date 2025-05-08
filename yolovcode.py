from imageai.Detection import ObjectDetection
def kim(resim):
    detector = ObjectDetection()
    model_path = "yolov3.pt"
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()
    detections = detector.detectObjectsFromImage(
            input_image=resim, 
            output_image_path="output_image.jpg", 
            minimum_percentage_probability=30)
    return detections

if __name__ == "__main__":
        print(kim("images\thumbs_b_c_8907b940332b061c7f507e57bea87ad6.jpg"))

def x(c):
        a = {}
        for b in c:
                if b["name"]