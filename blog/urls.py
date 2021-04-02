from django.urls import path
from blog import views

urlpatterns = [
    path('',views.post_list_view),
    path('post/<slug:slug>/',views.post_detail,name='post_detail'),
    path('blog/',views.PostListView.as_view()),
    path('mail/<id>/',views.mail_send_view),
]


