from . import views

urlpatterns = [
    url(r'^availability/$', views.availability, name='availability'),
]