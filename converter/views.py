from django.shortcuts import render
import requests
from .models import ConversationHistory
# Create your views here.
def convert_currency(request):
    api_key="a349923ae41cdde6b6e69adb"
    api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    print(request.user.id)
    cuurencies=['USD','EUR','SAR','GPB','JPY','CAD']
   
    if request.method=='POST':
        amount=float(request.POST.get('amount'))
        from_currency=request.POST.get('from_currency')
        to_currency=request.POST.get('to_currency')
        print(ConversationHistory.objects.filter(user_id = request.user.id).order_by('-date')[:5])
        response=requests.get(api_url) 
        data=response.json()
        response.status_code
        data['result']
        if response.status_code == 200 and data['result'] == 'success':
                rates=data['conversion_rates']
                if from_currency != 'USD':
                    amount_in_usd=amount/rates[from_currency]
                else:
                    amount_in_usd=amount
                converted_amount=amount_in_usd * rates[to_currency]

                ConversationHistory.objects.create(

                    amount=amount,
                    from_currency=from_currency,
                    to_currency=to_currency,
                    converted_amount=converted_amount,
                    user_id = request.user.id

                )


                context={
                    'currency':cuurencies,
                    'amount':amount,
                    'from_currency':from_currency,
                    'to_currency':to_currency,
                    'converted_amount':round(converted_amount,2),
                    'history':ConversationHistory.objects.filter(user_id = request.user.id).order_by('-date')[:5]
                }
        
        else:
            
            context={
                
                'currency':cuurencies,
                'error':'فشل جلب اسعار الصرف نرجو المحاولة لاحقاً'
            
            }
            return render(request,'index.html',context)

    else:
          context={
                
                'currency':cuurencies,
                'history':ConversationHistory.objects.filter(user_id = request.user.id).order_by('-date')[:5]
            
            }
    if request.user.id is None:
         context['history'] = None
    return render(request,'converter/templates/index.html',context)