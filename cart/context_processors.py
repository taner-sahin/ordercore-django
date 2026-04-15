from django.db.models import Sum
from .models import CartItem


def cart_item_count(request):
    if request.user.is_authenticated:
        result = CartItem.objects.filter(user=request.user).aggregate(total=Sum('quantity'))
        cart_count = result['total'] or 0
    else:
        cart_count = 0

    return {
        'cart_count': cart_count
    }