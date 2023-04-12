from django.shortcuts import render,redirect
from . import models

def main_page(request):
    region = models.Region.objects.all().order_by('name')
    categorys = models.Categoriya.objects.all()
    lastes_news = models.News.objects.filter(is_active = True)[:6]
    resent_post = models.News.objects.filter(is_active = False).order_by("-id")[:3]

    cats = {}

    for cat in models.Categoriya.objects.all():
        nq = models.News.objects.filter(category=cat,).count()
        cats[cat.name]=nq
    print(cats)

    context = {
        "region":region,
        "category":categorys,
        "lastes":lastes_news,
        "resent_posts":resent_post,
        "cat_count": cats
    }
    return render(request, "main/index-inner.html", context)

def category_detail(request, id):
    category = models.Categoriya.objects.filter(id=id)
    news = models.News.objects.filter(category=category)
    
    cats = {}

    for cat in models.Categoriya.objects.all():
        nq = models.News.objects.filter(category=cat,).count()
        cats[cat.name]=nq

    context = {
        'category':category,
        'news':news,
        'cat_count':cats
    }

    return render(request, 'main/category.html', context)


def news_detail(request, id):
    news = models.News.objects.get(id=id)
    photos = models.NewsImage.objects.filter(news=news)
    region = models.Region.objects.all().order_by('name')
    categorys = models.Categoriya.objects.all()
    coments = models.CommentNews.objects.filter(news=news)
    status = models.StatuxNews.objects.filter(news=news)
    resent_post = models.News.objects.filter(is_active = False).order_by("-id")[:3]
    like = 0
    dis_like =0
    for status in status:
        if status.like:
            like += 1
        else:
            dis_like += 1

    try:
        t = models.StatuxNews.objects.get(
            news=news,
            author=request.user
        )
        if t.like :
            status = 1
        else:
            status = 2
    except:
        status = 3

    context = {
        'news':news,
        'photos':photos,
        'coments':coments,
        'like':like,
        'dis_like':dis_like,
        'category':categorys,
        'region':region,
        'resent_posts':resent_post,
        'status':status
    }
    return render(request, 'main/news-detail.html', context)


def create_coment(request):
    news_id =request.POST['news_id']
    body = request.POST['body']
    news = models.News.objects.get(id=news_id)
    user = request.user
    models.CommentNews.objects.create(
        news =news,
        body=body,
        author = user
    )
    return redirect('news_detail', int(news_id))

def create_status(request):
    news_id = request.POST['news_id']
    user = request.user
    status_f = int(request.POST['status'])
    news = models.News.objects.get(id=news_id)
    data, created = models.StatuxNews.objects.get_or_create(
        news=news,
        author = user,
    )
    if created :
        if status_f == 1:
            data.like = True
        else: 
            data.dis_like = True
    else:
        if data.like:
            if status_f == 2:
                data.like = False
                data.dis_like = True
        else:
            if  status_f == 1:
                data.like = True
                data.dis_like = False
    data.save()
    return redirect('news_detail', int(news_id))