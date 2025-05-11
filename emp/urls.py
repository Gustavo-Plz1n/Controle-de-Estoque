from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("check-prod/", getProd),
    path("home-emp/",emp_home),
    path("add-prod/",add_produto),
    #path("delete-emp/<int:emp_id>",delete_emp),
    #path("update-emp/<int:emp_id>",update_emp),
    path("delete-prod/<int:produto_id>", delete_produto),
    path("update-prod/<int:produto_id>", update_produto),
    path("do-update-emp/<int:emp_id>",do_update_emp),
    path('buscar-produto/', buscar_produto_view, name='buscar_produto'),
]
