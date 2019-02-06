import adminapp.views as adminapp
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),

    path('companies/read/', adminapp.CompaniesListView.as_view(), name='companies'),
    path('companies/create/', adminapp.CompanyCreateView.as_view(), name='company_create'),
    path('companies/update/<int:pk>', adminapp.CompanyUpdateView.as_view(), name='company_update'),
    path('companies/delete/<int:pk>', adminapp.CompanyDeleteView.as_view(), name='company_delete'),

    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.users, name='users'),
    path('users/update/<int:pk>/', adminapp.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),
    path('users/restore/<int:pk>/', adminapp.user_restore, name='user_restore'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),
    path('categories/restore/<int:pk>/', adminapp.category_restore, name='category_restore'),

    path('products/create/', adminapp.ProductCreateView.as_view(), name='product_create'),
    path('products/read/category/<int:pk>/', adminapp.ProductCategoryListView.as_view(), name='products_by_category'),
    path('products/all/', adminapp.ProductsListView.as_view(), name='products_all'),
    path('products/read/<int:pk>/', adminapp.ProductDetailView.as_view(), name='product_read'),
    path('products/update/<int:pk>/', adminapp.ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', adminapp.ProductDeleteView.as_view(), name='product_delete'),
    path('products/export-to-csv/', adminapp.export_products_to_csv, name="export_to_csv"),
    path('products/import-from-csv/', adminapp.import_products_from_csv, name="import_from_csv"),
]