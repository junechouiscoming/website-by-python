"""定义my_sites的url模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
    # 主页URL
    url(r'^$', views.index, name='index'),

    # 主题URL
    url(r'^topics/$', views.topics, name='topics'),

    # 特定主题的详细页面URL
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    # 用户添加主题的URL
    url(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 用户添加新条目的URL
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
]