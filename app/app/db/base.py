# Import all the models, so that Base has them before being
# imported by Alembic
from .database import Base
from app.models.mean import Mean
from app.models.word import Word
from app.models.user import User