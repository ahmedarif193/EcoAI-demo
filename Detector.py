#! /usr/bin/env python3
import cv2

# Pretrained classes in the model
classNames = {1: 'CB'}


def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value


# Loading model
model = cv2.dnn.readNetFromTensorflow('model_TF/frozen_inference_graph.pb',
                                      'model_TF/5OCVgraph.pbtxt')
image = cv2.imread('test_images/Megots_cigarettes.jpg')

image_height, image_width, _ = image.shape

model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
output = model.forward()
# print(output[0,0,:,:].shape)
X = 0
#Y = 0
#Z = 0

for detection in output[0, 0, :, :]:
    confidence = detection[2]
    if confidence > .3:
        class_id = detection[1]
        if class_id == 1.0 :
            X = X + 1

print ("There are", X, "Cigarette butts")
