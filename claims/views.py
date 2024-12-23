from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reclamation
from .forms import ReclamationForm

@login_required
def reclamation_list(request):
    """
    Список рекламаций с фильтрацией/сортировкой.
    """
    qs = Reclamation.objects.select_related('machine').all()

    node_filter = request.GET.get('failure_node')
    if node_filter:
        qs = qs.filter(failure_node__icontains=node_filter)

    service_filter = request.GET.get('service')
    if service_filter:
        qs = qs.filter(service_company__icontains=service_filter)

    qs = qs.order_by('-failure_date')

    user_role = getattr(request.user, 'role', None)
    if user_role == 'client':
        qs = qs.filter(machine__client=request.user.username)
    elif user_role == 'service':
        qs = qs.filter(service_company=request.user.username)

    return render(request, 'claims/reclamation_list.html', {'records': qs})


@login_required
def reclamation_create(request):
    """
    Создание новой рекламации.
    По ТЗ сервисная организация может добавлять,
    клиент может только просматривать,
    менеджер — всё. (Регулируйте по задаче.)
    """
    user_role = getattr(request.user, 'role', None)
    if user_role == 'client':
        messages.error(request, "У вас нет прав создавать рекламации.")
        return redirect('reclamation-list')

    if request.method == 'POST':
        form = ReclamationForm(request.POST)
        if form.is_valid():
            rec_obj = form.save(commit=False)
            if user_role == 'service':
                if rec_obj.machine.service_company != request.user.username:
                    messages.error(request, "У вас нет прав добавлять для этой машины.")
                    return redirect('reclamation-list')
            rec_obj.save()
            messages.success(request, "Рекламация создана.")
            return redirect('reclamation-list')
    else:
        form = ReclamationForm()

    return render(request, 'claims/reclamation_create.html', {'form': form})


@login_required
def reclamation_edit(request, pk):
    rec_obj = get_object_or_404(Reclamation, pk=pk)
    user_role = getattr(request.user, 'role', None)

    if user_role == 'client':
        messages.error(request, "У вас нет прав редактировать рекламации.")
        return redirect('reclamation-list')
    elif user_role == 'service':
        if rec_obj.service_company != request.user.username:
            messages.error(request, "У вас нет прав на редактирование этой рекламации.")
            return redirect('reclamation-list')

    if request.method == 'POST':
        form = ReclamationForm(request.POST, instance=rec_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Изменения сохранены.")
            return redirect('reclamation-list')
    else:
        form = ReclamationForm(instance=rec_obj)

    return render(request, 'claims/reclamation_edit.html', {'form': form, 'rec_obj': rec_obj})
