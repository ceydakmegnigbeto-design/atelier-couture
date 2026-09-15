from urllib.parse import quote

from django.contrib import admin
from django.utils.html import format_html

from .models import Commande, Creation, MessageContact


@admin.register(Creation)
class CreationAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'categorie',
        'prix',
        'disponible',
        'date_creation',
    )

    list_filter = (
        'categorie',
        'disponible',
        'date_creation',
    )

    search_fields = (
        'nom',
        'description',
    )


@admin.register(Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = (
        'nom_client',
        'telephone',
        'creation',
        'taille',
        'couleur',
        'traitee',
        'date_commande',
        'whatsapp',
    )

    list_filter = (
        'traitee',
        'date_commande',
    )

    search_fields = (
        'nom_client',
        'telephone',
        'email',
    )

    readonly_fields = (
        'date_commande',
        'whatsapp',
    )

    def whatsapp(self, obj):
        numero_atelier = '2290193903638'

        message = (
            f"Bonjour {obj.nom_client}, "
            f"nous avons bien reçu votre demande pour "
            f"{obj.creation.nom}. "
            f"Nous allons vous contacter prochainement."
        )

        lien = (
            f"https://wa.me/2290193903638"
            f"?text={quote(message)}"
        )

        return format_html(
            '<a href="{}" target="_blank">'
            'Contacter sur WhatsApp'
            '</a>',
            lien
        )

    whatsapp.short_description = 'WhatsApp'


@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'email',
        'telephone',
        'sujet',
        'lu',
        'date_envoi',
    )

    list_filter = (
        'lu',
        'date_envoi',
    )

    search_fields = (
        'nom',
        'email',
        'telephone',
        'sujet',
        'message',
    )

    readonly_fields = (
        'date_envoi',
    )