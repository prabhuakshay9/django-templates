from django.conf import settings


def website_name(request):
    # Add 'WEBSITE_NAME' to the context
    return {"WEBSITE_NAME": settings.WEBSITE_NAME}
