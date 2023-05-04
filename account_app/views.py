from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from account_app.forms import CreateUserForm
from django.contrib import messages
import django.contrib.auth
import django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Profile
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import Http404, HttpResponseForbidden
from datetime import datetime
import os
from django.conf import settings
import shutil
from django.core.mail import send_mail
from .forms import AvatarForm
from django.core.files.images import ImageFile
import random
from .models import ResetPasswordModel, ForgetPasswordCode
from django.utils.datastructures import MultiValueDictKeyError


def copy_avatar_to_static():
    media_list = os.listdir(settings.MEDIA_ROOT + '/avatars/')
    static_list = os.listdir(settings.STATICFILES_DIRS[0] + '/img/avatars/')
    for i in media_list:
        if i not in static_list:
            # shutil.copy2(settings.MEDIA_ROOT + '/avatars/' + i, settings.STATICFILES_DIRS[0] + '/img/avatars/avatars_by_name/' + username + '.jpg')
            shutil.copy2(settings.MEDIA_ROOT + '/avatars/' + i, settings.STATICFILES_DIRS[0] + '/img/avatars/' + i)


def singupPage(request):
    form = CreateUserForm()

    user_list = []

    for i in User.objects.all():
        user_list.append(str(i))

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if 'chek_lis' in request.POST:
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                Profile.objects.create(user=User.objects.get(username=user))
                shutil.copy2(settings.STATICFILES_DIRS[0] + '/img/avatars/' + 'default_avatar.jpg', settings.STATICFILES_DIRS[0] + '/img/avatars/avatars_by_name/' + user + '.jpg')
                return redirect('MainPage')
        else:
            pass


    context = {'form': form, 'users': str(user_list)}
    return render(request, 'Accounts/singup.html', context)


def loginPage(request):
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            error = ''
            return redirect('MainPage')
        else:
            error = 'Email or password is wrong!'

    context = {'error': error}
    return render(request, 'Accounts/login.html', context)


def logout(request):
    django.contrib.auth.logout(request)
    return redirect('MainPage')


def UserProfile(request, user=''):
    try:
        user = request.user.get_username
        username = request.path.split('/')[3]


        profile_model = Profile.objects.get(user=User.objects.get(username=username))

        try:
            birthday_date = datetime.strptime(str(profile_model.age), '%Y-%m-%d')
            birhtday = datetime.strftime(birthday_date, '%d %B %Y')
        except ValueError:
            birhtday = 'unknown'

        try:
            avatar = '../../../static/img/avatars/' + str(profile_model.avatar).split('/')[1]
        except IndexError:
            avatar = None

        bio = 'unknown'

        if profile_model.bio != '':
            bio = profile_model.bio

        city = 'unknown'

        if profile_model.city != '':
            city = profile_model.city

        gender = 'unknown'

        if profile_model.gender != '':
            gender = profile_model.gender

        context = {'username': profile_model.user.username, 'first_name': profile_model.user.first_name, 'last_name': profile_model.user.last_name,
                   'email': profile_model.user.email, 'phone': profile_model.phone, 'age': birhtday, 'gender': gender,
                   'bio': bio, 'city': city, 'avatar': avatar}

        return render(request, 'Accounts/profile/user_profile.html', context)
    except ObjectDoesNotExist:
        raise Http404


def EditProfile(request, user=''):
    try:
        user_from_url = User.objects.get(username=request.path.split('/')[3])
        user = request.user
        if user == user_from_url:
            profile_model = Profile.objects.get(user=user)

            avatar = '../../../../static/img/avatars/' + str(profile_model.avatar).split('/')[1]

            city = ''

            avatar_field = profile_model.avatar

            if profile_model.city != 'unknown':
                city = profile_model.city

            context = {'username': profile_model.user.username, 'first_name': profile_model.user.first_name, 'last_name': profile_model.user.last_name,
                       'email': profile_model.user.email, 'phone': profile_model.phone, 'age': profile_model.age, 'gender': profile_model.gender,
                       'bio': profile_model.bio, 'city': city, 'avatar': avatar}

            error_status = False

            if request.method == 'POST':
                new_username = request.POST.get('username')
                new_email = request.POST.get('email')
                new_first_name = request.POST.get('first_name')
                new_last_name = request.POST.get('last_name')
                new_bio = request.POST.get('bio')
                new_phone = request.POST.get('phone')
                new_age = request.POST.get('age')
                new_gender = request.POST.get('gender')
                new_city = request.POST.get('city')


                if new_phone != '':
                    if new_phone[0] != '+':
                        messages.add_message(request, messages.ERROR, 'Please set correct phone number! Example: +12223334455.')
                        error_status = True
                else:
                    new_phone = ''

                old_username = request.user.username

                request.user.username = new_username
                request.user.email = new_email
                request.user.first_name = new_first_name
                request.user.last_name = new_last_name
                if not (str(request.FILES)[-1] == '>' and str(request.FILES)[-2] == '}' and str(request.FILES)[-3] == '{'):
                    if ImageFile(request.FILES['avatar']).width == ImageFile(request.FILES['avatar']).height:
                        profile_model.avatar = request.FILES['avatar']
                    else:
                        error_status = True
                        messages.add_message(request, messages.ERROR, 'Your avatar should be 1:1!')

                try:
                    if error_status != True:
                        request.user.save()
                        profile_model.phone = new_phone
                        profile_model.bio = new_bio
                        profile_model.gender = new_gender
                        profile_model.age = new_age
                        profile_model.city = new_city

                        profile_model.save()

                        copy_avatar_to_static()

                        avatar_name = str(Profile.objects.get(user=request.user).avatar)
                        avatar_name_clear = os.path.splitext(os.path.basename(avatar_name))[0]
                        shutil.copy2(settings.STATICFILES_DIRS[0] + '/img/' + avatar_name, settings.STATICFILES_DIRS[0] + '/img/avatars/avatars_by_name/' + new_username + '.jpg')
                        return redirect('/accounts/profile/' + new_username)
                    else:
                        return redirect('/accounts/profile/' + request.user.username + '/edit/')


                except IntegrityError:
                    try:
                        request.user.username = new_username
                        request.user.save()
                        return redirect('/accounts/profile/' + new_username)
                    except IntegrityError:
                        messages.add_message(request, messages.ERROR, 'This username already in use!')
                        error_status = True
                        request.user.username = old_username
                        request.user.save()
                        return redirect('/accounts/profile/' + request.user.username + '/edit/')

            return render(request, 'Accounts/profile/edit_profile.html', context)
        else:
            return HttpResponseForbidden()
    except ObjectDoesNotExist:
        raise Http404


def ResetPasswordSend(request):
    if request.user.is_authenticated:
        try:
            ResetPasswordModel.objects.create(user=request.user)
        except IntegrityError:
            pass

        code_send = ResetPasswordModel.objects.get(user=request.user)
        code_send.code_send = True
        code_send.code_checked = False
        code_send.save()

        code = random.randint(1000, 9999)

        code_model = ResetPasswordModel.objects.get(user=request.user)
        code_model.code = code
        code_model.save()

        print(code)

        ResetPasswordMod = ResetPasswordModel.objects.get(user=request.user)
        ResetPasswordMod.limit = 0
        ResetPasswordMod.save()

        send_mail(
            'Verification code',
            'Your code is ' + str(code) + ", please don't tell it to anyone!",
            ' ',
            [User.objects.get(username=request.GET['username']).email],
            fail_silently=False,
        )

        return redirect('/accounts/reset_password/')
    else:
        return HttpResponseForbidden()


def ForgetPasswordSend(request):
    try:
        User.objects.get(username=request.GET['username'])
        try:
            ResetPasswordModel.objects.create(user=User.objects.get(username=request.GET['username']))
        except IntegrityError:
            pass

        code_send = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))
        code_send.code_send = True
        code_send.code_checked = False
        code_send.save()

        code = random.randint(1000, 9999)

        code_model = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))
        code_model.code = code
        code_model.save()

        print(code)

        ResetPasswordMod = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))
        ResetPasswordMod.limit = 0
        ResetPasswordMod.save()

        send_mail(
            'Verification code',
            'Your code is ' + str(code) + ", please don't tell it to anyone!",
            '',
            [User.objects.get(username=request.GET['username']).email],
            fail_silently=False,
        )

        return redirect('/accounts/forget_password/?username=' + request.GET['username'])
    except ObjectDoesNotExist:
        return redirect('/accounts/forget_password/?username=' + request.GET['username'])


def ForgetPassword(request):
    message = ''
    email = ''
    error = ''
    try:
        User.objects.get(username=request.GET['username'])
        code_send = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))
        if code_send.code_send == True:
            user = User.objects.get(username=request.GET['username']).username
            message = "Verification code was sent to"
            email = User.objects.get(username=request.GET['username']).email

            code_send = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))

            error = ''
            if request.method == 'POST':
                try:
                    if ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username'])).limit < 3:
                        if int(request.POST.get('codeInput')) == int(ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username'])).code):
                            ResetPasswordMod = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))
                            ResetPasswordMod.code_checked = True
                            ResetPasswordMod.code_send = False
                            ResetPasswordMod.save()

                            code = ''
                            code_list = ['0', '1' , '2' , '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

                            for i in range(32):
                                code += random.choice(code_list)

                            try:
                                ForgetPasswordCode.objects.create(user=User.objects.get(username=request.GET['username']))
                            except IntegrityError:
                                pass

                            CodeModel = ForgetPasswordCode.objects.get(user=User.objects.get(username=request.GET['username']))
                            CodeModel.code = code
                            CodeModel.save()

                            return redirect('/accounts/new_password_forget/?username=' + request.GET['username'] + '&code=' + code + '&dont_copy_code=please')
                        else:
                            error = 'Code is wrong, please try again!'
                            ResetPasswordMod = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))
                            ResetPasswordMod.limit += 1
                            ResetPasswordMod.save()
                    else:
                        error = 'Сode limit exceeded!'
                except ValueError:
                    error = 'Code is wrong, please try again!'
                    ResetPasswordMod = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))
                    ResetPasswordMod.limit += 1
                    ResetPasswordMod.save()
        else:
            return HttpResponseForbidden()

    except ObjectDoesNotExist:
        message = "This username doesn't exist!"

    context = {'message': message, 'email': email, 'error': error}

    return render(request, 'Accounts/profile/forget_password.html', context)


def ResetPassword(request):
    if request.user.is_authenticated:
        code_send = ResetPasswordModel.objects.get(user=request.user)
        if code_send.code_send == True:
            user = request.user
            error = ''
            if request.method == 'POST':
                if ResetPasswordModel.objects.get(user=request.user).limit < 3:
                    try:
                        if int(request.POST.get('codeInput')) == int(ResetPasswordModel.objects.get(user=request.user).code):
                            ResetPasswordMod = ResetPasswordModel.objects.get(user=request.user)
                            ResetPasswordMod.code_checked = True
                            ResetPasswordMod.code_send = False
                            ResetPasswordMod.save()

                            return redirect('/accounts/new_password/')
                        else:
                            error = 'Code is wrong, please try again!'
                            ResetPasswordMod = ResetPasswordModel.objects.get(user=request.user)
                            ResetPasswordMod.limit += 1
                            ResetPasswordMod.save()
                    except ValueError:
                        error = 'Code is wrong, please try again!'
                        ResetPasswordMod = ResetPasswordModel.objects.get(user=request.user)
                        ResetPasswordMod.limit += 1
                        ResetPasswordMod.save()
                else:
                    error = 'Сode limit exceeded!'

            context = {'email': user.email, 'error': error}
            return render(request, 'Accounts/profile/reset_password.html', context)
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseForbidden()


def NewPassword(request):
    if request.user.is_authenticated:
        code_send = ResetPasswordModel.objects.get(user=request.user)
        if code_send.code_checked == True:
            user = request.user
            if request.method == 'POST':
                ResetPasswordMod = ResetPasswordModel.objects.get(user=request.user)
                ResetPasswordMod.code_checked = False
                ResetPasswordMod.save()

                passwrod = User.objects.get(username=request.user)
                passwrod.set_password(request.POST.get('new_password'))
                passwrod.save()

                user = authenticate(request, username=request.user, password=request.POST.get('new_password'))
                login(request, user)

                return redirect('../profile/' + str(request.user))
            else:
                context = {'email': user.email}
                return render(request, 'Accounts/profile/new_password.html', context)
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseForbidden()

def NewPasswordAfterForget(request):
        try:
            code = ForgetPasswordCode.objects.get(user=User.objects.get(username=request.GET['username']))
            if code.code == request.GET['code']:
                code_send = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))
                if code_send.code_checked == True:
                    user = request.user
                    if request.method == 'POST':
                        ResetPasswordMod = ResetPasswordModel.objects.get(user=User.objects.get(username=request.GET['username']))
                        ResetPasswordMod.code_checked = False
                        ResetPasswordMod.save()

                        passwrod = User.objects.get(username=request.GET['username'])
                        passwrod.set_password(request.POST.get('new_password'))
                        passwrod.save()

                        user = authenticate(request, username=request.GET['username'], password=request.POST.get('new_password'))
                        login(request, user)

                        return redirect('../profile/' + str(User.objects.get(username=request.GET['username'])))
                    else:
                        context = {'email': User.objects.get(username=request.GET['username']).email}
                        return render(request, 'Accounts/profile/new_password_forget.html', context)
                else:
                    return HttpResponseForbidden()
            else:
                return HttpResponseForbidden()
        except MultiValueDictKeyError:
            return HttpResponseForbidden()
