from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


def index(request):
    """显示网站主页"""
    return render(request, 'my_sites/index.html')


@login_required
def topics(request):
    """显示所有主题"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'my_sites/topics.html', context)


@login_required
def topic(request, topic_id):
    """显示单个主题及其所有条目"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'my_sites/topic.html', context)


@login_required
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('my_sites:topics'))

    context = {'form': form}
    return render(request, 'my_sites/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(topic, request)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('my_sites:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'my_sites/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """编辑既有的条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(topic, request)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_sites:topic', args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'my_sites/edit_entry.html', context)


# 检测登录用户是否是请求用户，如果不是，返回404
def check_topic_owner(topic, request):
    if topic.owner != request.user:
        raise Http404
