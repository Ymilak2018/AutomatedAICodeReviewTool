from django.db import models

# Create your models here.

class Message(models.Model):
    id = models.AutoField(primary_key=True)
    inp_text = models.TextField(max_length=999, verbose_name='Enter Your Text')

    def __str__(self):
        return f'Message {self.id}'