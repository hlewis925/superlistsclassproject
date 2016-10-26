from django.db import models

class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def save(self, for_list):
        self.instance.list = for_list
        return super().save()

    def __str__(self):
        return self.text
