from django.shortcuts import render, redirect
from .models import Widget
from django.views.generic import ListView
from .forms import WidgetForm
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Sum


def widget_index(request):
    total_quantity = Widget.objects.aggregate(
        total_quantity=Sum('quantity')).get('total_quantity')
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'widgets/index.html', {'widgets': widgets, 'widget_form': widget_form, 'total_quantity': total_quantity})


def widget_delete(request, widget_id):
    w = Widget.objects.get(id=widget_id)
    w.delete()
    return redirect('widget_index')


def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    return redirect('widget_index')
