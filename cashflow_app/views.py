from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Status, TransactionType, Category, SubCategory
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import CashFlowRecord, SubCategory
from .forms import CashFlowRecordForm
from django.http import JsonResponse
from django.views.generic import ListView
from .models import CashFlowRecord
from django.views.generic.edit import DeleteView


class CashFlowRecordListView(ListView):
    model = CashFlowRecord
    template_name = 'cashflow_app/record_list.html'
    context_object_name = 'records'


class CashFlowRecordCreateView(CreateView):
    model = CashFlowRecord
    form_class = CashFlowRecordForm
    template_name = 'cashflow_app/record_form.html'
    success_url = reverse_lazy('cashflow_app:record_list')

class CashFlowRecordUpdateView(UpdateView):
    model = CashFlowRecord
    form_class = CashFlowRecordForm
    template_name = 'cashflow_app/record_form.html'
    success_url = reverse_lazy('cashflow_app:record_list')
class CashFlowRecordDeleteView(DeleteView):
    model = CashFlowRecord
    template_name = 'cashflow_app/record_confirm_delete.html'
    success_url = reverse_lazy('cashflow_app:record_list')
class StatusListView(ListView):
    model = Status
    template_name = 'cashflow_app/status_list.html'

class StatusCreateView(CreateView):
    model = Status
    fields = ['name']
    template_name = 'cashflow_app/status_form.html'
    success_url = reverse_lazy('cashflow_app:status_list')

class StatusUpdateView(UpdateView):
    model = Status
    fields = ['name']
    template_name = 'cashflow_app/status_form.html'
    success_url = reverse_lazy('cashflow_app:status_list')

class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'cashflow_app/status_confirm_delete.html'
    success_url = reverse_lazy('cashflow_app:status_list')

class TransactionTypeListView(ListView):
    model = TransactionType
    template_name = 'cashflow_app/transactiontype_list.html'

class TransactionTypeCreateView(CreateView):
    model = TransactionType
    fields = ['name']
    template_name = 'cashflow_app/transactiontype_form.html'
    success_url = reverse_lazy('cashflow_app:transactiontype_list')

class TransactionTypeUpdateView(UpdateView):
    model = TransactionType
    fields = ['name']
    template_name = 'cashflow_app/transactiontype_form.html'
    success_url = reverse_lazy('cashflow_app:transactiontype_list')

class TransactionTypeDeleteView(DeleteView):
    model = TransactionType
    template_name = 'cashflow_app/transactiontype_confirm_delete.html'
    success_url = reverse_lazy('cashflow_app:transactiontype_list')

# --- Категории ---
class CategoryListView(ListView):
    model = Category
    template_name = 'cashflow_app/category_list.html'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'transaction_type']
    template_name = 'cashflow_app/category_form.html'
    success_url = reverse_lazy('cashflow_app:category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'transaction_type']
    template_name = 'cashflow_app/category_form.html'
    success_url = reverse_lazy('cashflow_app:category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'cashflow_app/category_confirm_delete.html'
    success_url = reverse_lazy('cashflow_app:category_list')

# --- Подкатегории ---
class SubCategoryListView(ListView):
    model = SubCategory
    template_name = 'cashflow_app/subcategory_list.html'

class SubCategoryCreateView(CreateView):
    model = SubCategory
    fields = ['name', 'category']
    template_name = 'cashflow_app/subcategory_form.html'
    success_url = reverse_lazy('cashflow_app:subcategory_list')

class SubCategoryUpdateView(UpdateView):
    model = SubCategory
    fields = ['name', 'category']
    template_name = 'cashflow_app/subcategory_form.html'
    success_url = reverse_lazy('cashflow_app:subcategory_list')

class SubCategoryDeleteView(DeleteView):
    model = SubCategory
    template_name = 'cashflow_app/subcategory_confirm_delete.html'
    success_url = reverse_lazy('cashflow_app:subcategory_list')
# AJAX-представление для подгрузки подкатегорий
def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)
