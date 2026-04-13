from .models import Category

def nav_categories(request):
    categories = Category.objects.all()
    return {'nav_categories': categories}
    