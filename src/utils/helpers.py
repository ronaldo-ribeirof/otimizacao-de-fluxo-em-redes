def ler_dados(arquivo):
    """Lê dados de um arquivo e retorna uma lista de linhas."""
    with open(arquivo, 'r') as f:
        return f.readlines()

def imprimir_resultados(resultados):
    """Imprime os resultados formatados."""
    for chave, valor in resultados.items():
        print(f"{chave}: {valor}")

def validar_entrada(entrada, tipo):
    """Valida a entrada com base no tipo esperado."""
    if tipo == 'int':
        return isinstance(entrada, int) and entrada >= 0
    elif tipo == 'float':
        return isinstance(entrada, float) and entrada >= 0.0
    elif tipo == 'str':
        return isinstance(entrada, str) and entrada.strip() != ""
    return False