from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome),
    path('plant/', views.plant),
    path('plant_tree/', views.plant_tree),
    path('edit/<int:tree_id>', views.show_edit_page),
    path('edit_tree/<int:tree_id>', views.edit_tree),
    path('show_tree/<int:id>', views.show_tree),
    path('add_to_visited/<int:tree_id>', views.add_to_visited),
    path('account', views.user_dash),
    path('delete/<int:tree_id>', views.delete_tree),
    path('logout', views.log_out)
]
