
from django.contrib import admin
from django.urls import path
from study.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('login', login, name="login"),
    path('admin_home', admin_home, name="admin_home"),
    path('logout', logout, name="logout"),
    path('questions', questions, name="questions"),
    path('signup', signup, name="signup"),
    path('user_home', user_home, name="user_home"),
    path('add_que_admin', add_que_admin, name="add_que_admin"),
    path('add_que_user', add_que_user, name="add_que_user"),
    path('view_que_visitor', view_que_visitor, name="view_que_visitor"),
    path('view_que_admin', view_que_admin, name="view_que_admin"),
    path('view_que_user', view_que_user, name="view_que_user"),
    path('add_ans_user/<int:pid>', add_ans_user, name="add_ans_user"),
    path('view_user', view_user, name="view_user"),
    path('delete_user/<int:id>', delete_user, name="delete_user"),
    path('delete_que/<int:id>', delete_que, name="delete_que"),
    path('delete_ans/<int:id>', delete_ans, name="delete_ans"),
    path('change_password', change_password, name="change_password"),
    path('feedback', feedback, name="feedback"),
    path('view_feedback', view_feedback, name="view_feedback"),
    path('delete_feedback/<int:id>', delete_feedback, name="delete_feedback"),
    path('view_que_admin', view_que_admin, name="view_que_admin"),
    path('helpful/<int:id>', helpful, name="helpful"),
    path('add/<int:id>', add, name="add"),
    path('add_on_admin/<int:id>', add_on_admin, name="add_on_admin"),
    path('addd/<int:id>', addd, name="addd"),
    path('addd_on_admin/<int:id>', addd_on_admin, name="addd_on_admin"),
    path('write_blog', write_blog, name="write_blog"),
    path('view_blogs', view_blogs, name="view_blogs"),
    path('view_blog_admin', view_blog_admin, name="view_blog_admin"),
    path('delete_blog/<int:id>', delete_blog, name="delete_blog"),
    path('follow_inc/<int:id>', follow_inc, name="follow_inc"),
    path('blog/<int:id>', blog, name="blog"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
