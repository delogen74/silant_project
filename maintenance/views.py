from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import TO
from .forms import TOForm
from machines.models import Machine

@login_required
def to_create(request, machine_id=None):
    """
    Создание новой записи ТО. Если передан machine_id, то подставляем машину автоматически.
    Иначе даём выбрать из списка.
    """
    if request.method == 'POST':
        form = TOForm(request.POST)
        if form.is_valid():
            to_obj = form.save(commit=False)

            user_role = getattr(request.user, 'role', None)
            if user_role == 'client':
                if to_obj.machine.client != request.user.username:
                    messages.error(request, "У вас нет прав создавать ТО для этой машины.")
                    return redirect('to-list')

            elif user_role == 'service':
                if to_obj.machine.service_company != request.user.username:
                    messages.error(request, "У вас нет прав создавать ТО для этой машины.")
                    return redirect('to-list')

            to_obj.save()
            messages.success(request, "ТО успешно добавлено.")
            return redirect('to-list')
    else:
        if machine_id:
            machine = get_object_or_404(Machine, pk=machine_id)
            form = TOForm(initial={'machine': machine})
        else:
            form = TOForm()

    return render(request, 'maintenance/to_create.html', {'form': form})

@login_required
def to_edit(request, pk):
    """
    Редактирование существующей записи ТО.
    """
    to_obj = get_object_or_404(TO, pk=pk)

    user_role = getattr(request.user, 'role', None)
    if user_role == 'client':
        if to_obj.machine.client != request.user.username:
            messages.error(request, "У вас нет прав редактировать эту запись ТО.")
            return redirect('to-list')
    elif user_role == 'service':
        if to_obj.service_company != request.user.username:
            messages.error(request, "У вас нет прав редактировать эту запись ТО.")
            return redirect('to-list')

    if request.method == 'POST':
        form = TOForm(request.POST, instance=to_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения сохранены.")
            return redirect('to-list')
    else:
        form = TOForm(instance=to_obj)

    return render(request, 'maintenance/to_edit.html', {'form': form})

@login_required
def to_list(request):
    """
    Список ТО с фильтром по сервисной компании, виду ТО и т. д.
    """
    qs = TO.objects.select_related('machine').all()

    service_filter = request.GET.get('service')
    if service_filter:
        qs = qs.filter(service_company__icontains=service_filter)

    to_type_filter = request.GET.get('to_type')
    if to_type_filter:
        qs = qs.filter(to_type__icontains=to_type_filter)

    qs = qs.order_by('-date_performed')

    # Разграничение по ролям:
    user_role = getattr(request.user, 'role', None)
    if user_role == 'client':
        qs = qs.filter(machine__client=request.user.username)
    elif user_role == 'service':
        qs = qs.filter(service_company=request.user.username)

    return render(request, 'maintenance/to_list.html', {'records': qs})
