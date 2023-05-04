from django.shortcuts import render
from news_app.models import Post
import logging

def News(request):
    all_list = Post.objects.all()
    main_dict = {}
    for i in all_list:
        TrueDay = i.created_on.strftime("%d")
        TrueMounth = i.created_on.strftime("%B")
        TrueYear = i.created_on.strftime("%Y")
        main_dict.update({i.title: {'title': i.title, 'author': i.author, 'content': i.content, 'day': TrueDay, 'mounth': TrueMounth, 'year': TrueYear}})
    context = {'data': main_dict}
    return render(request, 'News/news.html', context)

