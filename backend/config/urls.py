from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from ninja import NinjaAPI
from ninja.security import django_auth

from backend.config import settings
from backend.apps.news.views import router as news_router
from backend.apps.index.views import router as index_router
from backend.apps.card.views import router as card_router
from backend.apps.about.views import router as about_router
from backend.apps.service.views import router as service_router
from backend.apps.information.views import router as info_router
from backend.apps.license.views import router as license_router
from backend.apps.blank.views import router as blank_router
from backend.apps.rating.views import router as rating_router
from backend.apps.job.views import router as job_router
from backend.apps.livestream.views import router as stream_router
from backend.apps.account.views import router as register_router
from backend.apps.account.auth.login import router as login_router
from backend.apps.appeal.views import router as appeal_router


api = NinjaAPI(
    title="Сайт ГАРТСВС при КМ КР", # наименование проекта
   # docs_url=None, # закрыть доступ к документации docs
) # auth=django_auth, csrf=True

api.add_router(
    "api/",
    index_router,
    tags=["Видео в главной странице"]
)

api.add_router(
    "api/index",
    card_router,
    tags=["Карточки главной страницы"]
)

api.add_router(
    "api/about",
    about_router,
    tags=["О Нас"]
)

api.add_router(
    "api/new",
    news_router,
    tags=["Новости"]
)

api.add_router(
    "api/service",
    service_router,
    tags=["Сервисы"]
)

api.add_router(
    "api/information",
    info_router,
    tags=["Информации"]
)

api.add_router(
    "api/license",
    license_router,
    tags=["Вывод лицензии"]
)

api.add_router(
    "api/blank",
    blank_router,
    tags=["Бланки"]
)

api.add_router(
    "api/rating",
    rating_router,
    tags=["Рейтинг автошкол"]
)

api.add_router(
    "api/job",
    job_router,
    tags=["Вакансии"]
)

api.add_router(
    "api/online",
    appeal_router,
    tags=["Онлайн обращение"]
)

api.add_router(
    "api/",
    stream_router,
    tags=["Онлайн камеры"]
)

api.add_router(
    "api/register",
    register_router,
    tags=["Register"]
)
api.add_router(
    "api/login",
    login_router,
    tags=["Login"]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', api.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
