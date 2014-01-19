from django.http import HttpResponse

from hits.models import Hit


def index(request):
    Hit.objects.create()

    return HttpResponse('Hello World!' + str(Hit.objects.all().count()))
