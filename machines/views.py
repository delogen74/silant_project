from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Machine
from .forms import MachineForm
def guest_search(request):
    query = request.GET.get('factory_number')
    machine_found = None
    if query:
        try:
            machine_found = Machine.objects.get(factory_number=query)
        except Machine.DoesNotExist:
            machine_found = None
    return render(request, 'index_guest.html', {'machine_found': machine_found, 'query': query})

@login_required
def main_dashboard(request):
    """
    Страница /dashboard/, доступна только после логина.
    """
    return render(request, 'dashboard.html')

@login_required
def machines_list(request):
    """Список машин, доступный авторизованным пользователям."""
    all_machines = Machine.objects.all()

    return render(request, 'machines/machines_list.html', {
        'machines': all_machines
    })

@login_required
def machine_create(request):
    """
    Создание новой машины.
    """
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Машина успешно создана.")
            return redirect('machines-list')
    else:
        form = MachineForm()

    return render(request, 'machines/machine_create.html', {'form': form})

@login_required
def machine_edit(request, pk):
    machine_obj = get_object_or_404(Machine, pk=pk)
    if request.method == 'POST':
        form = MachineForm(request.POST, instance=machine_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения сохранены.")
            return redirect('machines-list')
    else:
        form = MachineForm(instance=machine_obj)

    return render(request, 'machines/machine_edit.html', {
        'form': form,
        'machine_obj': machine_obj
    })