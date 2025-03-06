from django.urls import path
from . import views

app_name = 'cashflow_app'

urlpatterns = [
    # Главная страница
    path('', views.CashFlowRecordListView.as_view(), name='record_list'),

    # CRUD для статусов
    path('statuses/', views.StatusListView.as_view(), name='status_list'),
    path('status/add/', views.StatusCreateView.as_view(), name='status_add'),
    path('status/edit/<int:pk>/', views.StatusUpdateView.as_view(), name='status_edit'),
    path('status/delete/<int:pk>/', views.StatusDeleteView.as_view(), name='status_delete'),

    # CRUD для типов транзакций
    path('transaction_types/', views.TransactionTypeListView.as_view(), name='transactiontype_list'),
    path('transaction_type/add/', views.TransactionTypeCreateView.as_view(), name='transactiontype_add'),
    path('transaction_type/edit/<int:pk>/', views.TransactionTypeUpdateView.as_view(), name='transactiontype_edit'),
    path('transaction_type/delete/<int:pk>/', views.TransactionTypeDeleteView.as_view(), name='transactiontype_delete'),

    # CRUD для категорий
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('category/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('category/edit/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # CRUD для подкатегорий
    path('subcategories/', views.SubCategoryListView.as_view(), name='subcategory_list'),
    path('subcategory/add/', views.SubCategoryCreateView.as_view(), name='subcategory_add'),
    path('subcategory/edit/<int:pk>/', views.SubCategoryUpdateView.as_view(), name='subcategory_edit'),
    path('subcategory/delete/<int:pk>/', views.SubCategoryDeleteView.as_view(), name='subcategory_delete'),
]
