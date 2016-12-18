from django.shortcuts import redirect,render, get_object_or_404
from .models import *
from django.utils import timezone
from .form import PostForm
from Uptime.chunkfile import chunkfile
from Uptime.uptimemain import *
# Create your views here.
def main(request):
	posts = addServer.objects.order_by('created_date')
	return render(request, 'suyatiUptime/main.html', {'posts': posts})
def post_detail(request, pk):
	addServer.objects.get(pk=pk)
	post = get_object_or_404(addServer, pk=pk)
	return render(request, 'suyatiUptime/post_detail.html', {'post': post})
def serv_ip():
	hosts = []
	serv = addServer.objects.order_by('created_date')
        for servers in serv:
            host = servers.ipAddress
            hosts.append(host)
        return hosts
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            host = serv_ip()
            chunk = chunkfile(host)
            datas = chunk.hostQue()
            uptimeMain.data = datas
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'suyatiUptime/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'suyatiUptimepost_edit.html', {'form': form})