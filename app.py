from conversor import ler_notas_csv

notas = ler_notas_csv()

media = calcular_media(notas)

maior_nota = obter_maior_nota(notas)

menor_nota = obter_menor_nota(notas)

notas_aprovadas = listar_aprovados(notas)

notas_reprovadas = listar_reprovados(notas)

quantidade_aprovados = contar_aprovados(notas)

quantidade_reprovados = contar_reprovados(notas)

soma_notas = calcular_soma_notas(notas)

mediana = calcular_mediana(notas)

amplitude = calcular_amplitude(notas)

notas_ordenadas_crescente = ordenar_notas_crescente(notas)

notas_ordenadas_decrescente = ordenar_notas_decrescente(notas)

notas_acima_de_sete = buscar_notas_acima_de(notas, 5.0)

notas_abaixo_de_sete = buscar_notas_abaixo_de(notas, 5.0)

quantidade_notas_unicas = contar_notas_unicas(notas)