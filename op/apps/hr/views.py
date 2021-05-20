import json
from django.shortcuts import render
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    return render(request, 'hr/index.html', {})


def get_rrs(request):
    from django.core.paginator import Paginator
    from django.core import serializers
    search_text = request.GET.get('search', 0)
    page_limit = request.GET.get('limit', 15)
    page_offset = request.GET.get('offset', 0)
    sort = request.GET.get('sort', 'username')
    sort_order = request.GET.get('order', 'asc')

    if sort_order == 'asc':
        employees = models.PeopleViewItd.objects.filter(Q(username__isnull=False)).order_by('%s' % sort)
    else:
        employees = models.PeopleViewItd.objects.filter(Q(username__isnull=False)).order_by('-%s' % sort)
    if search_text:
        employees = employees.filter(
            Q(username__icontains=search_text) | Q(chinese_full_name__icontains=search_text) | Q(
                english_full_name__icontains=search_text))
    if not page_offset:
        page = 1
    else:
        page = int(int(page_offset) / int(page_limit) + 1)
    paginator = Paginator(employees, page_limit)
    employees_page = paginator.get_page(page)
    query_result = serializers.serialize('json', employees_page,
                                         fields=('id', 'category', 'status', 'username', 'chinese_full_name',
                                                 'english_full_name', 'start_date', 'employee_start_date', 'end_date',
                                                 'mobile', 'country_code', 'gender', 'office_code', 'department_code',
                                                 'disable_account_date', 'backup_delete_email_date', 'is_production',
                                                 'level_code'))
    result = {}
    # print(query_result)
    # json -> list, get need data
    employees_count = employees.count()
    result['total'] = employees_count
    result['totalNotFilteredField'] = employees_count
    result['pageNumber'] = page
    result['rows'] = []
    for rr in json.loads(query_result):
        rr['fields']['id'] = rr['pk']
        result['rows'].append(rr['fields'])
    return HttpResponse(json.dumps(result))
