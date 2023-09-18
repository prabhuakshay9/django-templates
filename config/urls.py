from django.conf import settings
from django.contrib import admin
from django.urls import include, path

# Admin customization
admin.site.site_header = settings.WEBSITE_NAME
admin.site.site_title = f"{settings.WEBSITE_NAME} Administration"
admin.site.index_title = f"{settings.WEBSITE_NAME} - Admin"

# URL Patterns for installed apps
urlpatterns = [
    path("", include("apps.core.urls")),
    path('accounts/', include("apps.accounts.urls")),
    path('admin/', admin.site.urls),
]

# If DEBUG is true, load Dev Apps URLs
if settings.DEBUG:
    urlpatterns.extend([
        path("__reload__/", include("django_browser_reload.urls")),
    ])
