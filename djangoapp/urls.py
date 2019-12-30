"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from djangoapp.settings.prod import STATIC_URL, STATIC_ROOT
from django.conf.urls.static import static

from views import urls as views_urls
from news import urls as news_urls
from accounts import urls as accounts_urls
from activities import urls as activities_urls
from workshops import urls as workshops_urls
from events import urls as events_urls
from social import urls as socials_urls
from checkout import urls as checkout_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(views_urls)),
    path('news/', include(news_urls)),
    path('accounts/', include(accounts_urls)),
    path('activities/', include(activities_urls)),
    path('workshops/', include(workshops_urls)),
    path('events/', include(events_urls)),
    path('socials/', include(socials_urls)),
    path('checkout/', include(checkout_urls))
] + static(STATIC_URL, document_root=STATIC_ROOT)
