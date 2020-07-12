from django.urls import path
from . import views

urlpatterns = [
    path('', views.widget_index, name='widget_index'),

    # widget form
    path('widgets/add_widget', views.add_widget, name='add_widget'),
    # create widget
    path('widgets/create/', views.WidgetCreate.as_view(), name='widget_create'),

    path('widgets/<int:widget_id>/delete/',
         views.widget_delete, name='widget_delete'),

    # path('widgets/<int:pk>/delete/',
    #      views.WidgetDelete.as_view(), name='widget_delete'),

]
