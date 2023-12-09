from . models import Category
#this file is used to save links
def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)