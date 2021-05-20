import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, LDAPGroupQuery

AUTH_LDAP_ALWAYS_UPDATE_USER = True
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_TIMEOUT = 3600
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

AUTH_LDAP_SERVER_URI = "ldap://pdc.base-fx.com"
AUTH_LDAP_BIND_DN = "cn=zhangyt,ou=NON,ou=BJ,ou=Basers,dc=ad,dc=base-fx,dc=com"
AUTH_LDAP_BIND_PASSWORD = "7my_9rJg"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=Basers,dc=ad,dc=base-fx,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
)

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    "ou=Basers,dc=ad,dc=base-fx,dc=com", ldap.SCOPE_SUBTREE, "(objectClass=group)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
AUTH_LDAP_REQUIRE_GROUP = (
        LDAPGroupQuery("cn=ITD,ou=Basers,dc=ad,dc=base-fx,dc=com")
        | LDAPGroupQuery("cn=PLE,ou=Basers,dc=ad,dc=base-fx,dc=com")
)

AUTH_LDAP_USER_ATTR_MAP = {"first_name": "givenName", "last_name": "sn", "email": "mail"}
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": (
            LDAPGroupQuery("cn=ITD,ou=Basers,dc=ad,dc=base-fx,dc=com")
            | LDAPGroupQuery("cn=PLE,ou=Basers,dc=ad,dc=base-fx,dc=com")
    ),
    "is_staff": (
        LDAPGroupQuery("cn=ITD,ou=Basers,dc=ad,dc=base-fx,dc=com")
    ),
    # "is_active": "cn=ITD,ou=Basers,dc=ad,dc=base-fx,dc=com",
    # "is_staff": "cn=ITD,ou=Basers,dc=ad,dc=base-fx,dc=com",
    "is_superuser": "cn=ITD,ou=Basers,dc=ad,dc=base-fx,dc=com"
}

AUTHENTICATION_BACKENDS = [
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
]
