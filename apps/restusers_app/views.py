# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.

# url(r'^$', views.index),
# a GET request to /users - calls the index method to display all the users.
#   This will need a template.
def index(request) :
    print '$'*40 + " views:Index " + '$'*40
    context = { }
    return render(request, "restusers_app/index.html", context)

# url(r'^new$', views.new),
# GET request to /users/new - calls the new method to display a form allowing users to create a new user.
#   This will need a template.
def new(request) :
    print '$'*40 + " views:new " + '$'*40
    context = { }
    return render(request, "restusers_app/new.html", context)

# url(r'^(?P<number>\d+)/edit$', views.edit),
# GET request /users/<id>/edit - calls the edit method to display a form allowing users to edit an existing user with the given id.
#   This will need a template.
def edit(request, number) :
    print '$'*40 + " views:edit " + '$'*40

    #TODO Break full name into first name and last name.  pass in context.
    context = { 'id':number }
    return render(request, "restusers_app/edit.html", context)

# url(r'^(?P<number>\d+)$', views.show),
# GET /users/<id> - calls the show method to display the info for a particular user with given id.
#   This will need a template.
def show(request, number) :
    print '$'*40 + " views:show " + '$'*40
    context = { 'id':number }
    return render(request, "restusers_app/show.html", context)

# url(r'^create$', views.create),  # Post method sends here..
# POST to /users/create - calls the create method to insert a new user record into our database. This POST should be sent from the form on the page /users/new.
#   Have this redirect to /users/<id> once created.
def create(request) :
    print '$'*40 + " views:create " + '$'*40
    pass

# url(r'^(?P<number>\d+)/delete$', views.destroy),
# GET /users/<id>/destroy - calls the destroy method to remove a particular user with the given id.
#   Have this redirect back to /users once deleted.
def destroy(request, number) :
    print '$'*40 + " views:destroy " + '$'*40
    context = { 'id':number }
    pass

# url(r'^(?P<number>\d+)/update$', views.update),
# POST /users/<id> - calls the update method to process the submitted form sent from /users/<id>/edit.
#   Have this redirect to /users/<id> once updated.
def update(request, number) :
    print '$'*40 + " views:update " + '$'*40
    context = { 'id':number }
    pass
