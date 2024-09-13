from django.urls import re_path
from . import views


urlpatterns = [
      re_path('index/', views.index_view),   
      re_path('addmovie/', views.add_movie_view,name='addmovie'),   
      re_path('listmovies/', views.list_view),   

]

