
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userApp.urls')),
    path('event/', include('eventApp.urls')),
    # path('exam/', include('examApp.urls')),
    path('blog/', include('blogApp.urls')),
    path('member/', include('memberApp.urls')),
    path('payment/', include('paymentApp.urls')),
    path('notification/', include('notificationApp.urls')),

]
