from . import views
from django.urls import path
app_name='shop'
urlpatterns=[

    path('',views.allproductcat,name='allproductcat'),
    path('shop/<slug:c_slug>/',views.allproductcat,name='products_by_category'),
    path('shop/<slug:c_slug>/<slug:product_slug>/',views.productdetails,name='productcategory'),
]