# Valor planejado
vp = cota = int(input('Valor VP(COTA): '))
# Valor agregado
va = cotr = int(input('Valor VA(COTR): '))
# Custo real
cr = crtr = int(input('Valor CR(CRTR): '))
# Valor total do VP (maior)
#ont = int(input('Maior valor VP(COTA) no gráfico: '))
# Custo real no termino CRTR(maior)
#ont = int(input('Maior valor VP(COTA) no gráfico: '))
##########################################
##########################################
# Variação de Prazos
vpr = va - vp

# Variação de custo
vc = va - cr

# Índice de Desempenho de Prazo
idp = va/vp

# Índice de Desempenho de Custo
idc = va/cr

# 
#ent = cr + ONT – va

print('--------------------')
print(f'VPR: {vpr}\nVC: {vc}\nIDP: {idp}\nIDC: {idc}\n')