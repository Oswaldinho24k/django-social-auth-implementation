from django.urls import path, include
from .views import ResitrationView, MyProfile, EditProfile, NewLogroView
from django.contrib.auth import views as logViews

app_name="accounts"
urlpatterns = [
	path('register/', ResitrationView.as_view(), name="registro"),
	path('profile/', MyProfile.as_view(), name='profile'),
	path('login/', logViews.login, name="login"),
	path('logout/', logViews.logout, name="logout"),
	path('edit/', EditProfile.as_view(), name='edit'),
	path('logros/', NewLogroView.as_view(), name="new_logro")

]