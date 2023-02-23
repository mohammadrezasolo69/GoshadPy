from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
)

urlpatterns_api = [

]

urlpatterns = [
    path('admin/', admin.site.urls),

    # my api
    include('api/v1/', include(urlpatterns_api)),

    # urls drf_spectacular
    path('schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),


    {%- if cookiecutter.use_ckeditor == 'y' -%}
    path('ckeditor/', include('ckeditor_uploader.urls'), name="CKEditor_URL"),# urls CkEditor
    {%- endif -%}


    {%- if cookiecutter.use_django_debug_toolbar == 'y' -%}
    path('__debug__/', include('debug_toolbar.urls')),# urls debug_toolbar
    {%- endif -%}
]



# -------------------------------- Config Static and Media File -----------------------------------
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
