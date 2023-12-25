from django.contrib import admin
from .models import Function


@admin.action(description='Обновить')
def update_functions(modeladmin, request, queryset):
    queryset.update()


@admin.register(Function)
class FunctionAdmin(admin.ModelAdmin):
    list_display = ('statement', 'image_tag', 'interval', 'dt', 'creation_date')
    actions = [update_functions]
    # fields = ('image_tag', )
    readonly_fields = ('image_tag', )
