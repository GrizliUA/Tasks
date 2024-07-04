from django.shortcuts import redirect
from django.http import HttpRequest
from .models import Click
from django.utils import timezone
from django.shortcuts import render
from rest_framework import generics
from .serializers import ClickSerializer
from .permissions import IsAdminOrReadOnly

def track_click(request: HttpRequest, project: str = None):
    ip_address = request.META.get('REMOTE_ADDR')
    browser_info = request.META.get('HTTP_USER_AGENT', 'unknown')
    thanks_page = request.GET.get('thanks', '/thanks')
    current_time = timezone.localtime()

    Click.objects.create(
        ip_address=ip_address,
        browser_info=browser_info,
        timestamp=current_time,
        project=project,
        thank_you_page=thanks_page
    )

    return redirect(thanks_page)

def thanks(request):
    return render(request, 'thanks.html')

def clicks(request):
    queryset = Click.objects.all()
    return render(request, 'clicks.html', {'clicks': queryset})

class ClickAPIList(generics.ListCreateAPIView):
    queryset = Click.objects.all()
    serializer_class = ClickSerializer
    permission_classes = (IsAdminOrReadOnly,)  # Custom permission: Admin can modify, others can read

def main_page(request):
    return render(request, 'main.html')
