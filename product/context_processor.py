from .models import SubCategory


def get_all_sub_category(request):
    return {
        'all_sub_category': SubCategory.objects.all(),
    }
