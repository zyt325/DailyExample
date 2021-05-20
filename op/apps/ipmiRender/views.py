import json
import subprocess
import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from libs.serializable import DataEncoder


# Create your views here.
def index(request):
    return render(request, 'ipmirender/index.html', {})


def get_rrs(request):
    res = models.IpmiRender.objects.all().values()
    return HttpResponse(json.dumps(list(res), cls=DataEncoder))
    # return HttpResponse(json.dumps({"data": list(res)}, cls=DataEncoder))


@csrf_exempt
def op(request):
    ops = {'start': 'power on', 'stop': 'power off', 'update': 'power status'}
    action = request.POST['action']
    ids = request.POST['ids']
    try:
        for i in json.loads(ids):
            rs = models.IpmiRender.objects.filter(id=i)
            if rs:
                cmd = "ipmitool  -I %s  -H %s  -U %s  -P %s %s" % (
                    rs[0].intf, rs[0].ip, rs[0].username, rs[0].password, ops[action])
                # print(cmd)
                res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output = res.stdout.read()
                # print(output)
                # print(action)
                if action == 'update' and 'is on' in output.decode():
                    rs[0].status = 1
                elif action == 'update' and 'is off' in output.decode():
                    rs[0].status = 0
                else:
                    rs[0].status = 2
                rs[0].mdate = datetime.datetime.now()
                rs[0].save()
    except Exception as e:
        return HttpResponse(e)
    finally:
        return HttpResponse(1)
