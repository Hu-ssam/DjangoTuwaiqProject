from django.db import models

# Create your models here.
class ConversationHistory(models.Model):
    amount = models.FloatField()
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    converted_amount = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
