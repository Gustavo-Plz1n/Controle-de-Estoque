from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path("check-prod/", login_required(getProd)),
    path("home-emp/", login_required(emp_home)),
    path("add-prod/", login_required(add_produto)),
    path("delete-prod/<int:produto_id>", login_required(delete_produto)),
    path("update-prod/<int:produto_id>", login_required(update_produto)),
    path("do-update-emp/<int:emp_id>", login_required(do_update_emp)),
    path('buscar-produto/', login_required(buscar_produto_view), name='buscar_produto'),
]
