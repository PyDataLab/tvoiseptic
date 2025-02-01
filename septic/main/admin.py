from django.contrib import admin
from .models import (
    MetaContent,
    SideBar,
    Header,
    Menu,
    MainContent,
    Add,
    Quiz,
    Category,
    ModelStatic,
    ModelDynamic,
    Catalog,
    Budget,
    Guarantees,
    More,
    Portfolio,
    Video,
    Reviews,
    Install, Numbers, Quality, Faq, Requisition, Contacts, Footer, PopupRequest, PopupStock, PopupPolitic, PopupLeave)


@admin.register(MetaContent)
class MetaContentAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ('engineer_text', 'price_text', 'whatsapp_text')

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ('header_text1', 'phone_number')

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('main_link', 'main_link_text')

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(MainContent)
class MainContentAdmin(admin.ModelAdmin):
    list_display = ('text_1',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Add)
class AddAdmin(admin.ModelAdmin):
    list_display = ('add_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_header',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('header',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(ModelStatic)
class ModelStaticAdmin(admin.ModelAdmin):
    list_display = ('wa_link_s',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(ModelDynamic)
class ModelDynamicAdmin(admin.ModelAdmin):
    list_display = ('name_d', 'manufacturer_number_d', 'model_number_d',)
    readonly_fields = ('manufacturer_number_d', 'model_number_d',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('title_h2',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Guarantees)
class GuaranteesAdmin(admin.ModelAdmin):
    list_display = ('text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(More)
class MoreAdmin(admin.ModelAdmin):
    list_display = ('text1',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('header_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('header_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('header_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Install)
class InstallAdmin(admin.ModelAdmin):
    list_display = ('header_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Numbers)
class NumbersAdmin(admin.ModelAdmin):
    list_display = ('title1',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Quality)
class QualityAdmin(admin.ModelAdmin):
    list_display = ('header_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('header_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Requisition)
class RequisitionAdmin(admin.ModelAdmin):
    list_display = ('header_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('header_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('text1',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(PopupRequest)
class PopupRequestAdmin(admin.ModelAdmin):
    list_display = ('title',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(PopupStock)
class PopupStockAdmin(admin.ModelAdmin):
    list_display = ('header',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(PopupPolitic)
class PopupPoliticAdmin(admin.ModelAdmin):
    list_display = ('full_text',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей

@admin.register(PopupLeave)
class PopupLeaveAdmin(admin.ModelAdmin):
    list_display = ('header',)

    def has_add_permission(self, request):
        return False  # Запрещаем добавление новых записей

    def has_delete_permission(self, request, obj=None):
        return False  # Запрещаем удаление записей