from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .forms import ContactForm
from .models import CategoryCard, Tovar
from .templatetags.web_tags import *



class WebCatalog(ListView):
    model = CategoryCard
    template_name = 'web/main.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return CategoryCard.objects.order_by('category_title')


class WebTovars(ListView):
    paginate_by = 5
    model = Tovar
    template_name = 'web/tovars.html'
    context_object_name = 'tovars'

    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = get_categories
        return context


    def get_queryset(self):
        return Tovar.objects.filter(cat_id=self.kwargs['catalog_id'])


def tovar_card(request, catalog_id, tov_id):
    tovar = get_object_or_404(Tovar, cat_id=catalog_id, tovar_id=tov_id)
    context = {'tovar': tovar
               }

    return render(request, 'web/tovar.html', context)


def catalog(request):
    tovars = get_tovars('tovar_title')
    paginator = Paginator(tovars, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'tovars': tovars,
               'page_obj': page_obj,
               'categories': get_categories,
                }

    return render(request, 'web/tovars.html', context)


def about(request):
    return render(request, 'web/about.html', {'categories': get_categories})


def contacts(request):
    context = {}
    context['categories'] = get_categories
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            send_message(form.cleaned_data['name'],
                         form.cleaned_data['email'],
                         form.cleaned_data['message'],
                         form.cleaned_data['file']
                         )
            context = {'success':  1}
    else:
        form = ContactForm()


    context['form'] = form

    return render(request,
                  'web/contacts.html',
                  context=context)


def send_message(name, email, message, file):
    """email_subject = 'Сообщение через контактную форму'
    email_body = f"С сайта отправлено новое сообщение\n" \
                 f"Имя отправителя: {name}\n" \
                 f"E-mail отправителя: {email}\n" \
                 f"Сообщение:\n{message}"""
    send_email = EmailMessage('Cообщение с сайта',
                              f"Ое, {name}, ты зачем нам пишешь?\n"
                              "Не пиши нам болще, от тебя гавной воняет",
                              to=[f'{email}'])
    send_email.send()



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Ты чё понаписал в URL сайта, БАРАН!!!</h1>')