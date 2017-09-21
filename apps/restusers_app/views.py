# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import User, UserManager

def index(request) :
    context = { 'users' : User.objects.all() }
    return render(request, "restusers_app/index.html", context)

def new(request) :
    return render(request, "restusers_app/new.html")

def edit(request, number) :
    context = { 'user':User.objects.get(id=number) }
    return render(request, "restusers_app/edit.html", context)

def show(request, number) :
    print "POST: ", request.POST
    context = { 'user':User.objects.get(id=number) }
    return render(request, "restusers_app/show.html", context)

# url(r'^create$', views.create),  # Post method sends here..
# POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new.
#   Have this redirect to /users/<id> once created.
def create(request) :
    fName=request.POST['first_name']
    lName= request.POST['last_name']
    a_email = request.POST['email']

    newUser = User.objects.Creator(fName, lName, a_email)
    return redirect('/')

# url(r'^(?P<number>\d+)/delete$', views.destroy),
# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id.
#   Have this redirect back to /users once deleted.
def destroy(request, number) :
    thisUser =  User.objects.get(id=number)
    if None == thisUser:
        # TODO: Display this error.
        return redirect ('/')
    thisUser.delete()
    thisUser = None
    return redirect('/')

# url(r'^(?P<number>\d+)/update$', views.update),
# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit.
#   Have this redirect to /users/<id> once updated.
def update(request):
    userID=request.POST['id']
    fName=request.POST['first_name']
    lName= request.POST['last_name']
    a_email = request.POST['email']

    thisUser = newUser = User.objects.EditEntry(userID, fName, lName, a_email)
    if None == thisUser:
        # TODO: Display this error.
        return redirect ('/{}/edit'.format(userID))
    return redirect ('/{}'.format(thisUser.id))
