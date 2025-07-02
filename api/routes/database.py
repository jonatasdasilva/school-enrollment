from api.settings import Settings
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# cria o pool de conexões
engine = create_engine(Settings().DATABASE_URL)

# cria a sessão
session = Session(engine)

# operações na base de dados
session.add(obj) # Adiciona um objeto na base de dados
session.delete(obj) # Deleta um objeto na base de dados
session.refresh(obj) # Atualiza um objeto com a sessão

# Executa as UTs no banco de dados
session.commit()

# Desfaz as UTs no banco de dados
session.rollback()

# inicia a sessão
session.begin()

# fecha a sessão
session.close()
