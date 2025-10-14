from django.shortcuts import render
from .models import NoticeBoarforUser

# Create your views here.
def listNoticesforuser(request):
     notices = NoticeBoarforUser.objects.filter(user_id = request.user.id).all()
        
     return render(request, 'noticeboard/noticeuser-list.html', {'notices': notices} )