from django.http import JsonResponse
from .models import Gen

def filter_mother_choices(request):
    father_id = request.GET.get('father_id')
    if father_id:
        mother_choices = Gen.objects.exclude(id=father_id).exclude(father_only=True).values('id', 'name')
        return JsonResponse({'mother_choices': list(mother_choices)})
    return JsonResponse({'mother_choices': []})