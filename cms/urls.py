from django.urls import path
from cms import views

app_name = 'cms'

urlpatterns = [
    # Habit
    path('habit/', views.habit_list, name='habit_list'),
    path('habit/add/', views.habit_edit, name='habit_add'),
    path('habit/mod/<int:habit_id>/', views.habit_edit, name='habit_mod'),
    path('habit/del/<int:habit_id>/', views.habit_del, name='habit_del'),

    # Record
    path('record/<int:habit_id>/', views.RecordList.as_view(), name='record_list'),
    path('record/add/<int:habit_id>/', views.record_edit, name='record_add'),
    path('record/mod/<int:habit_id>/<int:record_id>/', views.record_edit, name='record_mod'),
    path('record/del/<int:habit_id>/<int:record_id>/', views.record_del, name='record_del'),

]
