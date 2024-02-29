from django.urls import include, path
from todos import views  # Импорт views из приложения todos

urlpatterns = [
    path('todos/', include('todos.urls')),
    # Другие пути...
]
from . import views

urlpatterns = [
    path('create/', views.create_todolist, name='create_todolist'),
    # other paths...
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # other paths...
]