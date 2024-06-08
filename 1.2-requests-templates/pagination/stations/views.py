from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import csv




def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        bus_stations = []
        for row in reader:
            record = {
                'Name': row.get('Name'),
                'Street': row.get('Street'),
                'District': row.get('District'),
            }
            bus_stations.append(record)

    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, 7)
    page = paginator.get_page(page_number)

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
