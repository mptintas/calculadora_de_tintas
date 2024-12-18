import streamlit as st

def calcular_rendimento_e_espessura():
    st.title("MP TINTAS EPÓXI")
    st.header("Calculadora de Rendimento e Espessura de tintas")
    st.write("Preencha os campos abaixo para calcular o rendimento e espessura da tinta.")

    # Entrada de dados
    volume_tinta = st.number_input("Digite o volume de tinta (em litros):", min_value=0.0, format="%.2f")
    teor_solidos = st.number_input("Digite o teor de sólidos (em %):", min_value=0.0, max_value=100.0, format="%.2f")
    area = st.number_input("Digite a área a ser pintada (em m²):", min_value=0.0, format="%.2f")

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
