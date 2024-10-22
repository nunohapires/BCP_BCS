import streamlit as st
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Projeto BCS - Unidade de Bombeio",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Barra lateral com imagem e informações do autor
st.sidebar.image('logo_nuno.jpg')
st.sidebar.markdown(
    """
    **Desenvolvido por:**
    - *Nuno Henrique Albuquerque Pires*
    - Estudante de Engenharia de Petróleo
    - Universidade Federal de Alagoas (UFAL)
    """
)

# Título principal da página
st.title('Projeto BCS ⚙🛢')
st.subheader('Unidade de Bombeio - Análise de Vazão e Correção por Fatores')

# Separador visual
st.divider()

# Bloco 1 - Entrada de Dados do Poço 1
bloco1, bloco2 = st.columns(2)

# Dados do Poço 1
with bloco1:
    st.header('📊 Dados do Poço 1')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        N1 = st.number_input('Rotação [rpm]', value=1500, help="Velocidade de rotação da bomba no Poço 1")
        Q1 = st.number_input('Produção [bpd]', value=1000, help="Produção de óleo no Poço 1")
    
    with col2:
        Di1 = st.number_input('Diâmetro da Coluna [in]', value=4.25, help="Diâmetro da coluna de produção no Poço 1")
        Ph1 = st.number_input('Pressão na Cabeça [psi]', value=230, help="Pressão na cabeça do poço")
    
    with col3:
        h1 = st.number_input('Profundidade [m]', value=1100, help="Profundidade do poço")
        densidade1 = st.number_input('Densidade do Óleo [kg/m³]', value=910, help="Densidade do óleo extraído")
    
    mi1 = st.number_input('Viscosidade do Óleo [cp]', value=1500, help="Viscosidade do óleo no Poço 1")

# Dados do Poço 2
with bloco2:
    st.header('📊 Dados do Poço 2')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        N2 = st.number_input('Rotação [rpm]', value=2000, help="Velocidade de rotação da bomba no Poço 2")
        mi2 = st.number_input('Viscosidade do Óleo [cp]', value=2000, help="Viscosidade do óleo no Poço 2")
    
    with col2:
        Di2 = st.number_input('Diâmetro da Coluna [in]', value=3.75, help="Diâmetro da coluna de produção no Poço 2")
        Ph2 = st.number_input('Pressão na Cabeça [psi]', value=200, help="Pressão na cabeça do poço")
    
    with col3:
        h2 = st.number_input('Profundidade [m]', value=1650, help="Profundidade do poço")
        densidade2 = st.number_input('Densidade do Óleo [kg/m³]', value=875, help="Densidade do óleo extraído")
    
    n = st.number_input('Fator Empírico [0.2 - 0.3]', value=0.25, min_value=0.2, max_value=0.3, step=0.01, help="Fator empírico para correção da vazão")

# Separador visual
st.divider()

# Bloco 2 - Cálculos e Resultados
bloco1, bloco2, bloco3 = st.columns(3)

# Passo 1: Cálculo da relação entre vazão e rotação
with bloco1:
    st.header('🔄 Relação Vazão vs Rotação')
    Q2 = Q1 * (N2 / N1)
    st.metric("Vazão Poço 2 [bpd]", f"{Q2:.2f}", help="Vazão ajustada de acordo com a rotação da bomba no Poço 2")

# Passo 2: Correção da vazão pela viscosidade
with bloco2:
    st.header('🧪 Correção pela Viscosidade')
    Q2_corri = Q2 * (mi1 / mi2) ** n
    st.metric("Vazão Corrigida [bpd]", f"{Q2_corri:.2f}", delta=f"{Q2 - Q2_corri:.2f}", delta_color="inverse", help="Correção aplicada para a diferença de viscosidade")

# Passo 3: Correção pelo diâmetro da coluna
with bloco3:
    st.header('🔧 Correção pelo Diâmetro')
    Q2_final = Q2_corri * (Di2 / Di1) ** 2
    st.metric("Vazão Final Poço 2 [bpd]", f"{Q2_final:.2f}", delta=f"{Q2_corri - Q2_final:.2f}", delta_color="inverse", help="Correção final de acordo com o diâmetro da coluna")

# Separador visual
st.divider()

# Bloco final - Considerações adicionais
st.subheader('📌 Observações sobre os resultados:')
st.markdown(
    """
    - **Ajuste de Rotação:** A vazão de produção no Poço 2 foi ajustada proporcionalmente à rotação da bomba.
    - **Correção pela Viscosidade:** A viscosidade do óleo afeta a vazão significativamente, com correção aplicada via fator empírico.
    - **Correção pelo Diâmetro da Coluna:** O diâmetro da coluna de produção também impacta a vazão final, sendo corrigido para refletir mudanças nas dimensões da coluna.
    """
)

# Conclusão final
st.info('✅ Os cálculos foram realizados com sucesso e exibidos acima.')
