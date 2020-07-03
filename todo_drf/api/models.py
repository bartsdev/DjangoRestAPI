from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        status = ""
        if self.completed is True:
            status = "Completed"
        else:
            status = "Not Completed"
        return f"{self.title}, Status : {status}"

