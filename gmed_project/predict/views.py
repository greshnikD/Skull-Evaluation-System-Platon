import base64
import datetime
import json
import io


from PIL import Image
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from .models import DotList, DotPairs, Coordinates
from visor.models import ResearchFiles, Research, Patient


@csrf_exempt
def recognize_image(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound("not found")

    else:
        if request.method == 'POST':
            input_data = json.loads(request.body.decode('utf-8'))
            imgdata = base64.b64decode(input_data['image'])

            timestamp = datetime.datetime.now().timestamp()

            new_patient = Patient(fio='Test Test Test', version=1)
            new_patient.save()

            research_file = ResearchFiles(
                real_file_name=f'new_{new_patient.id}_{request.user.id}_{timestamp}.jpg',
                showed_file_name=input_data['filename'],
                path='',
                file=input_data['image']
            )
            research_file.save()
            print(f'{research_file.id=}')

            research = Research(
                file=research_file,
                patient=new_patient,
                doctor=request.user,
                version=1
            )
            research.save()
            print(f'{research.id=}')

            request.session['research_id'] = research.id

            im = Image.open(io.BytesIO(imgdata))
            width, height = im.size

            precondition_dots = {
                'A': {'x': 1352, 'y': 1355, 'enabled': True},
                'Ar': {'x': 532, 'y': 1102, 'enabled': True},
                'B': {'x': 1269, 'y': 1678, 'enabled': True},
                'Ba': {'x': 407, 'y': 1186, 'enabled': True},
                'C': {'x': 574, 'y': 966, 'enabled': True},
                'DT': {'x': 1426, 'y': 1805, 'enabled': True},
                'EN': {'x': 1685, 'y': 1209, 'enabled': True},
                'Gn': {'x': 1315, 'y': 1875, 'enabled': True},
                'Go': {'x': 685, 'y': 1556, 'enabled': True},
                'LL': {'x': 1481, 'y': 1589, 'enabled': True},
                'Me': {'x': 1194, 'y': 1875, 'enabled': True},
                'N': {'x': 1403, 'y': 722, 'enabled': True},
                'Or': {'x': 1227, 'y': 1031, 'enabled': True},
                'Po': {'x': 370, 'y': 909, 'enabled': True},
                'Pog': {'x': 1315, 'y': 1875, 'enabled': True},
                'Pt': {'x': 856, 'y': 970, 'enabled': True},
                'S': {'x': 681, 'y': 778, 'enabled': True},
                'SNA': {'x': 1491, 'y': 1261, 'enabled': True},
                'SNP': {'x': 875, 'y': 1280, 'enabled': True},
                'Se': {'x': 681, 'y': 750, 'enabled': True},
                'Sn': {'x': 1532, 'y': 1322, 'enabled': True},
                'UL': {'x': 1546, 'y': 1467, 'enabled': True},
                'aii': {'x': 1222, 'y': 1725, 'enabled': True},
                'ais': {'x': 1278, 'y': 1270, 'enabled': True},
                'ii': {'x': 1306, 'y': 1500, 'enabled': True},
                'is': {'x': 1417, 'y': 1556, 'enabled': True},
                'n': {'x': 1463, 'y': 731, 'enabled': True}}

            pairs_list = [[pair.dot_1.name, pair.dot_2.name, pair.line] for pair in
                          DotPairs.objects.filter(active=True)]

            dots_list = {dot.name: {
                'description': dot.description,
                'editable': 'true' if dot.computability else 'false',
                'x': precondition_dots[dot.name]['x'] if dot.name in precondition_dots else width/2,
                'y': precondition_dots[dot.name]['y'] if dot.name in precondition_dots else height/2,
            } for dot in DotList.objects.all()}

            response_body = {
                'dots': dots_list,
                'pairs': pairs_list
            }

            return JsonResponse(response_body)


@csrf_exempt
def save_results(request):
    if not request.user.is_authenticated:
        return HttpResponseNotFound("not found")

    else:

        if request.method == 'POST':
            input_data = json.loads(request.body.decode('utf-8'))
            research = Research.objects.get(pk=request.session['research_id'])

            for dot in input_data:
                dot_in_list = DotList.objects.get(name=dot)
                new_coordinates = Coordinates(
                    dot=dot_in_list,
                    research=research,
                    x_value=input_data[dot]['x'],
                    y_value=input_data[dot]['y'],
                    z_value=input_data[dot]['z'] if 'z' in input_data[dot] else 0
                )
                new_coordinates.save()
                print(f'{new_coordinates.id=}')

        return JsonResponse({
            'data': 'OK',
            'research_id': research.id
        })
