import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- Configuração do Banco de Dados ---
# Prioriza a DATABASE_URL do ambiente (para Docker/Produção)
# Usa SQLite como fallback (para desenvolvimento local sem Docker)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./academic_agent.db")

# A verificação de 'check_same_thread' é específica para SQLite.
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL, connect_args=connect_args
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """
    Inicializa o banco de dados.
    Cria todas as tabelas se elas ainda não existirem.
    """
    from .models import Base
    Base.metadata.create_all(bind=engine)

# Se estivermos usando SQLite, é seguro inicializar o DB ao carregar o módulo.
# Para PostgreSQL, as migrações serão gerenciadas de outra forma (ex: Alembic).
if DATABASE_URL.startswith("sqlite"):
    print("Using SQLite database. Initializing database and creating tables...")
    init_db()
    print("Database initialized.") 