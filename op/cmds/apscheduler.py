import os
import sys
import logging
import subprocess
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

logger = logging.getLogger(__name__)
# pwd = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(pwd + "/../")
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'op.settings')
# import django
#
# django.setup()

from ipmiRender.models import IpmiRender

class IPMI:
    def __init__(self):
        pass

    def exec_cmd(self, i):
        cmd1 = subprocess.Popen(
            "ipmitool -I %s -R 1 -H %s -U %s -P %s power status" % (i.intf, i.ip, i.username, i.password),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output = bytes.decode(cmd1.stdout.read())
        print(output)
        if output:
            if 'on' in output:
                status = 1
            else:
                status = 0
        else:
            status = 2
        if status != i.status:
            i.status = status
            print(i.ip, i.status)
            i.save()

    def update_status(self,id=0):
        if not id:
            rrs = IpmiRender.objects.all()
            for i in rrs:
                self.exec_cmd(i)
        else:
            self.exec_cmd(id)

    def stop(self, id):
        i = IpmiRender.objects.get(id=id)
        cmd1 = subprocess.Popen(
            "ipmitool -I %s -R 1 -H %s -U %s -P %s power stop" % (i.intf, i.ip, i.username, i.password),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.exec_cmd(i)

    def start(self, id):
        i = IpmiRender.objects.get(id=id)
        cmd1 = subprocess.Popen(
            "ipmitool -I %s -R 1 -H %s -U %s -P %s power start" % (i.intf, i.ip, i.username, i.password),
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        self.exec_cmd(i)


# IPMI().update_status()

