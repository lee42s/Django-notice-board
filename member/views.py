from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from member.models import User
from member.forms import PermissionForm
from django.utils import timezone
# Create your views here.
# def user_permission_list(request):
#     user_is_member = User.objects.filter(is_member=True, date_joined__lte=timezone.now()).order_by('-date_joined')[:10]
#     none_user = User.objects.filter(is_member=False, date_joined__lte=timezone.now()).order_by('-date_joined')[:10]
#     return render(request, 'member/permission_list.html', {'user_is_member':user_is_member,'none_user':none_user})

@login_required
def user_permission_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = PermissionForm(request.POST, instance=user)
        if form.is_valid():
            user_member = form.save(commit=False)
            user_member.is_member = user.is_member
            # post.published_date = timezone.now()
            user_member.save()
            return redirect('manager_home')
    else:
        user_username = User.objects.filter(id=pk)
        form = PermissionForm(instance=user)
    return render(request, 'member/permission_edit.html',{'form':form,})