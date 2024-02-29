from django.apps import AppConfig
from django.conf import settings
# from .db_manager import DocumentManager
# import os
import logging


logger = logging.getLogger(__name__)


class ChromaConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chroma"
