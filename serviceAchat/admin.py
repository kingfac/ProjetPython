from django.contrib import admin
from serviceAchat.models import Produit2
from serviceAchat.models import apropos
from serviceAchat.models import panier
class AdminProduit(admin.ModelAdmin):
    list_display= ('nom','posologie','prix')


admin.site.register(Produit2,AdminProduit)
admin.site.register(apropos)
admin.site.register(panier)