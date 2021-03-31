from store.models import Category

def categories(self):
    return {
        'categories': Category.objects.all()
    }