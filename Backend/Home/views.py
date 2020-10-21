from django.shortcuts import render
import cv2

# Create your views here.
def home(request):
    cap = cv2.VideoCapture(0)
    while True:
        ret,frame = cap.read()
        if ret:
            break
    cap.release()
    cv2.destroyAllWindows()
    
    return render(request,"home.html")