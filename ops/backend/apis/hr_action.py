from django.http import HttpResponse, JsonResponse
from libs.ad import AD
def employee(request):
    action = request.GET.get('action', 'check')
    username = request.GET.get('username', 'None')
    if action == 'check':
        return JsonResponse(AD().check_user(username))
    elif action == 'unlock':
        return JsonResponse(AD().unlock(username))
    elif action == 'enable':
        return JsonResponse(AD().enable_user(username))
    elif action == 'disable':
        return JsonResponse(AD().disable_user(username))