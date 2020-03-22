from django.shortcuts import render
from .models import Post, Contact


def hello_blog(request):
    data_list = ['Django', 'Python', 'Nginx',
                 'Git', 'HTML', 'Linux', 'MongoDB']

    post_list = Post.objects.filter(delete=False)

    data = {'name': 'Django3 Crash Course',
            'tech_list': data_list, 'posts': post_list}

    return render(request, 'index.html', data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})


def save_form(request):
    Contact.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        message=request.POST['message']
    )
    return render(request, 'form_received.html')
