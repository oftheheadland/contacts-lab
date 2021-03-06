from user import views as uv
from score import views as sv
from inventory import views as iv
from subscribe import views as sb
from django.urls import path

urlpatterns = [
    path('user/', uv.HomePageView().create_or_retrieve),
    path('user/<str:uname>/', uv.HomePageView().create_or_retrieve),

    path('score/', sv.HomePageView().create_or_retrieve),
    path('score/<int:userid>/', sv.HomePageView().create_or_retrieve),

    path('subscribe/', sb.HomePageView().create_or_retrieve),
    path('subscribe/<int:userid>/', sb.HomePageView().create_or_retrieve),

    path('inventory/', iv.HomePageView().create_or_retrieve),
    path('inventory/<str:objdescription>/', iv.HomePageView().create_or_retrieve),
]
