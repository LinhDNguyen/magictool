import json
from django.conf import settings
from django.http import HttpResponse
from django.template import Context, RequestContext, Template, loader
from models import Category


def index(request):

    t = loader.get_template('note_list.html')
    categories = Category.objects.all()


    c = RequestContext(request, {
        'categories': categories,
    })
    rendered_template = t.render(c)
    return HttpResponse(rendered_template)