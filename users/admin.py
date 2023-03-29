from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import NewUser, Favorite, Address, Cart

class AddressInline(admin.StackedInline):
    model = Address
    extra = 0

class FavoriteInline(admin.StackedInline):
    model = Favorite
    extra = 0

class CartInline(admin.StackedInline):
    model = Cart
    extra = 0


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ('email', 'username')
    list_filter = ('is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'is_active', 'is_block', 'is_staff')
    fieldsets = (
        ('User Information', {'fields': ('username', 'email', 'password')}),

        ('Permissions', {'fields': ('is_staff', 'is_block', 'is_active')}),

        ('Group Permissions', {
            'fields': ('groups', 'user_permissions',)
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_active', 'is_block', 'is_staff')
        }),
    )
    inlines = [
        AddressInline,
        FavoriteInline,
        CartInline,
    ]



class FavoriteAdminConfig(admin.ModelAdmin):
    model = Favorite
    search_fields = ('user', 'product',)
    list_filter = ('user', 'product',)
    list_display = ('user', 'product',)
    fieldsets = (
        ('Favorite Information', {'fields': ('user', 'product',)}),
    )


class AddressAdminConfig(admin.ModelAdmin):
    model = Address
    search_fields = ('user', 'phone_number',)
    list_filter = ('user', 'phone_number',)
    list_display = ('user', 'full_name', 'phone_number')
    fieldsets = (
        ('Address Information',
         {'fields': ('user', 'full_name', 'phone_number', 'building_number', 'street_name', 'apartment_number', 'city', 'landmark')}),
    )


class CartAdminConfig(admin.ModelAdmin):
    model = Cart
    search_fields = ('user', 'product',)
    list_filter = ('user', 'product', 'price',)
    list_display = ('user', 'product', 'items', 'price',)
    fieldsets = (
        ('Cart Information', {'fields': ('user', 'product', 'items', 'price',)}),
    )




admin.site.register(NewUser, UserAdminConfig)
admin.site.register(Favorite, FavoriteAdminConfig)
admin.site.register(Address, AddressAdminConfig)
admin.site.register(Cart, CartAdminConfig)

