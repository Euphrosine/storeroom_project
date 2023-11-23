from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import CropsData
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# https://sensor-and-chart.onrender.com/chart_data/?temperature=value&humidity=value&rain=value&ldr=value

def api_data_view(request):
    temperature = request.GET.get('temperature', None)
    humidity = request.GET.get('humidity', None)
    co2 = request.GET.get('co2', None)
    ldr = request.GET.get('ldr', None)
  

    # Create a dictionary to store the data you want to save
    data_to_save = {
        'timestamp': timezone.now(),
        'temperature': temperature,
        'humidity': humidity,
        'co2': co2,
        'ldr': ldr,
    }

    # Remove None values from the dictionary
    data_to_save = {k: v for k, v in data_to_save.items() if v is not None}

    # Create a new entry in the database using the data
    CropsData.objects.create(**data_to_save)

    return JsonResponse({"message": "Data saved successfully"})


@login_required
def crop_data_view(request):
    # Get the data for each field
    temperature_data = CropsData.objects.values_list('timestamp', 'temperature')
    humidity_data = CropsData.objects.values_list('timestamp', 'humidity')
    co2_data = CropsData.objects.values_list('timestamp', 'co2')
    ldr_data = CropsData.objects.values_list('timestamp', 'ldr')
  

    # Prepare the data in a format suitable for Chart.js
    temperature_labels = [entry[0].strftime('%H:%M:%S') for entry in temperature_data]
    temperature_values = [entry[1] for entry in temperature_data]

    humidity_labels = [entry[0].strftime('%H:%M:%S') for entry in humidity_data]
    humidity_values = [entry[1] for entry in humidity_data]

    co2_labels = [entry[0].strftime('%H:%M:%S') for entry in co2_data]
    co2_values = [entry[1] for entry in co2_data]

    ldr_labels = [entry[0].strftime('%H:%M:%S') for entry in ldr_data]
    ldr_values = [entry[1] for entry in ldr_data]


    return render(request, 'storeroom_app/index.html', {
        'temperature_labels': temperature_labels,
        'temperature_values': temperature_values,
        'humidity_labels': humidity_labels,
        'humidity_values': humidity_values,
        'co2_labels': co2_labels,
        'co2_values': co2_values,
        'ldr_labels': ldr_labels,
        'ldr_values': ldr_values,
    })
def tables_view(request):
    # Get the data for each field
    temperature_data = CropsData.objects.all()
    humidity_data = CropsData.objects.all()
    co2_data = CropsData.objects.all()
    ldr_data = CropsData.objects.all()


    return render(request, 'storeroom_app/tables.html', {
        'temperature_data': temperature_data,
        'humidity_data': humidity_data,
        'co2_data': co2_data,
        'ldr_data': ldr_data,
    })

@login_required
def overall_view(request):
    crops_data = CropsData.objects.all()
    return render(request, 'storeroom_app/overall.html', {'crops_data': crops_data})


