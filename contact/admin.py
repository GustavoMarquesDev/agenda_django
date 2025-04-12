from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):

    # campos que estarão disponiveis na listagem
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show',)

    # campos que estarão disponiveis para filtro
    search_fields = ('first_name', 'last_name', 'phone', 'email')

    # ordenação dos campos decrescente
    ordering = ('-id',)

    # list_filter = ('created_date',)

    # contatos exibidos por página
    list_per_page = 10

    # ou um valor arbitrario como 200
    list_max_show_all = False

    # campos que podem ser editados direto na listagem
    list_editable = ('first_name', 'last_name', 'show')

    # campos que sao links que abrem para editar o contato
    list_display_links = ('id', 'phone')


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
    ordering = '-id',
