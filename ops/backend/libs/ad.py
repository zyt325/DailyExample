class AD():
    def __init__(self, host='10.9.1.42', display=True, debug=True):
        from ldap3 import Server, Connection, ALL, NTLM
        self._ldap_host = host
        self._ldap_user = 'ad\\zhangyt'
        self._ldap_pass = '7my_9rJg'
        server = Server(self._ldap_host, port=389, use_ssl=False, get_info=ALL)
        self.conn = Connection(server, user=self._ldap_user, password=self._ldap_pass, authentication=NTLM,
                               auto_bind=True)
        self._dn = {'base': 'dc=ad,dc=base-fx,dc=com'}
        self._dgattrs = {'user': {}}
        self._dgattrs['user']['dn'] = ','.join(['ou=Basers', self._dn['base']])

    def cur_user(self):
        return self.conn.extend.standard.who_am_i()

    def search_attr(self, attrs='cn', value='', search_range=0, reponse=0):
        from ldap3 import SUBTREE
        attr = ['cn', 'uidNumber', 'displayName', 'department', 'userAccountControl', 'adminCount', 'member',
                'lockoutTime']
        if not isinstance(attrs, list): attrs = [attrs]
        if search_range == 1 and len(attrs) == 1:
            searchfilter = "(&(objectClass=user)(%s=" % attrs[0] + "*" + "%s" % value + "*))"
        elif search_range == 0 and len(attrs) == 1:
            searchfilter = "(&(objectClass=user)(%s=%s))" % (attrs[0], value)
        elif attrs[0] == 'cn':
            searchfilter = search_range
        else:
            searchfilter = search_range
            attr = attrs
        self.conn.search(search_base=self._dgattrs['user']['dn'], search_filter=searchfilter, search_scope=SUBTREE,
                         attributes=attr)
        result = self.conn.entries
        if reponse:
            result = self.conn.response  # [{},{}]
        else:
            result = self.conn.entries
        if result != []:
            return result
        else:
            return False

    def check_user_enabled(self, usercontrol):
        old_usercontrol = int(usercontrol)
        useraccountcontrol = old_usercontrol
        useraccountcontrols = [16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 8192,
                               4096, 2048, 512, 256, 128, 64, 32, 16, 8, 2, 1]
        uac_array = []
        for uac in useraccountcontrols:
            if useraccountcontrol >= uac:
                uac_array.append(uac)
                useraccountcontrol = useraccountcontrol - uac
        if 2 not in uac_array:
            return True, old_usercontrol
        return False, old_usercontrol

    def check_user_unlocked(self, lockouttime):
        if lockouttime is None or str(lockouttime) == '1601-01-01 00:00:00+00:00':
            return True
        else:
            return False

    def check_user(self, username):
        search_result = self.search_attr(value=username)
        result_info = {}
        # print(search_result)
        if search_result:
            user_enabled = self.check_user_enabled(search_result[0].userAccountControl.value)
            user_unlocked = self.check_user_unlocked(search_result[0].lockoutTime.value)
            result_info.setdefault('enabled', user_enabled[0])
            result_info.setdefault('unlocked', user_unlocked)
            result_info.setdefault('exist', True)
            return result_info
        else:
            result_info.setdefault('exist', False)
            return result_info

    def set_user_attr(self, username, attrs):
        from ldap3 import MODIFY_REPLACE
        search_result = self.search_attr(value=username, reponse=1)
        # print(search_result)
        result_info = {}
        if search_result:
            user_dn = search_result[0]['dn']
            print(user_dn)
            modify_attr = {}
            for k, v in attrs.items():
                modify_attr.setdefault(k, []).append(MODIFY_REPLACE)
                modify_attr.setdefault(k, []).append([v])
            self.conn.modify(user_dn, modify_attr)
            result_info.setdefault('status', self.conn.result['result'])
        else:
            result_info.setdefault('exist', False)
        return result_info

    def test(self):
        return self.conn

    def unlock(self, username):
        return self.set_user_attr(username, {'lockoutTime': 0})

    def enable_user(self, username):
        return self.set_user_attr(username, {'userAccountControl': 66048})

    def disable_user(self, username):
        return self.set_user_attr(username, {'userAccountControl': 66050})