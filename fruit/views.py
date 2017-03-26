from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from .models import Fruit, SectionItem


def index(request):
    fruit_list = Fruit.objects.all()
    output = '<br/> '.join([item.name for item in fruit_list])
    return HttpResponse(output)

@csrf_exempt
def addfruit(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        name = req['name']
        description = req['description']
        new_fruit = Fruit()
        new_fruit.name = name
        new_fruit.description = description
        print new_fruit
        fruit_list = Fruit.objects.filter(name = name)
        for item in fruit_list:
            item.delete()
        new_fruit.save()

        # remove all furit section
        seciont_list = SectionItem.objects.filter(sectionItem__name = name)
        for item in seciont_list:
            item.delete()

        section_list = req['section']
        for item in section_list:
            section_item = SectionItem()
            section_item.section = item['title']
            section_item.content = item['content']
            section_item.itemType = 1
            section_item.sectionItem = new_fruit
            section_item.save()
        # fruit_list = Fruit.objects.all()
        print fruit_list


    return HttpResponse("404")