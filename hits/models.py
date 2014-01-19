from django.db import models


class Hit(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
