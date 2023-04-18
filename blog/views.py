from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from serviceAchat.models import Produit2
from serviceAchat.models import apropos
from authentification.models import User
from serviceAchat.models import panier

@login_required
def home(request):
    abouts=apropos.objects.all()
    produits=Produit2.objects.all()
    return render(request, 'blog/home.html',{'produits':produits,'apropos':abouts})

def detail_produit(request,produit_id):
    produit = Produit2.objects.get(id=produit_id)
    
    return render(
        request,
        'blog/components/detailProduit.html',
        {'produit': produit}
    )
# def panier(request,produit_id,user_id):
#     produit_id= Produit2.objects.get(id=produit_id)
#     User=User.objects.get(username=user_id)
#     p=panier(user=User,produit_id=produit_id,quantite=5)
#     p.save()
#     return render(request, 'blog/home.html')