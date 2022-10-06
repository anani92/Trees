from time import strftime
from django.shortcuts import redirect, render
from login.models import User
from .models import Tree
# Create your views here.
from datetime import datetime


def welcome(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user':  user,
        'trees': Tree.objects.all(),
    }
    return render(request, 'dashbord.html', context)


def plant_tree(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user':  user,

    }
    return render(request, 'plant-tree.html', context)


def plant(request):
    user = User.objects.get(id=request.session['user_id'])
    spiecie = request.POST.get('spiecie')
    location = request.POST.get('location')
    reason = request.POST.get('reason')
    date_planted = request.POST.get('plant_date')
    date_planted = datetime.strptime(date_planted, '%y-%m-%d')
    new_tree = Tree.objects.create(
        spiecie=spiecie,
        location=location,
        reason=reason,
        date_planted=date_planted,
        planted_by=user
    )
    print(date_planted)
    new_tree.save()
    return redirect(f'/arbortary/show_tree/{new_tree.id}')


def show_tree(request, id):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user':  user,
        'tree': Tree.objects.get(id=id)
    }
    return render(request, 'show_tree.html', context)


def user_dash(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'user_account.html', context)


def show_edit_page(request, tree_id):
    tree = Tree.objects.get(id=tree_id)

    context = {
        'tree': tree,
    }
    return render(request, 'edit_tree.html', context)


def edit_tree(request, tree_id):
    tree = Tree.objects.get(id=tree_id)
    tree.spiecie = request.POST.get('edit_spiecie')
    tree.location = request.POST.get('edit_location')
    tree.reason = request.POST.get('edit_reason')
    edited_date = request.POST.get('edit_date_planted')
    tree.date_planted = datetime.strptime(edited_date, '%Y-%m-%d')
    tree.save()
    return redirect(f'/arbortary/show_tree/{tree_id}')


def add_to_visited(request, tree_id):
    user = User.objects.get(id=request.session['user_id'])
    tree = Tree.objects.get(id=tree_id)
    user.visited_trees.add(tree)
    return redirect(f'/arbortary/show_tree/{tree_id}')


def delete_tree(request, tree_id):
    tree = Tree.objects.get(id=tree_id)
    tree.delete()
    return redirect('/arbortary/account')


def log_out(request):
    request.session.clear()
    return redirect('/')
