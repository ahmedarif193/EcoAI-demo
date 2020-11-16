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
        class_name=id_class_name(class_id,classNames)
#        print(str(str(class_id) + " " + str(detection[2])  + " " + class_name))
        if class_id == 1.0 :
            X = X + 1
        if class_id == 17.0 :
            Y = Y + 1
        if class_id == 18.0 :
            Z = Z + 1
        box_x = detection[3] * image_width
        box_y = detection[4] * image_height
        box_width = detection[5] * image_width
        box_height = detection[6] * image_height
        cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
        cv2.putText(image,class_name ,(int(box_x), int(box_y+.05*image_height)),cv2.FONT_HERSHEY_SIMPLEX,(2),(0, 0, 255))
        #X == N



# cv2.imwrite("image_box_text.jpg",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
print ("There are", X, "Cigarette butts")
#print("There are", Y , "9touta")
#print("There are", Z ,"klab")
