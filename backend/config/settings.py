import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # APPLICATIONS
    'backend.apps.news',
    'backend.apps.about',
    'backend.apps.account',
    'backend.apps.information',
    'backend.apps.livestream',
    'backend.apps.service',
    'backend.apps.index',
    'backend.apps.appeal',
    'backend.apps.job',
    'backend.apps.card',

    # library
    'ninja',
    'minio_storage',
    'ckeditor',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Перед corsheaders.middleware.CorsMiddleware
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://tsvs.gov.kg",
]


ROOT_URLCONF = 'backend.config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.config.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("POSTGRES_DB", default="db"),
        "USER": os.getenv("POSTGRES_USER", default="db_admuser"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", default="db_ZAQ12345tgb*"),
        "HOST": os.getenv("POSTGRES_HOST", default="127.0.0.1"),
        "PORT": os.getenv("POSTGRES_PORT", default="5432"),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Bishkek'
USE_I18N = True
USE_TZ = True


NINJA_API_URL = '/api/'
STATIC_URL = '/static/'
# для сервера
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# MEDIA
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}
# STOREGE
DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
MINIO_STORAGE_ENDPOINT = 'http://storage.tsvs.kg:5554/'
MINIO_STORAGE_ACCESS_KEY = 'Y2FkDiOCa82HME3t'
MINIO_STORAGE_SECRET_KEY = 'F3rSWzq9aTt0ZzijntTB5e5aULx10Yqs'
MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'media'
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_STATIC_BUCKET_NAME = 'static'
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True
