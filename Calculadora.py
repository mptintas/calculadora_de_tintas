import streamlit as st

# Função para validar e converter entrada numérica
def validar_entrada(texto):
    texto = texto.replace(",", ".")  # Substitui vírgulas por pontos
    try:
        return float(texto)
    except ValueError:
        st.error("Por favor, insira um número válido.")
        st.stop()

# Função para calcular as embalagens necessárias
def calcular_embalagens(volume, apenas_galoes=False):
    if apenas_galoes:
        # Apenas galões de 3,6 litros
        galoes = int(volume // 3.6)
        if volume % 3.6 > 0:
            galoes += 1  # Ajusta para cima se houver sobra
        total_volume = galoes * 3.6
        return 0, galoes, total_volume  # Retorna 0 baldes
    else:
        # Baldes de 18 litros e galões de 3,6 litros
        baldes = int(volume // 18)  # Número de baldes de 18 litros
        restante = volume % 18
        galoes = int(restante // 3.6)  # Número de galões de 3,6 litros
        if restante % 3.6 > 0:
            galoes += 1  # Ajusta para cima se houver sobra
        total_volume = baldes * 18 + galoes * 3.6
        return baldes, galoes, total_volume

# CSS customizado para ajustar o cursor apenas no selectbox
st.markdown(
    """
    <style>
    select {
        cursor: pointer; /* Faz a mãozinha aparecer apenas em caixas select */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def calcular_rendimento_e_espessura():
    # Cria colunas para centralizar a imagem    
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:  # Coloca o logotipo na coluna do meio
        st.image("Logo.png", width=300)

    st.header("Calculadora de Rendimento - Tinta Epóxi MP")
    st.write("Selecione o produto, informe a área que deseja revestir e descubra a quantidade necessária de Tinta Epóxi e qual será a Espessura Final da aplicação.")

    # Entrada de seleção do produto
    produto = st.selectbox("Selecione o produto:", [
        "Tinta Epóxi Dupla Função (78% de sólidos)",
        "Esmalte Epóxi 100% Sólidos"
    ])
    teor_solidos = 78 if "78%" in produto else 100  # Define o teor de sólidos com base no produto
    apenas_galoes = "100% Sólidos" in produto  # Define se deve usar apenas galões

    # Entrada da área
    area = st.text_input("Digite a área a ser pintada (em m²):", "0,00")
    area = validar_entrada(area)

    if st.button("Calcular"):
        if area <= 0:
            st.error("A área deve ser maior que zero.")
        else:
            # Calcula o volume necessário para uma demão
            espessura_desejada = 108  # microns
            volume_por_m2 = espessura_desejada / (teor_solidos / 100 * 1000)  # Volume necessário por m²
            volume_necessario_1_demao = volume_por_m2 * area

            # Calcula embalagens e volume total para uma demão
            baldes_1, galoes_1, volume_real_1 = calcular_embalagens(volume_necessario_1_demao, apenas_galoes)

            # Calcula embalagens e volume total para duas demãos (arredondando para menos)
            volume_necessario_2_demao = 2 * volume_real_1  # Duas demãos baseadas no volume adquirido
            baldes_2, galoes_2, volume_real_2 = calcular_embalagens(volume_necessario_2_demao, apenas_galoes)

            # Calcula espessuras finais
            espessura_final_1 = (volume_real_1 / area) * (teor_solidos / 100) * 1000
            espessura_final_2 = (volume_real_2 / area) * (teor_solidos / 100) * 1000

            # Exibição de resultados
            st.success("Resultados Calculados com Sucesso!")
            st.write(f"**Produto Selecionado:** {produto}")
            st.write(f"**Área a ser pintada:** {area:.2f} m²")

            st.subheader("Para uma Demão:")
            if baldes_1 > 0:
                st.write(f"**Baldes de 18 litros:** {baldes_1}")
            if galoes_1 > 0:
                st.write(f"**Galões de 3,6 litros:** {galoes_1}")
            st.write(f"**Volume Total Adquirido:** {volume_real_1:.2f} litros")
            st.write(f"**Espessura Final:** {espessura_final_1:.2f} microns (µm)")

            st.subheader("Para Duas Demãos:")
            if baldes_2 > 0:
                st.write(f"**Baldes de 18 litros:** {baldes_2}")
            if galoes_2 > 0:
                st.write(f"**Galões de 3,6 litros:** {galoes_2}")
            st.write(f"**Volume Total Adquirido:** {volume_real_2:.2f} litros")
            st.write(f"**Espessura Final:** {espessura_final_2:.2f} microns (µm)")

    st.write(">*Cálculo para uma espessura final (seca) mínima de 108 microns por demão, dentro da faixa estabelecida pela NBR 14050 da ABNT, que especifica espessuras entre 100 e 180 microns para pinturas consideradas de baixa espessura.")

# Executar a aplicação
if __name__ == "__main__":
    calcular_rendimento_e_espessura()
