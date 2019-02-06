from authapp.models import Customer
from authapp.forms import CustomerRegisterForm
from adminapp.forms import CustomerAdminEditForm, ProductCategoryEditForm, ProductEditForm, CompanyEditForm
from django.shortcuts import get_object_or_404, render
from mainapp.models import Product, ProductCategory, Company
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.core.files.images import ImageFile

from django.http import HttpResponse
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from dobryidomshop import settings
import csv
import os

def index(request):
    title = 'Администрирование'

    content = {
        'title': title,

    }
    return render(request, 'adminapp/index.html', content)


class CompaniesListView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Администрирование/Список организаций'
        return context

    model = Company
    success_url = reverse_lazy('admin:companies')
    template_name = 'adminapp/companies.html'


class CompanyCreateView(CreateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Администрирование/Добавление организации'
        return context

    model = Company
    form_class = CompanyEditForm
    success_url = reverse_lazy('admin:companies')
    template_name = 'adminapp/company_update.html'


class CompanyUpdateView(UpdateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Администрирование/Редактирование организации'
        return context

    model = Company
    form_class = CompanyEditForm
    success_url = reverse_lazy('admin:companies')
    template_name = 'adminapp/company_update.html'


class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('admin:companies')
    template_name = 'adminapp/company_delete.html'


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'Администрирование/Клиенты'

    users_list = Customer.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/customers.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'Пользователи/Создание'

    if request.method == 'POST':
        user_form = CustomerRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('adminapp:users'))
    else:
        user_form = CustomerRegisterForm()

    content = {'title': title, 'update_form': user_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'Пользователи/Редактирование'

    edit_user = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        edit_form = CustomerAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:user_update', args=[edit_user.pk]))
    else:
        edit_form = CustomerAdminEditForm(instance=edit_user)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/user_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    title = 'Пользователи/Удаление'

    user = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':

        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('adminapp:users'))

    content = {'title': title, 'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def user_restore(request, pk):
    title = 'Пользователи/Восстановление'

    user = get_object_or_404(Customer, pk=pk)

    if request.method == 'POST':

        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse('adminapp:users'))

    content = {'title': title, 'user_to_restore': user}

    return render(request, 'adminapp/user_restore.html', content)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'Администрирование/Категории'

    categories_list = ProductCategory.objects.all().order_by('-is_active', 'name')

    content = {
        'title': title,
        'objects': categories_list
    }

    return render(request, 'adminapp/categories.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    title = 'Категории/Создание'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('adminapp:categories'))
    else:
        category_form = ProductCategoryEditForm()

    content = {'title': title, 'update_form': category_form}

    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_update(request, pk):
    title = 'Категории/Редактирование'

    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('adminapp:category_update', args=[edit_category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/category_update.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk):
    title = 'Категории/Удаление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':

        category.is_active = False
        category.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    content = {'title': title, 'category_to_delete': category}

    return render(request, 'adminapp/category_delete.html', content)


@user_passes_test(lambda u: u.is_superuser)
def category_restore(request, pk):
    title = 'Категории/Восстановление'

    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':

        category.is_active = True
        category.save()
        return HttpResponseRedirect(reverse('adminapp:categories'))

    content = {'title': title, 'category_to_restore': category}

    return render(request, 'adminapp/category_restore.html', content)


def products(request, pk):
    title = 'Администрирование/Товары'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)


class ProductCategoryListView(ListView):

    def get_queryset(self):
        return Product.objects.filter(category__pk=int(self.kwargs['pk']))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = ProductCategory.objects.get(pk=int(self.kwargs['pk']))
        return context

    template_name = 'adminapp/products_of_category.html'


class ProductsListView(ListView):

    model = Product
    template_name = 'adminapp/products.html'
    paginate_by = 2
    queryset = Product.objects.all()



def product_create(request, pk):
    pass


class ProductCreateView(CreateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Администрирование/Добавление товара'
        return context

    form_class = ProductEditForm
    template_name = 'adminapp/product_update.html'
    success_url = reverse_lazy('adminapp:products_all')


class ProductUpdateView(UpdateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Администрирование/Редактирование товара'
        return context

    model = Product
    form_class = ProductEditForm
    success_url = reverse_lazy('adminapp:products_all')
    template_name = 'adminapp/product_update.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_detail.html'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'
    success_url = reverse_lazy('adminapp:products_all')


def product_read(request, pk):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass


def import_products_from_csv(request):
    csv_file = os.path.join(settings.BASE_DIR, "products.csv")
    with open(csv_file, "r") as input_file:
        product_list = csv.DictReader(input_file, delimiter=',')
        product_list = list(product_list)
        for producto in product_list:
            new_product=''
            producto = dict(producto)
            category = ProductCategory.objects.get(name=producto['category'])
            img_path =str(producto['image_path'])[1:]
            print(img_path)
            with open(img_path, "rb") as img_file:
                image = ImageFile(img_file)
            new_product = Product(category=category, name=producto['name'], image=image, old_price=producto['old_price'])
            new_product.save()
    return HttpResponseRedirect(reverse('adminapp:products_all'))

# Сохранение продуктов в файл на сервер
def export_products_to_csv(request):
    fieldnames = ['name', 'old_price', 'category','image_url']
    output = os.path.join(settings.BASE_DIR, "products.csv")
    with open(output, "w", newline='') as out_file:

        writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()
        data = Product.objects.all()
        for row in data:
            writer.writerow(rowdict={'name': row.name, 'old_price': row.old_price, 'category': row.category.name, 'image_url': row.image.url})

    return HttpResponseRedirect(reverse('adminapp:products_all'))

