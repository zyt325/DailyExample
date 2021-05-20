import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from . import models
from libs.serializable import DataEncoder


# Create your views here.
def index(request):
    return render(request, 'workday/index.html', {})


def get_rrs(request):
    res = models.Workday.objects.all().values()
    return HttpResponse(json.dumps(list(res), cls=DataEncoder))
    # return HttpResponse(json.dumps({"data": list(res)}, cls=DataEncoder))

    # data_list = []
    # query_set = models.Workday.objects.all()
    # for data_info in query_set:
    #     data_list.append({'id': data_info.id, 'workday': data_info.workday, 'category': data_info.category}
    #                      )
    # data_dict={}
    # data_dict['data']=data_list
    # return HttpResponse(json.dumps(data_dict,cls=DataEncoder))


@csrf_exempt
def op(request):
    if 'action' in request.POST:
        action = request.POST['action']
        ids = request.POST['ids']
        for i in json.loads(ids):
            rs = models.Workday.objects.filter(id=i)
            if action == 'add':
                rs[0].workday = ''
                rs[0].category = ''
                rs[0].save()
            elif action == 'del':
                rs[0].delete()
        return HttpResponse(1)
    else:
        pk = request.POST['pk']
        name = request.POST['name']
        value = request.POST['value']
        if pk == 0:
            r = models.Workday(**{name: value})
            r.save()
        else:
            rs = models.Workday.objects.get(id=pk)
            rs.__dict__.update({name: value})
            rs.save()
        return HttpResponse(1)
