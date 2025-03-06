from django.contrib import admin
from .models import Status, TransactionType, Category, SubCategory, CashFlowRecord

admin.site.site_header = "Управление движением денежных средств"
admin.site.index_title = "Администрирование системы"
admin.site.site_title = "ДДС"

admin.site.register(Status)
admin.site.register(TransactionType)

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'transaction_type')

@admin.register(CashFlowRecord)
class CashFlowRecordAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'status', 'transaction_type', 'category', 'subcategory', 'amount')
    list_filter = ('date_created', 'status', 'transaction_type', 'category', 'subcategory')
    search_fields = ('comment',)

admin.site.register(SubCategory)

