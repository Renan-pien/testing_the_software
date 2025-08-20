# executar_testes.py

from src.validadores import validar_cpf, validar_senha

def testar_senha():
    print("== Testes de Senha ==")
    casos = [
        ("Senha123!", True),
        ("senha123!", False),
        ("SENHA123!", True),  # Não exige minúscula no código
        ("Senha!", False),
        ("Senha123", False),
        ("Se123!", False),
        ("Senha123!Senha123!Senha", False)
    ]
    for entrada, esperado in casos:
        resultado = validar_senha(entrada)
        status = "OK" if resultado == esperado else "FALHOU"
        print(f"Entrada: {entrada:<30} Esperado: {esperado} | Resultado: {resultado} -> {status}")

def testar_cpf():
    print("\n== Testes de CPF ==")
    casos = [
        ("123.456.789-00", False), #deveria retornar false, mais a função esta retornando true.
        ("111.111.111-11", False),
        ("123.456.789-0a", False),
        ("12345678900", False),
        ("390.533.447-05", True)  # Simulado como válido
    ]
    for entrada, esperado in casos:
        resultado = validar_cpf(entrada)
        status = "OK" if resultado == esperado else "FALHOU"
        print(f"Entrada: {entrada:<20} Esperado: {esperado} | Resultado: {resultado} -> {status}")

if __name__ == "__main__":
    testar_senha()
    testar_cpf()
