from django.shortcuts import render, redirect
import telebot
from .forms import ContactForm

bot = telebot.TeleBot('1474480112:AAEob5IAylblNY8hg0fmF5yzAEa9yN7tFi4')

def index(request):
    return render(request, 'index.html', {})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mail = form.cleaned_data['mail']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            msg = f"Имя: {name}\n"\
                  f"Имя: {mail}\n"\
                  f"Имя: {subject}\n"\
                  f"Имя: {message}\n"
            bot.send_message(1029994960, msg)
    return redirect('home')


