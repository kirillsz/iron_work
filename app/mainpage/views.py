
from django.shortcuts import render




import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order

@csrf_exempt  # Отключаем CSRF для простоты, но в продакшене используйте защиту CSRF
def order_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.create(
            phone=data['phone'],
            desc=data['desc']
        )
        return JsonResponse({'id': order.id})  # Возвращает ID созданной заявки
    return HttpResponse(status=400)




def index(request):
	return render(request, 'index.html', {})