# src/validadores.py

import re

def validar_cpf(cpf: str) -> bool:
    """
    Valida o formato e os dígitos verificadores de um CPF.
    Retorna True se válido, False caso contrário.
    """
    # Verifica formato XXX.XXX.XXX-XX
    if not re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", cpf):
        return False
    # Verifica dígitos repetidos
    if cpf.count(cpf[0]) == len(cpf.replace('.', '').replace('-', '')):
        return False
    # (Simulação simplificada)
    return True

def validar_senha(senha: str) -> bool:
    """
    Valida se a senha atende aos critérios de segurança.
    """
    if not (8 <= len(senha) <= 20):
        return False
    if not re.search(r"[A-Z]", senha):
        return False
    if not re.search(r"[0-9]", senha):
        return False
    if not re.search(r"[!@#$%^&*()_+=\-]", senha):
        return False
    return True
