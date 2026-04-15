# Django'nun shortcut araçlarını içe aktarıyoruz.
# render  -> template göstermek için
# redirect -> işlem sonrası başka sayfaya yönlendirmek için
# get_object_or_404 -> veri bulunamazsa hata yerine 404 döndürmek için
from django.shortcuts import render, redirect, get_object_or_404

# Kullanıcı giriş yapmadan bu view'lara erişemesin diye kullanıyoruz.
from django.contrib.auth.decorators import login_required

# Sepete eklenecek ürünü bulmak için Product modelini içe aktarıyoruz.
from products.models import Product

# Sepet verisini tutan CartItem modelini içe aktarıyoruz.
from .models import CartItem


# Kullanıcı giriş yapmadan sepete ürün ekleyemez.
@login_required
def add_to_cart(request, product_id):
    # URL'den gelen product_id ile ilgili ürünü veritabanında buluyoruz.
    # Eğer ürün yoksa 404 hatası döner.
    product = get_object_or_404(Product, id=product_id)

    # Aynı kullanıcı + aynı ürün için sepette kayıt var mı diye bakıyoruz.
    # Varsa o kaydı getirir.
    # Yoksa yeni CartItem oluşturur.
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    # Eğer created False ise demek ki bu ürün zaten sepette var.
    # Bu durumda yeni satır açmak yerine quantity artırıyoruz.
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # İşlem bittikten sonra kullanıcıyı sepet detay sayfasına yönlendiriyoruz.
    return redirect('cart:cart_detail')


# Kullanıcı giriş yapmadan kendi sepetini göremez.
@login_required
def cart_detail(request):
    # Sadece giriş yapan kullanıcıya ait sepet ürünlerini getiriyoruz.
    cart_items = CartItem.objects.filter(user=request.user)

    # Sepetteki tüm ürünlerin satır toplamlarını topluyoruz.
    # item.get_total_price() = ürün_fiyatı * adet
    total_price = sum(item.get_total_price() for item in cart_items)

    # Template'e göndereceğimiz verileri context içinde hazırlıyoruz.
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }

    # cart/detail.html sayfasını bu verilerle birlikte render ediyoruz.
    return render(request, 'cart/detail.html', context)


# Kullanıcı giriş yapmadan adet artıramaz.
@login_required
def increase_cart_item(request, cart_item_id):
    # Burada ürünün id'sini değil, sepet satırının id'sini kullanıyoruz.
    # Ayrıca güvenlik için bu cart item'ın giriş yapan kullanıcıya ait olduğunu da kontrol ediyoruz.
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)

    # Adedi 1 artırıyoruz.
    cart_item.quantity += 1
    cart_item.save()

    # İşlemden sonra tekrar sepet detay sayfasına dönüyoruz.
    return redirect('cart:cart_detail')


# Kullanıcı giriş yapmadan adet azaltamaz.
@login_required
def decrease_cart_item(request, cart_item_id):
    # Yine sepet satırını hem id ile hem de kullanıcıya ait olması şartıyla buluyoruz.
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)

    # Eğer adet 1'den büyükse bir azaltıyoruz.
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        # Eğer adet zaten 1 ise 0 yapmıyoruz.
        # Bunun yerine sepet satırını tamamen siliyoruz.
        cart_item.delete()

    # İşlemden sonra tekrar sepet sayfasına dönüyoruz.
    return redirect('cart:cart_detail')


# Kullanıcı giriş yapmadan ürünü sepetten silemez.
@login_required
def remove_cart_item(request, cart_item_id):
    # Sadece kendi sepetindeki satırı silebilsin diye kullanıcı kontrolü yapıyoruz.
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)

    # Sepet satırını tamamen siliyoruz.
    cart_item.delete()

    # İşlemden sonra tekrar cart detail sayfasına dönüyoruz.
    return redirect('cart:cart_detail')