from django.urls import path
from age.views import yosh_hisoblash_view

urlpatterns = [
    path('', yosh_hisoblash_view, name='home'),
]
