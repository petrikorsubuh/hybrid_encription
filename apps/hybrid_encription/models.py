from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    send_from = models.CharField(max_length= 255)
    send_to = models.CharField(max_length= 255)
    key = models.CharField(max_length=30)
    enc_message = models.BinaryField()
    private_key = models.FileField(upload_to='priv_key')
    pub_key = models.FileField(upload_to='pub_key')
    enc_key_ntru = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'messages'
        ordering = ['send_to','create_at']
