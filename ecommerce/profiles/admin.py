from django.contrib import admin

from .models import UserTransaction


class UserTransactionAdmin(admin.ModelAdmin):
	class Meta:
		model = UserTransaction
admin.site.register(UserTransaction, UserTransactionAdmin)
