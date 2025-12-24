from django.contrib import admin
from .models import VaultItems, ShareLinkRules, AuditLogs

admin.site.register(VaultItems)
admin.site.register(ShareLinkRules)
admin.site.register(AuditLogs)

