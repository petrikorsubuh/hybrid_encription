from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from apps.hybrid_libs.aes_ok.main_aes import encrypt_AES_GCM
import subprocess
import shutil
from pathlib import Path
from .models import *
import os


class HomePage(LoginRequiredMixin, View):
    template_name = 'landing_page.html'
    login_url = '/login'

    def get(self, request):
        data = {'test': 'Hello'}
        return render(request, self.template_name, data)


class LoginView(View):
    template_name = 'auth/login.html'

    def get(self, request):
        form = LoginForm(request.POST)
        return render(request, self.template_name, {
            'fom_tittle': 'Login',
            'form': form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print('formnya valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username and password')
                return redirect('/login')
        else:
            return HttpResponse(form.errors)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/login')


class RegisterView(View):
    template_name = 'auth/register.html'

    def get(self, request):
        form = RegisterFrom(request.POST)
        return render(request, self.template_name, {
            'form_tittle': 'Register',
            'form': form
        })

    def post(self, request):
        form = RegisterFrom(request.POST)
        if form.is_valid():
            print("formnya valid")
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                user = User()
                user.username = form.cleaned_data['username']
                user.password = form.cleaned_data['password1']
                user.set_password(user.password)
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.email = form.cleaned_data['email']
                user.save()
                return redirect('/login')
            else:
                messages.error(request, 'your password is not correct')
        else:
            return HttpResponse(request, form.errors)


class ListInbox(View):
    template_name = 'list_inbox.html'

    def get(self, request):
        return render(request, self.template_name)


class MessageView(View):
    template_name = 'send_message_form.html'

    def get(self, request):
        form = AES_Form(request.POST)
        ntru_form = Ntru_Form(request.POST)
        return render(request, self.template_name, {
            'form': form,
            'ntru_form': ntru_form
        })


class AES_View(View):
    template_name = 'send_message_form.html'

    def get(self, request):
        aes_form = AES_Form(request.GET)
        ntru_form = Ntru_Form(request.GET, request.FILES)
        msg = aes_form['message'].value()
        key = aes_form['key'].value()
        encript_message = encrypt_AES_GCM(msg.encode(), key.encode())
        key_ntru = ntru_form['key'].value()
        key_ntru = aes_form['key'].value()
        print("hasil encrip message : ", encript_message)
        obj = Message()
        obj.send_from = request.user.email
        obj.send_to = aes_form['send_to'].value()
        obj.enc_message = encript_message
        obj.save()

        print(request.user.email)
        print(aes_form['send_to'].value())
        print("aes_form : ", request.GET)
        print("ntru_key_aes :", aes_form['key'].value())
        print("ntru_form :", ntru_form['key'])

        return render(request, self.template_name, {
            'aes_form': aes_form,
            'form': aes_form,
            'ntru_form': ntru_form,
            'obj_id':obj.id,

        })


from django.conf import settings


class Ntru_EncriptView(View):
    def post(self, request):
        ntru_form = Ntru_Form(request.POST)
        if ntru_form.is_valid():
            print('valid')
            print(settings.BASE_DIR)
            npz = '.npz'
            ntru_key = ntru_form.cleaned_data['key']
            pub_key_name = ntru_form.cleaned_data['pub_key']
            priv_key_name = ntru_form.cleaned_data['priv_key']
            pub_key_name += npz
            priv_key_name += npz
            src_dir = os.path.join(settings.BASE_DIR, 'apps/hybrid_libs/ntru_ok')
            des_dir = os.path.join(settings.BASE_DIR, 'media/files')

            asal = os.path.join(src_dir, str(ntru_key) + '.txt')
            file = open(asal, "w")
            file.write(ntru_key)
            file.close()
            ntru_py = os.path.join(src_dir, 'ntru.py')
            fix = str(ntru_key) + '.txt'
            enc_ntru_key = os.path.join(settings.BASE_DIR, str(ntru_key)+'_ntru_encript'+'.txt')
            print("sumber priv_key :",os.path.join(src_dir , str(priv_key_name)))
            print("des pri_key :",os.path.join(des_dir ,str(priv_key_name)))
            print("sumber priv_key :",os.path.join(src_dir , str(pub_key_name)))
            print("des pub_key :",os.path.join(des_dir ,str(pub_key_name)))
            subprocess.run(['python', ntru_py, '-v', 'gen', '167', '3', '128', priv_key_name, pub_key_name])

            open(enc_ntru_key, 'w')
            subprocess.run(['python', ntru_py, 'enc', pub_key_name, fix, ">>", enc_ntru_key])
            # shutil.move(os.path.join(settings.BASE_DIR , str(priv_key_name)), os.path.join(des_dir ,str(priv_key_name)))
            # shutil.move(os.path.join(settings.BASE_DIR, str(pub_key_name)), os.path.join(des_dir , str(pub_key_name)))
            # obj = Message.objects.get(id=id)



            return redirect('/send_message')
        else:
            pass

            "cek value dari masing2 form /clear"
            "generate menggunakan subprocess"
            "simpan privat_key ntru, public_key"
            "encript aes_key menggunakan ntru pbk--> menghasilkan enc_key"
            "DELETE key di model"


class Decript_NTRU_View(View):
    template_name = 'detail_message.html'

    def get(self, request):
        form = Decript_NtruForm(request.POST)
        return render(request, self.template_name, {
            'form': form
        })

    "ambil file key.txt, dan ntru priv_key, send_form attribut dari database"
    "enc_massage dari database"
    "buat ntru decript"
    "decript key aseli dengan aes"
    "tampilkan message"
