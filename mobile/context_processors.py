from django.db.models import Sum
from .models import Cart
def cart_total(request):
    total=Cart.objects.filter(user_id=request.user.id).aggregate(total=Sum("quantity"))["total"] or 0
    return {"cart_total":total}
def is_user_logged(request):
    if request.user.id is None:
        return {"is_user_logged": 0}
    else:
        return {"is_user_logged": 1}
