import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-insecure-dwwp#j0@fl0^e*mw3zcp)75&0z!mi0%2ol5bx9^ol5!)lkc@)("

DEBUG = True

ALLOWED_HOSTS = [
    "projectshopapi.pythonanywhere.com",
    "45.138.158.131",
    "127.0.0.1",
    'apidilbahdairy.uz'
]
CSRF_TRUSTED_ORIGINS = [
    'https://apidilbahdairy.uz'
]
INSTALLED_APPS = [
    "modeltranslation",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "django_filters",
    "corsheaders",
    "constance",
    "api.apps.ApiConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True

STATIC_URL = "/static/"
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),
# ]
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
gettext = lambda s: s
LANGUAGES = (
    ("ru", gettext("Russian")),
    ("en", gettext("English")),
    ("uz", gettext("Uzbek")),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = "ru"
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 15,
}

CORS_ALLOW_ALL_ORIGINS = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 465
EMAIL_USE_TLS = False
EMAIL_HOST_USER = "dilbahdairy@gmail.com"  # Replace with your email address
EMAIL_HOST_PASSWORD = "uago btnw pvzk qzvk"  # Replace with your email password
EMAIL_USE_SSL = True
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

CONSTANCE_CONFIG = {
    "GENERAL_PHONE_NUMBER": ("+998900000000", "Основной номер телефона"),
    "GENERAL_EMAIL": ("info@sitename.ru", "Основная почта сайта"),
    "GENERAL_ADDRESS": ("Город, улица номер дома", "Основной адрес"),
    "GENERAL_ADDRESS_EN": ("Город, улица номер дома", "Основной адрес"),
    "GENERAL_ADDRESS_UZ": ("Город, улица номер дома", "Основной адрес"),
    "GENERAL_WORKING_TIME": ("Ежедневно, с 9:00 до 20:00", "Время работы"),
    "GENERAL_WORKING_TIME_EN": ("Ежедневно, с 9:00 до 20:00", "Время работы"),
    "GENERAL_WORKING_TIME_UZ": ("Ежедневно, с 9:00 до 20:00", "Время работы"),
    "TITLE": ("", "Заголовок главной страницы"),
    "TITLE_EN": ("", "Заголовок главной страницы"),
    "TITLE_UZ": ("", "Заголовок главной страницы"),
    "TEXT": ("", "Текст главной страницы"),
    "TEXT_EN": ("", "Текст главной страницы"),
    "TEXT_UZ": ("", "Текст главной страницы"),
    "SLOGAN": ("", "Слоган главной страницы"),
    "SLOGAN_UZ": ("", "Слоган главной страницы"),
    "SLOGAN_EN": ("", "Слоган главной страницы"),
}

CONSTANCE_CONFIG_FIELDSETS = {
    "Общее": {"fields": ("GENERAL_PHONE_NUMBER", "GENERAL_EMAIL")},
    "Статичный контент (RU)": {
        "fields": ("GENERAL_ADDRESS", "GENERAL_WORKING_TIME", "TITLE", "TEXT", "SLOGAN")
    },
    "Статичный контент (UZ)": {
        "fields": (
            "GENERAL_ADDRESS_UZ",
            "GENERAL_WORKING_TIME_UZ",
            "TITLE_UZ",
            "TEXT_UZ",
            "SLOGAN_UZ",
        )
    },
    "Статичный контент (EN)": {
        "fields": (
            "GENERAL_ADDRESS_EN",
            "GENERAL_WORKING_TIME_EN",
            "TITLE_EN",
            "TEXT_EN",
            "SLOGAN_EN",
        )
    },
}
