from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):

    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """返回模型的字符串显示"""
        return self.text


class Entry(models.Model):

    """用户学习主题下的相关知识"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串显示"""
        t = self.text
        if len(t) >= 50:
            return t[:50] + '......'
        return t