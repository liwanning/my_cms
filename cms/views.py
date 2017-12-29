from django.shortcuts import render,get_object_or_404,render_to_response
from django.db.models import Q
from cms.models import Category,Story
from django.views.generic import ListView,DetailView
# Create your views here.

def category(request,slug):
    category_obj = get_object_or_404(Category,slug=slug)
    story_list = Story.objects.filter(category=category_obj)
    heading = "Category:%s"%category_obj.label
    return render(request,'cms/story_list.html',locals())

class StoryListView(ListView):
    model = Story
    template_name = 'cms/story_list.html'
    context_object_name = "story_list"

class StoryDetailView(DetailView):
    model = Story
    template_name = "cms/story_detail.html"
    context_object_name = "story"

def search(request):
    print(request.GET)
    if 'q' in request.GET:

        term = request.GET.get('q')
        story_list = Story.objects.filter(Q(title__icontains=term)|Q(makedown_content__icontains=term)).all()
        heading = "检索结果"
        return render(request,"cms/story_list.html",locals())