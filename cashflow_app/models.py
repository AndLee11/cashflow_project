from django.db import models
from django.utils import timezone

class Status(models.Model):
    name = models.CharField("Статус", max_length=100)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name

class TransactionType(models.Model):
    name = models.CharField("Тип транзакции", max_length=100)

    class Meta:
        verbose_name = "Тип транзакции"
        verbose_name_plural = "Типы транзакций"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField("Категория", max_length=100)
    transaction_type = models.ForeignKey(TransactionType, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name} ({self.transaction_type.name})"

class SubCategory(models.Model):
    name = models.CharField("Подкатегория", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class CashFlowRecord(models.Model):
    date_created = models.DateField("Дата создания", default=timezone.now)
    status = models.ForeignKey(Status, verbose_name="Статус", on_delete=models.SET_NULL, null=True)
    transaction_type = models.ForeignKey(TransactionType, verbose_name="Тип транзакции", on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(SubCategory, verbose_name="Подкатегория", on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField("Сумма", max_digits=12, decimal_places=2)
    comment = models.TextField("Комментарий", blank=True, null=True)

    class Meta:
        verbose_name = "Запись о движении денежных средств"
        verbose_name_plural = "Записи о движении денежных средств"

    def __str__(self):
        return f"{self.date_created} | {self.transaction_type.name} | {self.amount} р."
