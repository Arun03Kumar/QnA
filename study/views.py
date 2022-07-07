from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from .models import *
import random


def index(request):
    data = Questions.objects.all()
    usr_data = Signup.objects.all()
    lst = []
    cnt = 1
    for i in data:
        if i.que is not None and i.que != "" and cnt <= 5:
            lst.append([i, str(i.id)])
        cnt += 1
    for i in range(len(lst)-1):
        random_index = random.randint(0, len(lst)-1)
        temp = lst.pop(random_index)
        lst.append(temp)
    print(len(lst))
    d = {'data': data, 'lst': lst, 'usr_data': usr_data}
    return render(request, 'index.html', d)


def login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = auth.authenticate(username=u, password=p)
        try:
            if user.is_staff:
                auth.login(request, user)
                error = "no"
            elif user is not None:
                auth.login(request, user)
                return redirect('user_home')
                error = "not"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'login.html', d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Questions.objects.all()
    usr_data = Signup.objects.all()
    lst = []
    for i in data:
        if i.que is not None and i.que != "":
            lst.append([i, str(i.id)])
    d = {'data': data, 'lst': lst, 'usr_data': usr_data}
    return render(request, 'admin_home.html', d)


def logout(request):
    auth.logout(request)
    return redirect('/')


def questions(request):
    data = Questions.objects.all()
    d = {'data': data}
    return render(request, 'questions.html', d)


def signup(request):
    error = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        e = request.POST['email']
        con = request.POST['contact']
        p = request.POST['pwd']
        gen = request.POST['gender']
        d = request.POST['dob']
        try:
            user = User.objects.create_user(
                first_name=f, last_name=l, username=e, password=p)
            Signup.objects.create(user=user, mobile=con, gender=gen,
                                  dob=d, follower=0, following=0, que_asked=0, answered=0)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'signup.html', d)


def user_home(request):
    data = Questions.objects.all()
    user = request.user
    # print(user.id)
    all_user_data = Signup.objects.all()
    user_data = Signup.objects.all().filter(user__exact=user.id)[0]
    # print(user_data)
    lst = []
    for i in data:
        if i.que is not None and i.que != "":
            lst.append([i, str(i.id)])
    # print(len(lst))
    for i in range(len(lst)-1):
        random_index = random.randint(0, len(lst)-1)
        temp = lst.pop(random_index)
        lst.append(temp)
    d = {'data': data, 'lst': lst, 'u_data': user_data, 'all_usr': all_user_data}
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'user_home.html', d)


def add_que_admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        t = request.POST['topic']
        q = request.POST['que']
        try:
            Questions.objects.create(que=q, topic=t)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_que_admin.html', d)


def add_que_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        t = request.POST['topic']
        q = request.POST['que']
        user = request.user
        user_name = user.first_name + " " + user.last_name
        print(user_name)
        try:
            Questions.objects.create(
                que=q, topic=t, user=user_name, user_id=user.id)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_que_user.html', d)


def view_que_admin(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Questions.objects.all()
    d = {'data': data}
    return render(request, 'view_que_admin.html', d)


def view_que_user(request):
    data = Questions.objects.all()
    hp = Helpful.objects.all()
    use_data = Signup.objects.all()
    ur = request.user
    lst = []
    for i in data:
        if i.que is not None and i.que != "":
            lst.append([i, str(i.id)])
    # for i in range(len(lst)-1):
    #     random_index = random.randint(0, len(lst)-1)
    #     temp = lst.pop(random_index)
    #     lst.append(temp)
    d = {'data': data, 'data2': hp, 'ur': ur, 'usr_data': use_data, 'lst': lst}
    return render(request, 'view_que_user.html', d)


def add_ans_user(request, pid):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Questions.objects.get(id=pid)
    user = request.user
    user_name = user.first_name + " " + user.last_name
    # print(user)
    if request.method == 'POST':
        a = request.POST['ans']
        t = request.POST['atopic']
        try:
            Questions.objects.create(
                ans=a, user=user_name, user_id=user.id, atopic=t, h=0, nh=0)
        except:
            pass
    d = {'data': data}
    return render(request, 'add_ans_user.html', d)


def view_user(request):
    if not request.user.is_authenticated:
        return redirect('login')
    data = Signup.objects.all()
    d = {'data': data}
    return render(request, 'view_user.html', d)


def delete_user(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    student = User.objects.get(id=id)
    student.delete()
    return redirect('view_user')


def delete_que(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    student = Questions.objects.get(id=id)
    student.delete()
    return redirect('admin_home')


def delete_ans(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    student = Questions.objects.get(id=id)
    student.delete()
    return redirect('admin_home')


def change_password(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'change_password.html', d)


def feedback(request):
    error = ""
    if request.method == 'POST':
        n = request.POST['fname']
        p = request.POST['fphone']
        e = request.POST['femail']
        c = request.POST['fcomment']
        try:
            Feedback.objects.create(
                feedback_name=n, feedback_contact=p, feedback_email=e, feedback_comment=c)
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'feedback.html', d)


def view_feedback(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Feedback.objects.all()
    d = {'data': data}
    return render(request, 'view_feedback.html', d)


def delete_feedback(request, id):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    feedback = Feedback.objects.get(id=id)
    feedback.delete()
    return redirect('view_feedback')


def helpful(request, id):
    que = Questions.objects.get(id=id)
    hp = Helpful.objects.all()

    for i in hp:
        n = i.num
        n1 = i.numid
        print(id)
        if n1 == id:
            try:
                i.numid = id
                i.num = n+1
                i.save()
                break
            except:
                pass
    else:
        Helpful.objects.create(numid=id, num=1)
        # break
    return redirect('view_que_user')

# def nothelpful(request):
#     num = 1


def write_blog(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    u_name = user.first_name + " " + user.last_name
    blog_obj = None
    if request.method == 'POST':
        t = request.POST['btopic']
        bc = request.POST['blog']
        try:
            blog_obj = Blog.objects.create(
                user_id=user.id, user_name=u_name, topic=t, blog_c=bc)
            return blog(request, blog_obj.id)
        except:
            pass
    # return blog(request, blog_obj.id)
    return render(request, 'write_blog.html')


def view_blogs(request):
    data = Blog.objects.all()
    usr_data = Signup.objects.all()
    data.reverse()
    d = {'data': data, 'usr_data': usr_data}
    return render(request, 'view_blogs.html', d)


def view_blog_admin(request):
    data = Blog.objects.all()
    usr_data = Signup.objects.all()
    data.reverse()
    d = {'data': data, 'usr_data': usr_data}
    return render(request, 'view_blog_admin.html', d)


def delete_blog(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('view_blog_admin')


def view_que_visitor(request):
    data = Questions.objects.all()
    hp = Helpful.objects.all()
    d = {'data': data, 'data2': hp}
    return render(request, 'view_que_visitor.html', d)


def add(request, id):
    all = Questions.objects.all()
    for i in all:
        if i.id == id:
            try:
                i.h = i.h+1
                i.save()
                break
            except:
                pass
    return redirect('view_que_user')


def add_on_admin(request, id):
    all = Questions.objects.all()
    for i in all:
        if i.id == id:
            try:
                i.h = i.h+1
                i.save()
                break
            except:
                pass
    return redirect('admin_home')


def addd(request, id):
    all = Questions.objects.all()
    for i in all:
        if i.id == id:
            try:
                i.nh = i.nh+1
                i.save()
                break
            except:
                pass
    return redirect('view_que_user')


def addd_on_admin(request, id):
    all = Questions.objects.all()
    for i in all:
        if i.id == id:
            try:
                i.nh = i.nh+1
                i.save()
                break
            except:
                pass
    return redirect('admin_home')


def follow_inc(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = request.user
    jiska_follow_inc_krna = Signup.objects.all().filter(user__exact=id)[0]
    jiska_following_inc_krna = Signup.objects.all().filter(
        user__exact=user.id)[0]
    # print(jiska_following_inc_krna.following)
    try:
        jiska_following_inc_krna.following = jiska_following_inc_krna.following + 1
        jiska_following_inc_krna.save()
        jiska_follow_inc_krna.follower = jiska_follow_inc_krna.follower + 1
        jiska_follow_inc_krna.save()
    except:
        pass
    return redirect('user_home')


def blog(request, id):
    blog = Blog.objects.all().filter(id__exact=id)[0]
    usr_data = Signup.objects.all().filter(user__exact=blog.user_id)[0]
    print(usr_data)
    return render(request, 'blog.html', {'blog_obj': blog, 'user_data': usr_data})
