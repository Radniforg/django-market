from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cart, Category, Article, \
    Product, Order, CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',
                       'is_staff', 'is_active')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


class RelationshipInline(admin.TabularInline):
    model = Cart
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "creation", "status", "total")
    readonly_fields = ("id", "user", "creation", "status", "total")
    inlines = [RelationshipInline]

    def has_add_permission(self, request, obj=None):
        return False
