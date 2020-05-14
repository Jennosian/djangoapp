# -*- coding: utf8 -*-
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from ddv_example.models import AgregateData
from ddv_example.models import DetailData
from django.shortcuts import get_object_or_404
from django.utils.html import escape
from django.db.models import Q

from django.shortcuts import render


class TestModelList(TemplateView):
    template_name = 'ddv_example/koondvaade.html'

class TestModelListJson(BaseDatatableView):
    model = AgregateData
    # columns and order columns are provided by datatables in the request using "data" in columns definition


def firma_vaade(request, random_id_code):

    kirje = (DetailData.objects
                .filter(random_id_code__startswith=random_id_code)
                .order_by('-date'))

    context = {'kirje': kirje,
               }
    return render(request, 'ddv_example/firma_vaade.html', context)

