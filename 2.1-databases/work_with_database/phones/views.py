from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort')
    records = []
    phone_objects = Phone.objects.all()
    for phone in phone_objects:
        record = {
            'name': phone.name,
            'price': phone.price,
            'image': phone.image,
            'slug': phone.slug,
        }
        records.append(record)
    if sort_type:
        if sort_type == 'name':
            cont = sorted(records, key=lambda x: x['name'])
        elif sort_type == 'min_price':
            cont = sorted(records, key=lambda x: x['price'])
        else:
            cont = sorted(records, key=lambda x: x['price'], reverse=True)
    else:
        cont = records
    context = {
        'phones': cont
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    right_phone = Phone.objects.get(slug=slug)
    context = {
        'phone': {
            'name': right_phone.name,
            'price': right_phone.price,
            'image': right_phone.image,
            'release_date': right_phone.release_date,
            'lte_exists': right_phone.lte_exists,
        }
    }
    return render(request, template, context)
