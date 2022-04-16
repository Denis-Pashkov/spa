import random
from typing import Any
from urllib import response
from attr import fields
from django.forms import model_to_dict
from django.views.generic.list import ListView
from django.shortcuts import redirect, render
from requests import request
from rest_framework.response import Response
from django.http import HttpRequest, HttpResponse, JsonResponse
from .serializers import TableSerializer
from . import models
from spa_app.models import Table
from django.core import serializers
from rest_framework import generics
from rest_framework.views import APIView
from .forms import table_form

# Create your views here.

# class Table(ListView):
#     model = Reviews
#     context_object_name = 'reviewes_list'
#     try:
#         queryset = Reviews.objects.order_by('-date')[:15]
#     except:
#         paginate_by = 15
#     template_name = 'home/in_menu/about/reviews.html'


def table(request):
    return render(request, 'spa_app/table.html')


class Table_view(ListView):
    # if request.is_ajax and request.method
    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    # if request.is_ajax:
    #     table = Table.objects.all()[:5].values_list
    #     ser_instance = serializers.serialize('json', [ table, ])
    #     # send to client side.
    #     return JsonResponse({"instance": ser_instance}, status=200)
    # return super().get(request, *args, **kwargs)
    model = Table
    template_name = 'spa_app/table.html'
    context_object_name = 'table'
    print('is ok')
    paginate_by = 5

    # for i in range(1, 501):

    #     def rd_asd():
    #         rd = float(str(random.randint(1, 4000)) + '.' + str(random.randint(1, 999)))
    #         return rd

    #     new_s1 = Table(name=f'Name{i}', amount=rd_asd(), distance=rd_asd())
    #     new_s1.save()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_form'] = table_form
        return context

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        response = super().dispatch(request, *args, **kwargs)
        if request.is_ajax():
            print('--------------asd')
            user_form = table_form(request.GET)
            # print(user_form.data['column'], user_form.data['filter_condition'], user_form.data['paginate_field'],
            #       user_form.data['find_text'], sep='\n')
            table_response = serializers.serialize('json', Table.objects.all()[:int(user_form.data['paginate_field'])], fields={
                                                   'id', 'date', 'name', 'amount', 'distance'})
            # print(Table.objects.all()[:5].values)
            return JsonResponse({'success': table_response}, status=200)
        else:
            return response

    # def dispatch(request, *args, **kwargs):
    #         response = super().dispatch(request, *args, **kwargs)
            # if request.is_ajax():
            #    return JsonResponse({'success': 1}, status=200)
            # else:
            #    return response


# class TableApiView(generics.ListAPIView):
#     queryset = Table.objects.all()
#     serializer_class = TableSerializer


class TableApiView(APIView):
    def get(self, request):
        lst = Table.objects.all()[:5].values_list()
        if request.is_ajax():
            # table = {'table': Response({'get': lst})}
            # return render(request, 'spa_app/table.html', table)

            table = serializers.serialize(
                'json',
                Table.objects.all()[:5],
                fields=('id', 'date', 'name', 'amount', 'distance')
            )
            # Возвращать простым Response, также возвращается JSON
            return JsonResponse({'table': table}, status=200)

            return JsonResponse({'success': True}, status=201)
        else:
            return Response({'get': lst})

    def post(self, request):
        post_new = Table(
            name=request.data['name'], amount=request.data['amount'], distance=request.data['distance'])
        post_new.save()
        return Response({'post': model_to_dict(post_new)})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context

    # new_s1 = Table(name = 'Name1', amount = 122.3, distance = 11.431)
    # new_s1.save()
    # new_s1 = Table(name = 'Name2', amount = 33.3, distance = 654.787)
    # new_s1.save()
    # new_s1 = Table(name = 'Name3', amount = 112.3, distance = 34.673)
    # new_s1.save()
    # new_s1 = Table(name = 'Name4', amount = 123.3, distance = 89.874)
    # new_s1.save()
    # new_s1 = Table(name = 'Name5', amount = 435.3, distance = 56.455)
    # new_s1.save()
    # new_s1 = Table(name = 'Name6', amount = 1.3, distance = 44.345)
    # new_s1.save()
    # new_s1 = Table(name = 'Name7', amount = 44.3, distance = 66.234)
    # new_s1.save()
    # new_s1 = Table(name = 'Name8', amount = 23.3, distance = 22.235)
    # new_s1.save()
    # new_s1 = Table(name = 'Name9', amount = 534.3, distance = 123.242)
    # new_s1.save()
    # new_s1 = Table(name = 'Name10', amount = 12.3, distance = 423.651)
    # new_s1.save()
    # new_s1 = Table(name = 'Name11', amount = 330.3, distance = 30.764)
    # new_s1.save()
    # new_s1 = Table(name = 'Name12', amount = 3.3, distance = 33.234)
    # new_s1.save()
