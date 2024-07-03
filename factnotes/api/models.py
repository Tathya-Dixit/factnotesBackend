from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    archived = models.BooleanField(default=False)
    updated = models.TimeField(auto_now=True)
    created = models.TimeField(auto_now_add = True)
    

    class Meta:
        verbose_name = ("Note")
        verbose_name_plural = ("Notes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Note_detail", kwargs={"pk": self.pk})
