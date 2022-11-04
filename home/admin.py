from django.contrib import admin
from django.contrib.auth.models import Group,User

# from orphanage.home.models import Orphanage
from . models import District,Orphanage, donationtype, new_donor

# Register your models here.

admin.site.register(District)
admin.site.register(donationtype)

class OrphanageAdmin(admin.ModelAdmin):
    list_display = ('name','district','city','pin','image','phone','email','no_of_persons')


admin.site.register(Orphanage,OrphanageAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)


class UserAdmin(admin.ModelAdmin):
    list_display=['donorname']
    exclude=('password',)
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    verbose_name_plural = "Donor Details"
admin.site.register(new_donor,UserAdmin)