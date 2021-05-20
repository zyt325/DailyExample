import os
import sys
from django.core.exceptions import ObjectDoesNotExist

sys.path.append("/sw/systems/shared/python3/")
from Inventory import Inventory

inventory = Inventory()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ops.settings')
import django

django.setup()
from cmdb import models


def host():
    for k, v in inventory.items(item_type='Server').items():
        # print(v)
        s = models.Host()
        s.hostname = "%s.%s.base-fx.com" % (v['hostname'], v['city'])
        s.name = v['hostname']
        s.save()

def label(name):
    for k, v in inventory.items(item_type='Server').items():
        if v[name]:
            obj, created = models.Label.objects.get_or_create(name=name, value=v[name])
            obj.name = name
            obj.value = v[name]
            obj.save()

def map_host_label(name='system_class'):
    for k, v in inventory.items(item_type='Server').items():
        if v[name]:
            try:
                s = models.Host.objects.get(hostname="%s.%s.base-fx.com" % (v['hostname'], v['city']))
                l = models.Label.objects.get(name=name, value=v[name])
                # print(s,l)
                models.HostMapLabel.objects.get_or_create(host=s, label=l)
            except Exception:
                pass
def basic_info(name='ram'):
    for k, v in inventory.items(item_type='Server').items():
        if v[name]:
            map={'ram':'memory'}
            obj, created = models.BasicInfo.objects.get_or_create(type=map[name], value=v[name])
            obj.type = map[name]
            obj.name = v['name']
            obj.comment = '单位:G'
            obj.save()
            # models.BasicInfo.objects.get_or_create(type="nic", value={"eth0": v['ip'][0]})

def basic_info_ip():
    for k, v in inventory.items(item_type='Server').items():
        if v['ip']:
            if len(v['ip']) == 1:
                obj, created = models.BasicInfo.objects.get_or_create(type='nic', value={"eth0": v['ip'][0]})
                obj.type = 'nic'
                obj.name = v['hostname']
                obj.save()
                # models.BasicInfo.objects.get_or_create(type="nic", value={"eth0": v['ip'][0]})
            else:
                obj, created = models.BasicInfo.objects.get_or_create(type='nic', value={"eth0": v['ip']})
                obj.type = 'nic'
                obj.name = v['hostname']
                obj.save()
                # models.BasicInfo.objects.get_or_create(type="nic", value={"eth0": v['ip']})
def map_host_basic(name='ram'):
    for k, v in inventory.items(item_type='Server').items():
        if v[name]:
            map = {'ram': 'memory'}
            try:
                s = models.Host.objects.get(hostname="%s.%s.base-fx.com" % (v['hostname'], v['city']))
                i = models.BasicInfo.objects.get(type=map[name], value=v[name])
            except Exception:
                pass
            models.HostMapBasicInfo.objects.get_or_create(host=s, basic_info=i)


def map_host_basic_ip():
    for k, v in inventory.items(item_type='Server').items():
        if v['ip']:
            try:
                s = models.Host.objects.get(hostname="%s.%s.base-fx.com" % (v['hostname'], v['city']))
                if len(v['ip']) == 1:
                    i = models.BasicInfo.objects.get(value={"eth0": v['ip'][0]})
                else:
                    i = models.BasicInfo.objects.get(value={"eth0": v['ip']})
            except Exception:
                pass
            models.HostMapBasicInfo.objects.get_or_create(host=s, basic_info=i)

# label('os')
# map_host_label('os')
basic_info()
# map_host_basic()