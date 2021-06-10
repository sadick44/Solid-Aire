from django.contrib import admin
from . models import Products, Offer, Registration


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


class OfferAdmin(admin.ModelAdmin):
    list_display = ("code", "discount")


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "stock")


admin.site.register(Products, ProductsAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Registration, RegistrationAdmin)