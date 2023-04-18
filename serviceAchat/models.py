from django.db import models
from authentification.models import User

class Produit2(models.Model):
    nom = models.fields.CharField(max_length=100)
    description= models.fields.CharField(max_length=500)
    image=models.ImageField(upload_to='image',null=True,blank=True)
    prix=models.fields.IntegerField()
    posologie=models.fields.CharField(max_length=500)

    def __str__(self):
        return self.nom
    
class apropos(models.Model):
    description= models.fields.CharField(max_length=1000)

    def __str__(self):
        return self.description

class panier(models.Model):
    user= models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    produit_id=models.ForeignKey(Produit2, null=True, on_delete=models.SET_NULL)
    quantite= models.IntegerField()
    