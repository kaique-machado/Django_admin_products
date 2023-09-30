from django.contrib import admin
from .models import categoria, produto


@admin.register(categoria)
class categoriAdmin(admin.ModelAdmin):
    pass


@admin.register(produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("nome", "preço", "descrição", "categoria")
    list_filter = ("categoria",)
    list_editable = ("preço", "categoria")
    list_display_links = ("nome", "descrição")
    search_fields = ("nome", "descrição")
