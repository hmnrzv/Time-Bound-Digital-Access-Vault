from django.urls import path
from . import views

urlpatterns=[
    path('', views.main, name='main'),
    path('view_vault_items/', views.view_vault_items, name='view_vault_items'),
    path('create_vault_item/', views.create_vault_item, name='create_vault_item'),
    path('create_share_link_rules/', views.create_share_link_rules, name='create_share_link_rules'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register', views.register_user, name='register')
]