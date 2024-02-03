"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao, {nome}}'

saudar_bom_dia = criar_saudacao('Boa tarde')
print(saudar_bom_dia('Victor')) 