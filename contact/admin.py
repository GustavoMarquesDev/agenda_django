from django.contrib import admin
from contact import models


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):

    # campos que estarão disponiveis na listagem
    list_display = ('id', 'first_name', 'last_name',
                    'phone', 'email', 'created_date')

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
    # list_editable = ('first_name', 'last_name', 'phone', 'email')

    # campos que sao links que abrem para editar o contato
    list_display_links = ('first_name', 'last_name')
