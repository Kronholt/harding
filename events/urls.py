from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('volunteering/', views.volunteering, name="volunteering"),
    path('event/<str:pk>/', views.event,name='event'),
    path('stories/', views.stories, name="stories"),
    path('story/<str:pk>/', views.story, name="story"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name='login'),
    path('attend/<str:pk>/', views.attend, name="attend"),
]