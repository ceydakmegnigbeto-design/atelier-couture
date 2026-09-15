from django.db import models


class Creation(models.Model):
    CATEGORIES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Enfant', 'Enfant'),
        ('Accessoire', 'Accessoire'),
    ]

    nom = models.CharField(max_length=150)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    categorie = models.CharField(
        max_length=30,
        choices=CATEGORIES,
        default='Femme'
    )

    image = models.ImageField(upload_to='creations/')
    disponible = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    class MessageContact(models.Model):
     nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=30, blank=True)
    sujet = models.CharField(max_length=150)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"
    creation = models.ForeignKey(
        Creation,
        on_delete=models.CASCADE,
        related_name='commandes'
    )

    nom_client = models.CharField(max_length=100)
    telephone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    taille = models.CharField(max_length=20)
    couleur = models.CharField(max_length=50)
    mesures = models.TextField(blank=True)
    message = models.TextField(blank=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    traitee = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom_client} - {self.creation.nom}"
class MessageContact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=30, blank=True)
    sujet = models.CharField(max_length=150)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    lu = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"
    