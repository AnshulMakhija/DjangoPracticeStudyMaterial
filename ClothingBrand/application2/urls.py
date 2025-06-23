from django.contrib import admin
from django.urls import path, include
from application2 import views

# one way
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun1_app_2/', views.function1_app2),
    path('fun2_app_2/', views.function2_app2),
]
'''

# another way
'''
urlpatterns = [
    path('app2',include([
        path('fun1_app_2/', views.function1_app2),
        path('fun2_app_2/', views.function2_app2),
    ]))
]
'''

#another way
all_paths = [
    path('fun1_app_2/', views.function1_app2),
    path('fun2_app_2/', views.function2_app2),
    path('dynamic/', views.renderhtmlrequest),
    path('dynamic2/', views.renderhtmlrequest2),
    path('filters/', views.filter_html),
    
]

urlpatterns = [
    path('app2_all_path/', include(all_paths),)
]

