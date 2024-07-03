from django.urls import path
from .views import track_click, thanks, ClickAPIList, clicks

urlpatterns = [
    path('track/', track_click, name='track_click'),
    path('click/<str:project>/', track_click, name='track_click_project'),
    path('thanks/', thanks, name='thanks'),
    path('clicks/', clicks, name='clicks')
    # path('clicks/', ClickAPIList.as_view())
]