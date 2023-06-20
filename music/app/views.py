from django.shortcuts import render,redirect
from .models import *
from django.views import View

# Create your views here.
def index(request):
    data = Song.objects.all()
    return render(request,'index.html',{'data':data})

def artist(request,uid):
    singer = Song.objects.filter(id=uid)
    print(id)
    return render(request,'artist.html',{'singer':singer})

def base(request):
    return render(request,'base.html')

def song(request):
    return render(request,'song.html')

def upload(request):
    return render(request,'upload.html')

class song(View):
    def get(self,request,uid):
        data = Song.objects.get(id=uid)
        return render(request,'song.html',{'i':data})


def add_song(request):
    if request.method == 'POST':
        name = request.POST['name']
        singer = request.POST['singer']
        pic = request.FILES['pic']
        audio = request.FILES['audio']
        Song.objects.create(song_name=name,singer_name=singer,song_image=pic,song_audio=audio)
        return redirect('/')
    else:
        return render(request,'upload.html')
    
#     def upd(request):
#     if request.method == "POST":
#         hide = request.POST['hide']
#         name = request.POST['name']
#         subject_id = request.POST['subject']
#         subject = Subject.objects.get(id=subject_id)
#         address = request.POST['address']
#         mobile = request.POST['mobile']
#         image = request.FILES.get('image')
#         student = Student.objects.get(id=hide)
#        student.name = name
#         student.address = address
#         student.mobile = mobile
# student.subject = subject

#         if image:
#             student.image = image

#         student.save()

#         return redirect('/table/')