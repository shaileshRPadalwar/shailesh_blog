from django.urls import path
from blog import views

urlpatterns = [
    path('',views.post_list_view),
    path('tag/<slug:tag_slug>/',views.post_list_view,name='post_list_by_tag_name'),
    path('post/<slug:slug>/',views.post_detail,name='post_detail'),
    path('blog/',views.PostListView.as_view()),
    path('mail/<id>/',views.mail_send_view),
]