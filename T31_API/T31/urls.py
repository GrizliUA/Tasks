from django.urls import path
from .views import track_click, thanks, clicks, main_page

urlpatterns = [
    path('track/', track_click, name='track_click'),
    path('click/<str:project>/', track_click, name='track_click_project'),
    path('thanks/', thanks, name='Thanks'),
    path('clicks/', clicks, name='clicks'),
    path('main/', main_page, name='Main')
]