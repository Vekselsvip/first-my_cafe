from django.shortcuts import render
from base_app.models import ModelFormMessage
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator


def is_manager(user):
    return user.groups.filter(name='manager').exists()


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def message_list(request):
    message = ModelFormMessage.objects.filter(is_processed=False).order_by('-id')
    return render(request, 'send_message.html', context={'message': message})
