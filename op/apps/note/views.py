import json
from urllib import parse
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models

# Create your views here.

def index(request):
    return render(request,'note/index.html',{})

def get_rrs(request):
    from django.core.paginator import Paginator
    from django.core import serializers
    search_text = request.GET.get('search', 0)
    page_limit = request.GET.get('limit', 15)
    page_offset = request.GET.get('offset', 0)
    sort = request.GET.get('sort', 'title')
    sort_order = request.GET.get('order', 'asc')
    if sort_order == 'asc':
        notes = models.Note.objects.filter(Q(title__isnull=False)).order_by('%s' % sort)
    else:
        notes = models.Note.objects.filter(Q(title__isnull=False)).order_by('-%s' % sort)
    if search_text:
        notes = notes.filter(Q(title__icontains=search_text) | Q(body__icontains=search_text))
    if not page_offset:
        page = 1
    else:
        page = int(int(page_offset) / int(page_limit) + 1)
    paginator = Paginator(notes, page_limit)
    notes_page = paginator.get_page(page)
    query_result = serializers.serialize('json', notes_page,
                                         fields=('id', 'title','file_name','create_at'))
    result = {}
    # print(query_result)
    # json -> list, get need data
    notes_count = notes.count()
    result['total'] = notes_count
    result['totalNotFilteredField'] = notes_count
    result['pageNumber'] = page
    result['rows'] = []
    for rr in json.loads(query_result):
        rr['fields']['id'] = rr['pk']
        result['rows'].append(rr['fields'])
    return HttpResponse(json.dumps(result))

@csrf_exempt
def add_note(request):
    if request.method=='GET':
        return render(request,'note/add.html',{})
    elif request.method=='POST':
        from django.utils.timezone import now
        from libs.Common import genera_uuid
        from libs.Note import save_article
        pwd=request.POST['pwd']
        if pwd!='325':
            return HttpResponse(3)
        title=request.POST['title']
        body_html=request.POST['txt']
        filename_rand = "note_%s.html" % genera_uuid()
        create_date=now()
        if len(models.Note.objects.filter(title=title)) !=0:
            return HttpResponse(2)
        try:
            note=models.Note(title=title,body=body_html,file_name=filename_rand,create_at=create_date)
            note.save()
            save_article(filename_rand, title,note.id,parse.unquote(body_html))
            return JsonResponse({'status':1,'result':{'filename':filename_rand}})
        except Exception as e:
            print(type(e),e)
            return HttpResponse(4)
@csrf_exempt
def edit_note(request):
    if request.method=='GET':
        note_id = request.GET.get('id')
        note=models.Note.objects.filter(id=note_id)
        note_body=note[0].body
        note_title=note[0].title
        return render(request,'note/edit.html',context=locals())
    elif request.method=='POST':
        from django.utils.timezone import now
        from libs.Note import save_article
        pwd=request.POST['pwd']
        if pwd!='325':
            return HttpResponse(3)
        title=request.POST['title']
        body_html=request.POST['txt']
        id=request.POST['id']
        create_date=now()
        if len(models.Note.objects.filter(
                Q(title=title) & ~Q(id=id))) > 0:
            return HttpResponse(2)
        try:
            note = models.Note.objects.filter(id=id)[0]
            note.title=title
            note.body=body_html
            file_name=note.file_name
            note.save()
            save_article(file_name, title,note.id,parse.unquote(body_html))
            return JsonResponse({'status':1,'result':{'filename':file_name}})
        except Exception as e:
            print(type(e),e)
            return HttpResponse(4)

@csrf_exempt
def op(request):
    action=request.POST['action']
    from django.utils.timezone import now
    from libs.Common import genera_uuid
    from libs.Note import save_article
    if action=='del':
        ids = request.POST['ids']
        for i in json.loads(ids):
            rs = models.Note.objects.filter(id=i)
            if action == 'add':
                rs[0].workday = ''
                rs[0].category = ''
                rs[0].save()
            elif action == 'del':
                rs[0].delete()
        return HttpResponse(1)

@csrf_exempt
def uploadImg(request):
    if request.method == 'POST':
        import os
        from django.conf import settings
        upload_path = settings.MEDIA_ROOT + '/uploads/'
        upload_url = settings.MEDIA_URL + 'uploads/'
        if not os.path.exists(upload_path):
            os.makedirs(upload_path)
        imgs = request.FILES
        result={"data":[],"errno": 0}
        for img in imgs:
            imgPath = upload_path + img
            imgUrl = upload_url + img
            with open(imgPath.encode('utf-8'), 'wb') as f_img:
                for i in imgs[img].chunks():
                    f_img.write(i)
            result['data'].append({'url':imgUrl,'alt':img,'href':imgUrl})
        return JsonResponse(result)
