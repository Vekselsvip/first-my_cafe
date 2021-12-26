from django.shortcuts import render, redirect
from .models import CategoryDish, Dish, HeroSection, AboutSection
from .forms import FormRegistration, FormMessage


def base_app_view(request):
    if request.method == 'POST':
        form = FormRegistration(request.POST)
        form_ = FormMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        if form_.is_valid():
            form_.save()
            return redirect('/')
    form_registration = FormRegistration()
    form_reg_message = FormMessage()
    category = CategoryDish.objects.filter(is_visible=True).order_by('position')
    dish = Dish.objects.filter(is_visible=True, is_special=False).order_by('dish_order')
    special = Dish.objects.filter(is_visible=True, is_special=True).order_by('dish_order')
    hero_section = HeroSection.objects.all()
    about_section = AboutSection.objects.all()
    return render(request, 'base_app.html', context={
        'category': category,
        'dish': dish,
        'special': special,
        'form_registration': form_registration,
        'hero_section': hero_section,
        'about_section': about_section,
        'form_reg_message': form_reg_message,
        })

