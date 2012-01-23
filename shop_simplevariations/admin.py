#-*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.admin.options import TabularInline, ModelAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.utils.translation import ugettext_lazy as _
from nani.admin import TranslatableAdmin, TranslatableTabularInline
from shop_simplevariations.models import Option, OptionGroup, TextOption

class OptionInline(TranslatableTabularInline):
    model = Option

class OptionGroupAdmin(TranslatableAdmin):
    inlines = [OptionInline,]
    #prepopulated_fields = {"slug": ("name",)} # not supported in hvad yet
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple(
            verbose_name=_('products'),
            is_stacked=False
            )},
    }

admin.site.register(OptionGroup, OptionGroupAdmin)

class TextOptionAdmin(TranslatableAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple(
            verbose_name=_('products'),
            is_stacked=False
            )},
    }

admin.site.register(TextOption, TextOptionAdmin)
