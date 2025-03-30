from django.shortcuts import render , redirect , get_object_or_404
from .models import Post
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView , FormView
from .forms import ContactForm , PostForm
from  django.urls import reverse

# Create your views here.

# def post_list(request):
#     post_list = Post.objects.all()

#     return render(request , 'post/post_list.html' , {'post_list':post_list})

# def post_detail(request , slug):
#     pass

# templates
# django name template : post/post_list.html
# model name : Post
"""
if you want to change the name of the template
    template_name = 'post/post_list.html'

if PostDetail 
django name template : post/post_detail.html

it take the name of the model and add _detail
"""



class PostList(ListView):
    model = Post
    ordering = ['-created_at']
    # template_name = 'post/post_list.html'
    # context_object_name = 'post_list' ## in template [object_list , post_list]
    # paginate_by = 3 # in template paginator name is page_obj
    # page_kwarg = 'page' # if you want to change the name of the page in the url
    # allow_empty = True # if you want to allow empty page
    # template_name_suffix = '_list' # if you want to change the name of the template
    # template_name = 'post/post_list.html' # if you want to change the name of the template
    # context_object_name = 'post_list' # if you want to change the name of the context in the template
    # paginator_class = MyPaginator # if you want to add custom paginator class 
    # in template paginator name is paginator 
    # extra_context = {'title': 'Post List'} # if you want to add extra context to the template
    # queryset = Post.objects.filter(active=True) # if you want to filter the post by active = True
    def get_queryset(self):
        return Post.objects.filter(active=True) # if you want to filter the post by active = True
    
    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Posts List'
        return context

class FormView(FormView):
    form_class = ContactForm
    template_name = 'post/form.html'
    success_url = '/' # success_url = return redirect()

    def form_valid(self, form):
        #print(form.cleaned_data)
        return super().form_valid(form)


class PostDetail(DetailView):
    model = Post ## in template [object_list , post_list]
    
    # add comment to the post
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['comment_form'] = CommentForm()
    #     return context

    # template_name = 'post/post_detail.html'
    # context_object_name = 'post' ## in template [post]
    # slug_field = 'slug' # if you want to change the name of the slug
    # slug_url_kwarg = 'slug' # if you want to change the name of the slug in the url
    


class PostCreate(CreateView):
    model = Post # template name for CreateView is post_form.html
    template_name = 'post/post_form.html' 
    fields = ['title' , 'content' , 'image']
    success_url = '/'

# i Make UpdateView Use The Same Template I Used For CreateView or FormView 
class PostUpdate(UpdateView):
    model = Post
    fields = ['title' , 'content' , 'image']
    template_name = 'post/form.html' # template name for UpdateView is post_form.html
    def get_success_url(self):
        return reverse('post:post_detail' , kwargs={'slug':self.object.slug})
    # methods
    # def post(self, request, *args, **kwargs):
    #     return super().post(request, *args, **kwargs)

class PostDelete(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post/delete_post.html'


