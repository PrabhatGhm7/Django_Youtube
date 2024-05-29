
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import video_upload_form
from django.contrib import messages
from .models import video_upload, comments , channel
from django import forms
from django.contrib.auth.decorators import login_required
from .forms import commentsform
from django.db.models import F , Q

@login_required
def upload(request):
    if request.method == 'POST':
        videoform = video_upload_form(request.POST, request.FILES)
        if videoform.is_valid():
            videoform.save()
            messages.success(request, "Uploaded successfully")  
            return redirect('upload_video') 
        else:
            messages.error(request, "Error")  

    # Initializing new form
    videoform = video_upload_form()
    videos = video_upload.objects.all()
    return render(request=request, template_name='index.html', context={'videoform': videoform,'videos':videos})

def home(request):
    videos = video_upload.objects.all()  
    return render(request, 'home.html', {'videos': videos } )


def search(request):
    srchtitle = request.POST.get('title')
    if request.method == 'POST' and srchtitle: #ie srchtitle is no empty
        searchvideo = video_upload.objects.filter(title__icontains=srchtitle)
        return render(request, 'home.html', {'videos': searchvideo, 'search_query': srchtitle})
    
    return render(request, 'home.html', {'videos': []})
            
            
def videoview(request, pk):
    
    video = video_upload.objects.get(pk=pk)
    
    session_key = f'viewes_video{pk}'
    if not request.session.get(session_key,False):
        video.views=F('views') + 1
        video.save()
        video.refresh_from_db()
        request.session[session_key] = True
    
    commentquery= comments.objects.filter(video=video)
    
    if request.method == 'POST':
        @login_required
        def post_comment(request):
            form = commentsform(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.video = video
                comment.save()
                return redirect(reverse('video', kwargs={'pk': video.pk}))
        return post_comment(request)
    
    form = commentsform()
        
    context = {
        'video': video,
        'comments': commentquery,
        'form': form,
    }
    
    return render(request, 'videoview.html', context)

@login_required
def userupload(request):
    videos = video_upload.objects.filter(Q(author=request.user))
    return render(request, 'userupload.html',{'videos':videos})
        
