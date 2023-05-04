import json
import xml.etree.ElementTree as ET
from django.shortcuts import render
from django.http import HttpResponse
from .models import Keys, ForumTopic, Posts, Pays
from datetime import datetime, date, timedelta
from django.shortcuts import redirect
import django.http
import requests
import json
from django.contrib.auth.models import User
import base64
import hmac
import hashlib
from django.views.decorators.csrf import csrf_exempt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os, binascii
import secrets


def MainCSGO(request):
    return render(request, '../templates/csgo/main.html')


def Cobalt(request):
    return render(request, '../templates/csgo/cobalt.html')


def CobaltSuc(request):
    return render(request, '../templates/csgo/success.html')

def CobaltPayR30(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            try:
                user_email = User.objects.get(username=request.user.username).email
                pay = Pays(email=user_email, length=30)
                pay.save()

                url = "https://oplata.qiwi.com/create?publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPv7WmE6m9JsDkeLFCqcrGikz3z7eJ5AoBQnUvVTzsPNsYi7AqCa2DgRXY5vvPsZSVkTQZAbDFwLf4k8XdmdJuogWjXKx8GkQuEPuz5sYoR&" \
                    "&amount=99" \
                    "&billId=" + str(pay.id) + "" \
                    "&comment=" + str(pay.id) + "" \
                    "&successUrl=https%3A%2F%2Fmodernface.space%2Fcsgo%2Fcobalt%2Fpay%2Fsuccess" \
                    "&customFields%5BthemeCode%5D=Danyyl-EJa2htk5pl" \
                    "&email=" + str(user_email.replace("@", "%40"))

                context = {"url": url}

                return render(request, '../templates/csgo/pay.html', context)
            except:
                raise django.http.Http404
        else:
            return redirect('/accounts/login/')


def CobaltPayR90(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            try:
                user_email = User.objects.get(username=request.user.username).email
                pay = Pays(email=user_email, length=90)
                pay.save()

                url = "https://oplata.qiwi.com/create?publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPv7WmE6m9JsDkeLFCqcrGikz3z7eJ5AoBQnUvVTzsPNsYi7AqCa2DgRXY5vvPsZSVkTQZAbDFwLf4k8XdmdJuogWjXKx8GkQuEPuz5sYoR&" \
                    "&amount=249" \
                    "&billId=" + str(pay.id) + "" \
                    "&comment=" + str(pay.id) + "" \
                    "&successUrl=https%3A%2F%2Fmodernface.space%2Fcsgo%2Fcobalt%2Fpay%2Fsuccess" \
                    "&customFields%5BthemeCode%5D=Danyyl-EJa2htk5pl" \
                    "&email=" + str(user_email.replace("@", "%40"))

                context = {"url": url}

                return render(request, '../templates/csgo/pay.html', context)
            except:
                raise django.http.Http404
        else:
            return redirect('/accounts/login/')


@csrf_exempt
def PayHook(request):
    raise Exception

    if request.method == "POST":
        hook_data = json.loads(request.body.decode('utf-8'))

        webhook_key_base64 = 'sxh0H+e1TOMts2qh0HO6S4bnvs5u4cbuIl2Sep9vPns='
        webhook_key = base64.b64decode(bytes(webhook_key_base64, 'utf-8'))
        data = str(hook_data["payment"]["sum"]["currency"]) + "|" + str(hook_data["payment"]["sum"]["amount"]) + "|" + str(hook_data["payment"]["type"]) + "|" + str(hook_data["payment"]["account"]) + "|" + str(hook_data["payment"]["txnId"])

        if hmac.new(webhook_key, data.encode('utf-8'), hashlib.sha256).hexdigest() == hook_data["hash"]:
            email = Pays.objects.get(id=hook_data["payment"]["comment"]).email
            length = Pays.objects.get(id=hook_data["payment"]["comment"]).length

            print(email)

            key_number = str(secrets.token_hex(2)) + "-" + str(secrets.token_hex(2)) + "-" + str(secrets.token_hex(2)) + "-" + str(secrets.token_hex(2))
            new_key = Keys(username=User.objects.get(email__exact=email).username, key=key_number, number_of_months=int(length))
            new_key.save()

            print(new_key.key)

            fromaddr = ""
            toaddr = email
            mypass = ""

            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "COBALT"

            body = "Thank you! Your key: " + key_number + ". Download link: https://modernface.space/downloads/cobalt_updater.exe"
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.outlook.com')
            server.starttls()
            server.login(fromaddr, mypass)
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

            return redirect('/')
        else:
            raise django.http.Http404
    else:
        raise django.http.Http404



def CheckKey(request):
    if request.method == "GET":
        key = str(request.GET['key'])
        username = str(request.GET['username'])
        try:
            row = Keys.objects.get(key=key)

            correct_username = str(row.username)

            if username == correct_username:
                try:
                    request.GET['activate']
                    if row.activated == False:
                        start_date = date(row.start_date.year, row.start_date.month, row.start_date.day)
                        day_delta = (date.today() - start_date).days

                        print(day_delta)

                        if day_delta <= int(row.number_of_months):
                            row.activated = True
                            row.save()
                            return HttpResponse('true')
                        else:
                            return HttpResponse('false')
                    else:
                        return HttpResponse('false')
                except:
                    start_date = date(row.start_date.year, row.start_date.month, row.start_date.day)
                    day_delta = (date.today() - start_date).days

                    print(day_delta)

                    if day_delta <= int(row.number_of_months):
                        return HttpResponse('true')
                    else:
                        return HttpResponse('false')
            else:
                return HttpResponse('false')
        except:
            return HttpResponse('false')


def ForumMain(request):
    if request.method == "GET":
        context = {"popular_topics": [], "last_topics": []}

        counter = 0
        for i in ForumTopic.objects.order_by('-views'):
            if len(i.description) <= 200:
                context['popular_topics'].append({"id": i.id, "name": i.name, "description": i.description, "views": str(i.views), "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[:4], "number_of_posts": str(i.number_of_posts)})
            else:
                context['popular_topics'].append({"id": i.id, "name": i.name, "description": i.description[:201] + '...', "views": str(i.views), "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[:4], "number_of_posts": str(i.number_of_posts)})

            counter += 1
            if counter >= 5:
                break

        counter = 0
        for i in ForumTopic.objects.order_by('-id'):
            if len(i.description) <= 120:
                context['last_topics'].append({"id": i.id, "name": i.name, "description": i.description, "views": str(i.views),
                     "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[:4], "number_of_posts": str(i.number_of_posts)})
            else:
                context['last_topics'].append({"id": i.id, "name": i.name, "description": i.description[:201] + '...', "views": str(i.views),
                     "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[:4], "number_of_posts": str(i.number_of_posts)})

            counter += 1
            if counter >= 7:
                break

        counter = 0
        counter_id = 0
        themes_list = []
        for i in ForumTopic.objects.order_by('?'):
            try:
                while True:
                    item = ForumTopic.objects.order_by('?')[counter_id]
                    if item.subject not in themes_list:
                        themes_list.append(item.subject)
                        counter_id += 1
                        break
                    else:
                        counter_id += 1
            except IndexError:
                pass

            counter += 1
            if counter >= 7:
                break

        context['themes'] = themes_list

        return render(request, '../templates/csgo/forum/main_forum.html', context)
    elif request.method == "POST":
        text = request.POST.get("search_topic")

        return redirect('/csgo/forum/search_topic/?search=' + text)


def Topic(request):
    if request.method == "GET":
        try:
            topic_id = str(request.GET['topic_id'])
            topic_name = ForumTopic.objects.get(id=topic_id).name[:20]
            topic_name_full = ForumTopic.objects.get(id=topic_id).name
            topic_date = ForumTopic.objects.get(id=topic_id).creation_date
            topic_subject = ForumTopic.objects.get(id=topic_id).subject
            topic_description = ForumTopic.objects.get(id=topic_id).description
            topic_author = ForumTopic.objects.get(id=topic_id).author

            is_super_topic = ForumTopic.objects.get(id=topic_id).is_super_topic

            posts = Posts.objects.filter(topic_id=int(topic_id)).order_by("creation_datetime")
            numbers_of_posts = Posts.objects.filter(topic_id=topic_id).count()
            list_of_posts = []


            for i in posts:
                post = {}
                post["author"] = i.author
                post['datetime'] = i.creation_datetime
                post['text'] = i.text
                list_of_posts.append(post)


            context = {"topic_id": topic_id, "topic_name": topic_name, "topic_name_full": topic_name_full, "topic_date": topic_date, "topic_subject": topic_subject,
                       "topic_description": topic_description, "topic_author": topic_author, "posts": list_of_posts, "is_super_topic": is_super_topic}


            topic_state = ForumTopic.objects.get(id=topic_id)
            topic_state.views += 1
            topic_state.number_of_posts = numbers_of_posts
            topic_state.save()

            return render(request, '../templates/csgo/forum/topic.html', context)
        except:
            raise django.http.Http404


def NewPost(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            context = {}

            try:
                topic_id = str(request.GET['topic_id'])

                context["topic_id"] = topic_id
            except:
                raise django.http.Http404

            return render(request, '../templates/csgo/forum/new_post.html', context)
        elif request.method == "POST":
            try:
                topic_id = str(request.GET['topic_id'])

                text = request.POST.get("text")
                user = request.user.username

                new_post = Posts(topic_id=topic_id, author=user, text=text)
                new_post.save()

                topic = ForumTopic.objects.get(id=topic_id)
                topic.last_update = datetime.today().date()
                topic.save()

                return redirect('/csgo/forum/topic/?topic_id='+ topic_id)
            except:
                raise django.http.Http404
    else:
        return redirect('/accounts/login/')


def NewTopic(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            context = {}

            # try:
            #
            # except:
            #     raise django.http.Http404

            return render(request, '../templates/csgo/forum/new_topic.html', context)
        elif request.method == "POST":
            try:
                text = request.POST.get("text")
                name = request.POST.get("title")
                theme = request.POST.get("themes")
                user = request.user.username

                print(theme)

                new_topic = ForumTopic(author=user, description=text, name=name, subject=theme, views=1, last_update=datetime.today().date(), number_of_posts=0)
                new_topic.save()


                return redirect('/csgo/forum/')
            except:
                raise django.http.Http404
    else:
        return redirect('/accounts/login/')


def ThemesList(request):
    context = {}
    try:
        theme = str(request.GET['theme'])

        context = {"themes": [], "theme": theme}

        for i in ForumTopic.objects.filter(subject=theme):
            if len(i.description) <= 200:
                context['themes'].append(
                    {"id": i.id, "name": i.name, "description": i.description, "views": str(i.views),
                     "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[
                                                                                                    :4],
                     "number_of_posts": str(i.number_of_posts)})
            else:
                context['themes'].append(
                    {"id": i.id, "name": i.name, "description": i.description[:201] + '...', "views": str(i.views),
                     "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[
                                                                                                    :4],
                     "number_of_posts": str(i.number_of_posts)})

        return render(request, '../templates/csgo/forum/themes_list.html', context)
    except:
        raise django.http.Http404


def SearchTopic(request):
    text = request.GET.get("search")

    results = ForumTopic.objects.filter(name__contains=text)
    results_themes = ForumTopic.objects.filter(subject__contains=text)

    search = str(request.GET['search'])

    context = {"results": [], "results_themes": [], "search": search}

    for i in results:
        if len(i.description) <= 200:
            context['results'].append(
                {"id": i.id, "name": i.name, "description": i.description, "views": str(i.views),
                 "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[
                                                                                                :4],
                 "number_of_posts": str(i.number_of_posts)})
        else:
            context['results'].append(
                {"id": i.id, "name": i.name, "description": i.description[:201] + '...', "views": str(i.views),
                 "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[
                                                                                                :4],
                 "number_of_posts": str(i.number_of_posts)})

    for i in results_themes:
        if len(i.description) <= 200:
            context['results_themes'].append(
                {"id": i.id, "name": i.name, "description": i.description, "views": str(i.views),
                 "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[
                                                                                                :4],
                 "number_of_posts": str(i.number_of_posts)})
        else:
            context['results_themes'].append(
                {"id": i.id, "name": i.name, "description": i.description[:201] + '...', "views": str(i.views),
                 "last_update": str(i.last_update)[-2:] + "." + str(i.last_update)[5:7] + "." + str(i.last_update)[
                                                                                                :4],
                 "number_of_posts": str(i.number_of_posts)})

    return render(request, '../templates/csgo/forum/topic_search.html', context)
