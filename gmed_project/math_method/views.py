import json

from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import Parameters
from visor.models import Research


@csrf_exempt
def calculate(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound("not found")

    else:
        if request.method == 'POST':
            input_data = json.loads(request.body.decode('utf-8'))
            print(input_data)
            # берём pk из сессии: research = Research.objects.get(pk=request.session['research_id'])

            research = Research.objects.get(pk=2)

            # Тут нужно магии добавить и сохранение

            parameters = Parameters.objects.filter(research__pk=research.id)

            report = [{
                'name': parameter.parameter.name,
                'description': parameter.parameter.description,
                'measure': parameter.parameter.measure,
                'normal_value': parameter.parameter.normal_value,
                'delta': parameter.parameter.delta,
                'value': parameter.value,
                'diagnoses': parameter.diagnoses.name,
            } for parameter in parameters]

            return JsonResponse({'report': report})
