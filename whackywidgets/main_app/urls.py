from django.urls import path
from . import views

urlpatterns = [
    # widget index
    path('', views.widget_index, name='widget_index'),

    # widget form
    path('widgets/add_widget', views.add_widget, name='add_widget'),

    # delete widget
    path('widgets/<int:widget_id>/delete/',
         views.widget_delete, name='widget_delete'),

]
