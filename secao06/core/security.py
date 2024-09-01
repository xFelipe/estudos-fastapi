from passlib.context import CryptContext


CRIPTO = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """Verifica se senha inserida pelo usuário está correta"""
    return CRIPTO.verify(secret=senha, hash=hash_senha)


def gerar_hash_senha(senha: str) -> str:
    return CRIPTO.hash(senha)