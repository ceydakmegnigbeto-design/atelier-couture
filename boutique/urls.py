from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.accueil,
        name='accueil'
    ),

    path(
        'creation/<int:creation_id>/',
        views.detail_creation,
        name='detail_creation'
    ),

    path(
        'commander/<int:creation_id>/',
        views.commander,
        name='commander'
    ),

    path(
        'confirmation/<int:commande_id>/',
        views.confirmation,
        name='confirmation'
    ),
path(
    'contact/',
    views.contact,
    name='contact'
),

path(
    'contact/confirmation/',
    views.contact_confirmation,
    name='contact_confirmation'
),
]