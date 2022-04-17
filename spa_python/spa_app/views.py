import random
from turtle import distance
from typing import Any
from unicodedata import name
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
    paginate_by = 5

    # for i in range(1, 501):

    #     def set_name():
    #         lst = list('abcdefghigklmnopqrstuvyxwz')
    #         name = ''
    #         for i in range(0, 6):
    #             name += str(random.choice(lst))
    #             if i == 0:
    #                 name = name.upper()
    #         return name

    #     def rd_asd():
    #         rd = float(str(random.randint(1, 4000)) + '.' + str(random.randint(1, 999)))
    #         return rd

    #     new_s1 = Table(name=set_name(), amount=rd_asd(), distance=rd_asd())
    #     new_s1.save()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_form'] = table_form
        return context

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        response = super().dispatch(request, *args, **kwargs)

        def clean_filter_text_to_sort():
            if (user_form.data['find_text'] == '' and user_form.data['filter_condition'] == '-') or (user_form.data['find_text'] == '' and user_form.data['filter_condition'] != '-'):
                return True

        def clean_all():
            if user_form.data['find_text'] != '' and user_form.data['filter_condition'] != '-':
                return True

        def isfloat(a):
            try:
                z = float(a)
                return True
            except:
                return False

        def eq():
            if user_form.data['filter_condition'] == '-' and user_form.data['find_text'] != '':
                return True

        if request.is_ajax():

            user_form = table_form(request.GET)
            quer = ''
            if user_form.data['column'] != '-':
                if clean_filter_text_to_sort():
                    quer = Table.objects.order_by(
                        f"{user_form.data['column']}")[:int(user_form.data['paginate_field'])]

                if eq() and quer == '':
                    if user_form.data['column'] != 'name' and not isfloat(user_form.data['find_text']):
                        raise TypeError(
                            'Значение должно быть числом или числом с плавающей точкой')
                    else:
                        quer = Table.objects.raw(
                            f"SELECT * FROM public.spa_app_table WHERE {user_form.data['column']} = '{user_form.data['find_text']}' order by {user_form.data['column']} limit {user_form.data['paginate_field']};")

                if clean_all() and quer == '':
                    if user_form.data['filter_condition'] != 'include' and user_form.data['column'] != 'name':
                        if not isfloat(user_form.data['find_text']):
                            raise TypeError('Значение должно быть числом или числом с плавающей точкой')
                        quer = Table.objects.raw(
                            f"SELECT * FROM public.spa_app_table WHERE {user_form.data['column']} {user_form.data['filter_condition']} {user_form.data['find_text']} order by {user_form.data['column']} limit {user_form.data['paginate_field']};")
                    elif user_form.data['filter_condition'] == 'include':
                        # cl = user_form.data['column']
                        ft = user_form.data['find_text']
                        if user_form.data['column'] == 'name':
                            quer = Table.objects.filter(name__icontains=f'{ft}').order_by(
                                user_form.data['column'])[:int(user_form.data['paginate_field'])]
                        elif user_form.data['column'] == 'amount':
                            quer = Table.objects.filter(amount__icontains=f'{ft}').order_by(
                                user_form.data['column'])[:int(user_form.data['paginate_field'])]
                        elif user_form.data['column'] == 'distance':
                            quer = Table.objects.filter(distance__icontains=f'{ft}').order_by(
                                user_form.data['column'])[:int(user_form.data['paginate_field'])]

                # if user_form.data['column'] == 'name' and user_form.data['find_text'] != '' and quer == '':
                #     quer = Table.objects.raw(
                #         f"SELECT * FROM public.spa_app_table WHERE {user_form.data['column']} = '{user_form.data['find_text']}' order by {user_form.data['column']} limit {user_form.data['paginate_field']};")

                table_response = serializers.serialize(
                    'json', quer, fields={'id', 'date', 'name', 'amount', 'distance'})
                return JsonResponse({'success': table_response}, status=200)
            else:
                quer = Table.objects.all()[:int(
                    user_form.data['paginate_field'])]
                table_response = serializers.serialize(
                    'json', quer, fields={'date', 'name', 'amount', 'distance'})
                return JsonResponse({'success': table_response}, status=200)
        else:
            return response


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

            # return JsonResponse({'success': True}, status=201)
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
