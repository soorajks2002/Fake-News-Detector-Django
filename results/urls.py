from django.urls import path, include
from results import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('show', views.show, name='show')
]
