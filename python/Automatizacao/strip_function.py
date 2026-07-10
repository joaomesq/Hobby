import re

def regex_strip(string, chars=None):
    if chars is None:
        padrao = r"\s"
    else:
        padrao = rf"[{re.escape(chars)}]"

    padrao_final = rf"^{padrao}+|{padrao}+$"
    return re.sub(padrao_final, '', f"{string}")
    

# --- TESTES DE FUNCIONAMENTO ---

# Teste 1: Sem o segundo argumento (remove espaços em branco)
texto1 = "   Olá Euclides!   "
print(f"'{regex_strip(texto1)}'") 
# Saída: 'Olá, Euclides!'

# Teste 2: Removendo caracteres específicos do início e do fim
texto2 = "://exemplo.com.br"
print(f"'{regex_strip(texto2, 'w.br')}'") 
# Saída: 'exemplo.com'

# Teste 3: Removendo caracteres especiais com segurança
texto3 = "***Importante!!!***"
print(f"'{regex_strip(texto3, '*!')}'") 
# Saída: 'Importante'
