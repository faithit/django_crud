from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
   path('',views.index,name='index'),
   path('products/',views.admin ,name='products'),
   path('addproduct/',views.add_product,name='addproduct'),
   path('delete/<int:id>/',views.delete_product,name='delete'),
   path('update/<int:id>/',views.update_product,name='update'),
   path('register/',views.register_user,name='register')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)