from django import forms
from django.contrib import admin
from .models import Gen, Creature


class CreatureForm(forms.ModelForm):
    class Meta:
        model = Creature
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['father'].widget.can_add_related = False
        self.fields['mother'].widget.can_add_related = False


class GenAdmin(admin.ModelAdmin):
    list_display = ('name', 'rank', 'type')


class CreatureAdmin(admin.ModelAdmin):
    form = CreatureForm
    list_display = ('name', 'father', 'mother', 'rank', 'type')


admin.site.register(Gen, GenAdmin)
admin.site.register(Creature, CreatureAdmin)
