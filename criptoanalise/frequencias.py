# -*- coding: utf-8 -*-
import collections

# Texto dos caracteres, sem acento e maiusculas
texto = '''
Caminho Dificil

Por milhares de anos o ser-humano vem tentando encontrar respostas para perguntas como “qual o sentido da vida”?. A filosofia que, ao que tudo indica, parece ter se iniciado com Tales de Mileto em meados de 700 a.c, visa encontrar vestígios de perguntas sem respostas. A pesquisa profunda pela verdade absoluta advém da filosofia, e quando falamos a respeito de caminhos fáceis oc difíceis, estamos nos referindo a esse tipo de teorema.

É fácil aceitar o que desde criança te ensinaram que é errado. Difícil é quando adulto, entender que te ensinaram errado o que desde criança você suspeitou que fosse correto. Em outras palavras, se você se enquadra em alguém cujos estímulos do meio lhe determinaram certo comportamento, fazendo com que estivesse à mercê de crenças já providas e bem estabelecidas em dogmas e rituais, com uma massa concentrada de pessoas nela, ou, permitindo-o ficar no conformismo, aceitando o conceito de felicidade e de sentido da vida embutido pela mídia e pela sociedade, então claramente você faz parte do caminho fácil para a busca pela verdade absoluta. Acaso se enquanto na segunda opção, ou seja, aquele que suspeitava de todo conjunto de crenças que lhe foi enraizado, então este tem tudo para ser um investigador da veracidade nas coisas ao seu redor, entrando em um caminho mais complicado, no qual uma minoria se

	Uma vez que a normalidade se aporesenta como um padrão retilíneo e uniforme, e por conseguinte é a causa do agir das massas, logo, os do caminho fácil estão mais para ela do que os do caminho difícil. Consequentemente estes últimos tendem a ter mais disponibilidade de se extraviar, indo para a extremidade tanto de lucidez como de insanidade. Todavia, lembre-se que o dito “normal” aqui não quer dizer exatamente algo “positivo”, mas sim faz alusão ao modo que interpretam as pessoas ao derredor ao que é agir de forma aceita em uma sociedade. Acresce que esta maneira habitual de enxergar a normalidade é domada ao método incutido pela mídia e pelos outros particípios do senso comum para como você deve se manifestar no ambiente social. Ademais, convém com isto alegar a possibilidade aflorado dos que seguem o padrão reto da normalidade estarem somados aos do caminho fácil, que por sua vez resulta na alienação. Contudo, que fique claro que nem sempre é generalizado, podnedo, diferentemente, ser algo produtivo e benéfico.
	É de cunho pertinente alegar antes de mais nada que as extremidades são muito mais plausíveis de se acontecerem - independente dos caminhos a se seguir, em suas máximas - nos “contínuos”. Ora, eles são o ponto extremo das duas trilhas, então, decerto é por el-

	Vimos que o caminho fácil é uma reta, sem curvas, retilinea e uniforme. No entanto, o caminho difícil é bem apresentado como tendo inúmeras curvaturas, e justamente por não ser uniforme, não se pode ver o fim. Diferentemente da ilusão acarretada nos que seguem o caminho fácil em acuar que estão vendo o final da trilha, este novo rumo se será cheio de barreiras e poucos são os que se _ _ _ _ _ m _ _ _ m a elas.
	Para se ter uma devida noção do quão ardiloso é permear este percurso assim como glorioso e virtuoso, _ a _ _ _ que nos baseemos na vida de grandes homens que vieram para a terra. Contudo, é necessário primeiro apreender quanto as formas de se seguir essa direção. E elas serão di_i_i_as _ _  _uas  também. Desta vez não sera classi_ _ _ _   _
'''.decode('ASCII','ignore').upper()

#lista dos caracteres
letras = list(texto)
# estrutura com a frequencia de cada letra (o que nao era letra foi eliminado)
cnt = collections.Counter()
for word in letras:
	if word.isalpha():
		cnt[word] += 1
# Total de letras
total = sum(cnt.values())
print 'Total:\t%s' % total
# Frequencia absoluta por letra
for i in sorted(list(cnt)):
	print '%s\t%s' % (i, cnt[i])
# Frequencia relativa por letra
print 'Relativa'
for i in sorted(list(cnt)):
	print '%s\t%.2f%%' % (i, float(cnt[i])/total*100)
