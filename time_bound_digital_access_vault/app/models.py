from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# class User(models.Model):
#   firstname = models.CharField(max_length=30)
#   lastname = models.CharField(max_length=30)
#   user_id = models.CharField(max_length=20, unique=True)
#   password=models.CharField(max_length=128, null=True, blank=True)
#   def __str__(self):
#     return f"{self.firstname} {self.lastname}"

class VaultItems(models.Model):
  def __init__(self, request):
    self.session=request.session
    item=self.session.get('session_key')
    if'session-key' not in request.session:
      item=self.session['session_key']={}
    self.item=item

  def add(self, vitem):
    vitem_id=str(vitem.id)
    if vitem_id in self.item:
      pass
    else:
      self.item[vitem_id]={'title':str(vitem.title),'content':str(vitem.content),'owner_reference':str(vitem.user.id), 'timestamp':str(vitem.timestamp)}
  title = models.CharField(max_length=255)
  content = models.TextField()
  owner_reference_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  creation_timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
  
class ShareLinkRules(models.Model):
  expiration_time = models.DateTimeField()
  max_views = models.PositiveIntegerField()
  access_password = models.CharField(max_length=30)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  vault_item = models.ForeignKey(VaultItems,on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.user}"


class AuditLogs(models.Model):
  timestamp = models.DateTimeField(auto_now_add=True)
  access_outcome = models.CharField(max_length=10)
  src_metadata = models.GenericIPAddressField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  vault_item = models.ForeignKey(VaultItems,on_delete=models.CASCADE)

  def __str__(self):
    return f"Audit Log for {self.vault_item} at {self.timestamp}"
