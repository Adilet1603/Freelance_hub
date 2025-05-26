from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi




schema_view = get_schema_view(
    openapi.Info(
        title="FreelanceHub API",
        default_version='v1',
        description="...",
        terms_of_service="https://your-site.com/terms/",
        contact=openapi.Contact(email="contact@your-site.com"),
        license=openapi.License(name="BSD License"),
    ),
)

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('freelance_app.urls')),
    path('accounts/', include('allauth.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
