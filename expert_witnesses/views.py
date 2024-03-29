from django.shortcuts import render

from .models import AreaOfExpertise, Expert


def browser(request):
    aoe = AreaOfExpertise.objects.all().order_by('field')

    experts = Expert.objects.all()

    institutes = set()
    for expert in experts:
        institutes.add(expert.institute) if expert.institute is not None else None

    name = request.GET.get('name')
    institute = request.GET.get('institute')
    expertise = request.GET.get('expertise')

    if name:
        experts = experts.filter(name__contains=request.GET.get('name'))

    if institute:
        experts = experts.filter(institute=request.GET.get('institute'))

    if expertise:
        experts = experts.filter(expertise=AreaOfExpertise.objects.filter(field=expertise)).distinct()

    return render(request, 'expertBrowser.html', {'experts': experts, 'institutes': institutes, 'aoe': aoe, 'name': name, 'institute': institute, 'expertise': expertise})


def viewer(request, id):
    expert = Expert.objects.get(id=id)
    return render(request, 'expertViewer.html', {'expert': expert})
