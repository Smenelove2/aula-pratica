import utilitarios

notas = utilitarios.ler_notas_csv()

media = utilitarios.calcular_media(notas)

maior_nota = utilitarios.obter_maior_nota(notas)

menor_nota = utilitarios.obter_menor_nota(notas)

notas_aprovadas = utilitarios.listar_aprovados(notas)

notas_reprovadas = utilitarios.listar_reprovados(notas)

quantidade_aprovados = utilitarios.contar_aprovados(notas)

quantidade_reprovados = utilitarios.contar_reprovados(notas)

soma_notas = utilitarios.calcular_soma_notas(notas)

mediana = utilitarios.calcular_mediana(notas)

amplitude = utilitarios.calcular_amplitude(notas)

notas_ordenadas_crescente = utilitarios.ordenar_notas_crescente(notas)

notas_ordenadas_decrescente = utilitarios.ordenar_notas_decrescente(notas)

notas_acima_de_sete = utilitarios.buscar_notas_acima_de(notas, 5.0)

notas_abaixo_de_sete = utilitarios.buscar_notas_abaixo_de(notas, 5.0)

quantidade_notas_unicas = utilitarios.contar_notas_unicas(notas)