import json
from typing import Any
from .models import Table
from .forms import table_form
from django.core import serializers
from django.shortcuts import HttpResponse
from django.views.generic.list import ListView
from django.http import HttpRequest, JsonResponse


class Table_view(ListView):
    model = Table
    template_name = 'spa_app/table.html'
    context_object_name = 'table'
    paginate_by = 5


    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_form'] = table_form
        return context

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any):
        response = super().dispatch(request, *args, **kwargs)

        def isfloat(a):
            try:
                z = float(a)
                return True
            except:
                return False
        def is_ajax(request):
            return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
        if is_ajax(request=request):
            user_form = table_form(request.GET)
            quer = ''
            if user_form.data['column'] != '-':
                if user_form.data['find_text'] == '':
                    quer = Table.objects.order_by(
                        f"{user_form.data['column']}")[:int(user_form.data['paginate_field'])]

                if user_form.data['filter_condition'] == '-' and user_form.data['find_text'] != '' and quer == '':
                    if user_form.data['column'] != 'name' and not isfloat(user_form.data['find_text']):
                        err = {
                            'ValueError': 'The value must be a number or a float'}
                        return JsonResponse({"errors": json.dumps(err)}, status=400)
                        # raise TypeError('Значение должно быть числом или числом с плавающей точкой')
                    else:
                        quer = Table.objects.raw(
                            f"SELECT * FROM public.spa_app_table WHERE {user_form.data['column']} = '{user_form.data['find_text']}' order by {user_form.data['column']} limit {user_form.data['paginate_field']};")

                if user_form.data['find_text'] != '' and user_form.data['filter_condition'] != '-' and quer == '':
                    if user_form.data['filter_condition'] != 'include' and user_form.data['column'] != 'name':
                        if not isfloat(user_form.data['find_text']):
                            err = {
                                'ValueError': 'The value must be a number or a float'}
                            return JsonResponse({"errors": json.dumps(err)}, status=400)
                            # raise TypeError('Значение должно быть числом или числом с плавающей точкой')
                        quer = Table.objects.raw(
                            f"SELECT * FROM public.spa_app_table WHERE {user_form.data['column']} {user_form.data['filter_condition']} {user_form.data['find_text']} order by {user_form.data['column']} limit {user_form.data['paginate_field']};")
                    elif user_form.data['filter_condition'] != 'include' and user_form.data['column'] == 'name':
                        err = {
                            'OperationError': 'Operations [>, <, =] can only be applied to the fields AMOUNT and DISTANCE'}
                        return JsonResponse({"errors": json.dumps(err)}, status=400)
                        # raise TypeError('Операции [>, <, =] могут быть применены только к полям AMOUNT и DISTANCE')
                    elif user_form.data['filter_condition'] == 'include':
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
            else:
                quer = Table.objects.all()[:int(
                    user_form.data['paginate_field'])]
            table_response = serializers.serialize(
                'json', quer, fields={'date', 'name', 'amount', 'distance'})
            return JsonResponse({'success': table_response}, status=200)
        else:
            return response
