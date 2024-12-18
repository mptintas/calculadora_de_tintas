import streamlit as st

# Função para validar e converter entrada numérica
def validar_entrada(texto):
    texto = texto.replace(",", ".")  # Substitui vírgulas por pontos
    try:
        return float(texto)
    except ValueError:
        st.error("Por favor, insira um número válido.")
        st.stop()

def calcular_rendimento_e_espessura():
    # Cria colunas para centralizar a imagem    
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  # Coloca o logotipo na coluna do meio
        st.image("Logo.png", width=300)

    st.header("Calculadora de Espessura e Rendimento de Tintas")
    st.write("Conheça a espessura final da aplicação com base no Teor de Sólidos e da área a ser revestida")

    # Entrada de dados sem sinais de + e -
    volume_tinta = st.text_input("Digite o volume de tinta (em litros):", "0,00")
    teor_solidos = st.text_input("Digite o teor de sólidos (em %):", "0,00")
    area = st.text_input("Digite a área a ser pintada (em m²):", "0,00")

    # Validação e conversão das entradas
    volume_tinta = validar_entrada(volume_tinta)
    teor_solidos = validar_entrada(teor_solidos)
    area = validar_entrada(area)

    # Botão para calcular
    if st.button("Calcular"):
        if volume_tinta <= 0 or teor_solidos <= 0 or area <= 0:
            st.error("Os valores de volume, teor de sólidos e área devem ser maiores que zero.")
        else:
            # Cálculos
            teor_solidos_decimal = teor_solidos / 100  # Converter porcentagem para decimal
            volume_seco = volume_tinta * teor_solidos_decimal  # Volume que forma o filme seco
            espessura_final_seca = (volume_seco / area) * 1000  # Espessura final seca em micrômetros
            espessura_final_umida = (volume_tinta / area) * 1000  # Espessura final úmida em micrômetros
            rendimento_por_litro = area / volume_tinta  # Rendimento por litro
            rendimento_total = area  # Rendimento total para o volume informado

            # Verificação da espessura conforme a norma
            espessura_minima = 100  # Micrômetros (mínimo pela norma)
            if espessura_final_seca < espessura_minima:
                diferenca_percentual = ((espessura_minima - espessura_final_seca) / espessura_minima) * 100
                norma_resultado = f"Espessura final seca {diferenca_percentual:.2f}% inferior ao mínimo admitido pela norma NBR 14050 da ABNT."
            else:
                diferenca_percentual = ((espessura_final_seca - espessura_minima) / espessura_minima) * 100
                norma_resultado = f"Espessura final seca {diferenca_percentual:.2f}% superior ao mínimo admitido pela norma NBR 14050 da ABNT."

            # Exibição de resultados
            st.success("Resultados Calculados com Sucesso!")
            st.write(f"Rendimento por litro: **{rendimento_por_litro:.2f} m²/L**")
            st.write(f"Rendimento total: **{rendimento_total:.2f} m²** para **{volume_tinta:.2f} litros**")
            st.write(f"Espessura final úmida: **{espessura_final_umida:.2f} micrômetros (µm)**")
            st.write(f"Espessura final seca: **{espessura_final_seca:.2f} micrômetros (µm)**")
            st.write(norma_resultado)

# Executar a aplicação
if __name__ == "__main__":
    calcular_rendimento_e_espessura()
