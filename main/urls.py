from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    path('create-product-ajax/', add_product_ajax, name="create_product_ajax"),
    path('product/<uuid:id>/', show_product, name='show_product'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:product_id>/edit-ajax', edit_product_ajax, name='edit_product_ajax'),
    path('product/<uuid:id>/delete', delete_product, name="delete_product"),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('register_ajax/', register, name='register_ajax'),
    path('login/', login_user, name='login'),
    path('login_ajax/', login_ajax, name='login_ajax'),
    path('logout/', logout_user, name='logout'),
    path('proxy-image/', proxy_image, name="proxy_image"),
    path('create-flutter/', create_product_flutter, name="create_flutter")
]