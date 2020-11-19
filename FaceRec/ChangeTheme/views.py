from django.shortcuts import render
from .modules.facecv import FaceCV,get_args

def index(request):
    #Face Recognition
    args = get_args()
    depth = args.depth
    width = args.width

    face = FaceCV(depth=depth, width=width)

    predicted_ages,predicted_genders=face.detect_face()
    


    context={
        'age':predicted_ages,
        'gender':predicted_genders,
    }

    return render(request,"home.html",context)