 import numpy as np
import cv2
import cv2.aruco as aruco

#cap = cv2.VideoCapture(0)

def arucoFunc(image):
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_1000)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(
        image, aruco_dict, parameters=parameters)
    if isinstance(ids, np.ndarray):
        if ids[0,0]==0:
            return 0
        if ids[0,0]==1:
            return 1

    


# import numpy as np
# import cv2
# import cv2.aruco as aruco

# cap = cv2.VideoCapture(0)

# while True:
#     _, image = cap.read()
    

#     aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
#     parameters = aruco.DetectorParameters_create()
#     corners, ids, rejectedImgPoints = aruco.detectMarkers(
#         image, aruco_dict, parameters=parameters)
#     if isinstance(ids, np.ndarray ):
#         if ids[0,0]==0:
#             print("left")
#         if ids[0,0]==1:
#             print("right")
#     aruco.drawDetectedMarkers(image, corners, ids)
#     aruco.drawDetectedMarkers(image, rejectedImgPoints, borderColor=(100, 0, 240))

#     cv2.imshow('so52814747', image)
#     key = cv2.waitKey(1)
#     if key == 27:
#         cv2.destroyAllWindows()
#         break

    


