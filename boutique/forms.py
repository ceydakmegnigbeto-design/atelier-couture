from django import forms
from .models import Commande, MessageContact


class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande

        fields = [
            'nom_client',
            'telephone',
            'email',
            'taille',
            'couleur',
            'mesures',
            'message',
        ]

        labels = {
            'nom_client': 'Nom complet',
            'telephone': 'Téléphone',
            'email': 'Adresse email',
            'taille': 'Taille',
            'couleur': 'Couleur souhaitée',
            'mesures': 'Mesures',
            'message': 'Message complémentaire',
        }

        widgets = {
            'nom_client': forms.TextInput(attrs={
                'placeholder': 'Exemple : Jean Dupont'
            }),

            'telephone': forms.TextInput(attrs={
                'placeholder': '+229 XX XX XX XX'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'exemple@email.com'
            }),

            'taille': forms.TextInput(attrs={
                'placeholder': 'Exemple : M, L, XL'
            }),

            'couleur': forms.TextInput(attrs={
                'placeholder': 'Exemple : bleu marine'
            }),

            'mesures': forms.Textarea(attrs={
                'placeholder': 'Tour de poitrine, taille, longueur...',
                'rows': 4
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Précisions concernant votre commande',
                'rows': 4
            }),
        }
class MessageContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact

        fields = [
            'nom',
            'email',
            'telephone',
            'sujet',
            'message',
        ]

        labels = {
            'nom': 'Nom complet',
            'email': 'Adresse email',
            'telephone': 'Téléphone',
            'sujet': 'Sujet',
            'message': 'Votre message',
        }

        widgets = {
            'nom': forms.TextInput(attrs={
                'placeholder': 'Votre nom'
            }),

            'email': forms.EmailInput(attrs={
                'placeholder': 'exemple@email.com'
            }),

            'telephone': forms.TextInput(attrs={
                'placeholder': '+229 XX XX XX XX'
            }),

            'sujet': forms.TextInput(attrs={
                'placeholder': 'Sujet de votre message'
            }),

            'message': forms.Textarea(attrs={
                'placeholder': 'Écrivez votre message...',
                'rows': 6
            }),
        }