import sys
import nmap
import subprocess
sys.path.append('/sw/systems/shared/python')
from DB import DB
from Credentials import DBCredentials

test_con, test_cur = DB().connect(host='10.14.6.159',
                                  user='root',
                                  passwd='mysql325')

# def GetRenderInfo():
#     con, cur = DB().connect_db(DBCredentials('dns'))
#     querySQL = """select r.domain_name,r.value from dns.dns_tool_bindrr r
#     left join dns.dns_tool_bindzones z on r.zone_id=z.id
#     where r.type='A' and z.zone_name='bj.base-fx.com' and r.domain_name like 'ipmi-node%'  
#     """
#     ipmi_rrs = []
#     cur.execute(querySQL)
#     for d in cur.fetchall():
#         ipmi_rrs.append(d)
#     return ipmi_rrs

# def scanIP():
#     nm = nmap.PortScanner()
#     ret = nm.scan(hosts='10.7.30.0/24 10.7.31.0/24 10.7.32.0/24',
#                   ports='80',
#                   arguments="-sS")
#     return ret

# ips = scanIP()

# for d in GetRenderInfo():
#     ip = d['value']
#     if ip in ips['scan'].keys():
#         name = d['domain_name']
#         test_cur.execute(
#             """insert into basefx.ipmi_render(ip,fqdn,status) values("%s","%s",0)"""
#             % (ip, name))

test_cur.execute('select id,ip from basefx.ipmi_render')
for i in test_cur.fetchall():
    import os
    import commands
    print(i['ip'])
    # os.system("ipmitool -I lanplus -H %s -U admin -P admin power status" %
    #   i['ip'])
    status, ouput = commands.getstatusoutput(
        "ipmitool -I lanplus -R 1 -H %s -U admin -P admin power status" %
        i['ip'])

    # status, ouput = commands.getstatusoutput(
    #     "ipmitool -I lanplus -R 1 -H %s -U root -P calvin power status" %
    #     i['ip'])
    print(status, ouput)
    if not status:
        test_cur.execute(
            "update basefx.ipmi_render set username='admin',password='admin' where id=%d "
            % i['id'])
        # test_cur.execute(
        #     "update basefx.ipmi_render set username='root',password='calvin' where id=%d "
        #     % i['id'])
        if 'is on' in ouput:
            test_cur.execute(
                "update basefx.ipmi_render set status=1,intf='lanplus' where id=%d "
                % i['id'])
        else:
            test_cur.execute(
                "update basefx.ipmi_render set status=0,intf='lanplus' where id=%d "
                % i['id'])
    # else:
    #     test_cur.execute(
    #         "update basefx.ipmi_render set status=2 where id=%d " % i['id'])
test_con.commit()
