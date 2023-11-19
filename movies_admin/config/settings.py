"""Django project settings."""

from pathlib import Path

from dotenv import load_dotenv
from split_settings.tools import include

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

include(
    'components/security.py',
    'components/application.py',
    'components/database.py',
    'components/password_validation.py',
    'components/internationalization.py',
    'components/static.py',
    'components/media.py',
)
