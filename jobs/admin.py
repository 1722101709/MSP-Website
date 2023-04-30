from django.contrib import admin
from .models import Database, Company, Eligibilities, Internships, Contest, ContestDatabase, User
# Register your models here.
admin.site.register(Database)
admin.site.register(Internships)
admin.site.register(Company)
admin.site.register(Eligibilities)
admin.site.register(Contest)
admin.site.register(ContestDatabase)
admin.site.register(User)
