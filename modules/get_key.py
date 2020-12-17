from .facecv import FaceCV,get_args
from .fuzzy import findClosest
from keras import backend as K

def get_key():
    #Face Recognition
    args = get_args()
    depth = args.depth
    width = args.width
    face = FaceCV(depth=depth, width=width)

    #Predicting Age and Gender
    #K.clear_session()
    predicted_ages,predicted_genders=face.detect_face()

    #Calculating Session Key
    if predicted_genders>0.5:
        predicted_genders=1
    else:
        predicted_genders=0
    fuzzy=findClosest(predicted_genders*50+predicted_ages/4)
    K.clear_session()
    return fuzzy