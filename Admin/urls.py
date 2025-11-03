from django.urls import path,include
from Admin import views
app_name="Admin"
urlpatterns = [
    path('admin/',views.admin,name="admin"),
]