from multiprocessing import Condition
from random import choices
from django import forms


class table_form(forms.Form):

    column_choices = (
        ('-', '-'),
        # ('date', 'DATE'),
        ('name', 'NAME'),
        ('amount', 'AMOUNT'),
        ('distance', 'DISTANCE'),
    )
    
    filter_choices = (
        ('-', '-'),
        ('=', '='),
        ('>', '>'),
        ('<', '<'),
        ('include', 'include'),
    )

    paginate = (
        ('5', '5'),
        ('10', '10'),
        ('20', '20'),
        ('50', '50'),
        ('100', '100'),
        ('200', '200'),
    )
    column = forms.ChoiceField(choices=column_choices)
    filter_condition = forms.ChoiceField(choices=filter_choices)
    paginate_field = forms.ChoiceField(choices=paginate)
    find_text = forms.CharField(max_length=20, required=False)
    
