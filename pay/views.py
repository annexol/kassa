import hashlib
from .models import UserName

from django.shortcuts import render

# Create your views here.


# Тут создается форма платежа, она вроде как работает
def balance(request):
    merchant_id = '6132'
    secret_word = 'kqzE/212XsddscG%&Az*)sd'
    order_id = '154'
    order_amount = '10.11'
    currency = 'RUB'
    sign = hashlib.md5(f'{merchant_id}:{order_amount}:{secret_word}:{currency}:{order_id}'.encode('utf-8')).hexdigest()

    context = {
        'm': merchant_id,
        'oa': order_amount,
        'o': order_id,
        's': sign,
        'currency': currency
    }

    return render(request, 'pay/balance.html', context)


# Суда приходят данные с URL оповещения. Вот тут и проблема в том что в переменную amount ничего не присваивается.
def payment_alerts(request):
    print(request)
    current_user = UserName.objects.create(name="Joe2")
    current_user.save()
    # amount = request.GET.get("AMOUNT")
    # current_user = UserProfile.objects.get(pk=request.user.id)
    # current_user.balance = current_user.balance + amount
    # current_user.save()


# При успешной оплате
def payment_success(request):
    current_user = UserName.objects.create(name="Joe")
    current_user.save()
    return render(request, 'pay/success.html')


# При ошибке в оплате
def payment_error(request):
    return render(request, 'pay/error.html')