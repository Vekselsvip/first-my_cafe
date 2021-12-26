from django.contrib import admin
from .models import CategoryDish, Dish, HeroSection, AboutSection, ModelFormRegistration, ModelFormMessage


class DishAdmin(admin.TabularInline):
    model = Dish
    row_id_fields = ['name']


@admin.register(CategoryDish)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visible', 'position']
    list_filter = ['is_visible']
    inlines = [DishAdmin]


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image']


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title_1', 'desc_1', 'feature_1']


admin.site.register(ModelFormRegistration)
admin.site.register(ModelFormMessage)
