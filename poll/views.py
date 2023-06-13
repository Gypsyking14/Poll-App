
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello,Obidients. you're at Cohort-1 polls index.")

