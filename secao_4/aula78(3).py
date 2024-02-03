# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}

uniao = s1 | s2
interseccao = s1 & s2
diferenca1 = s1 - s2
diferenca2 = s2 - s1
diferenca_simetrica = s1 ^ s2 # Não importa a sequência 
print(uniao) # Os valores presentes nos dois sets sem repetir
print(interseccao) # Os valores que iguais nos dois
print(diferenca1) # presentes apenas no set da esquerda
print(diferenca2) 
print(diferenca_simetrica) 