from django.shortcuts import render

def hello_blog(request):
    data_list = ['Django', 'Python', 'Nginx', 'Git', 'HTML', 'Linux', 'MongoDB']
    data = {'name': 'Django3 Crash Course', 'tech_list': data_list}
    return render(request, 'index.html', data)
