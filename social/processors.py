from .models import Link


def extend_contextor(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return  ctx
    