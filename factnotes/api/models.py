from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    bgcolor = models.CharField(max_length = 50,default="rgb(17 24 39)")
    archived = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)
    

    class Meta:
        verbose_name = ("Note")
        verbose_name_plural = ("Notes")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Note_detail", kwargs={"pk": self.pk})
