from django.urls import reverse_lazy
from django.views.generic import CreateView , UpdateView , DetailView , DeleteView 
from .forms import SignupForm , UserForm , ProfileForm
from .models import Profile
from django.shortcuts import redirect
# Create your views here.

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')



class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'
    def get_object(self):
        return self.request.user.profile

class ProfileEditView(UpdateView):
    model = Profile
    fields = ['bio' , 'phone_number' , 'image' , 'city']
    template_name = 'accounts/profile_edit.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self , queryset=None):
        return self.request.user.profile
    
    def post(self, request, *args, **kwargs):
        userform = UserForm(request.POST , instance=request.user)
        profileform = ProfileForm(request.POST , request.FILES , instance=self.get_object())
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('accounts:profile')
        else:
            userform = UserForm(instance=request.user)
            profileform = ProfileForm(instance=self.get_object())
        
        return super().post(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['userform'] = UserForm(instance=self.request.user)
        context['profileform'] = ProfileForm(instance=self.get_object())
        return context
    
class DeleteProfileView(DeleteView):
    model = Profile
    template_name = 'accounts/delete_profile.html'
    success_url = reverse_lazy('accounts:signup')

    def get_object(self , queryset=None):
        return self.request.user.profile
