import streamlit as st
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Projeto BCS",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar com imagem e créditos
st.sidebar.image('logo_nuno.jpg')
st.sidebar.markdown(
    """
    **Desenvolvido por:**
    - *Nuno Henrique Albuquerque Pires*
    - Estudante de Engenharia de Petróleo
    - Universidade Federal de Alagoas (UFAL)
    """
)

# Título da página
st.title('Projeto BCS ⚙🛢')
st.subheader('Unidade de Bombeio Centrífugo Submerso')

# Separador visual
st.divider()

# Descrição do problema
st.header('Dimensionamento do Sistema de Bombeio Centrífugo Submerso (BCS)')
st.write("""
Vamos calcular os parâmetros de dimensionamento de um sistema de BCS com base nos dados fornecidos pelo usuário.
Preencha os campos abaixo com os valores adequados para obter os resultados.
""")

# Seção de entrada de dados
st.subheader('📋 Dados de Entrada')

col1, col2, col3 = st.columns(3)

with col1:
    Hs = st.number_input('🔹 Profundidade [ft]', value=7000) / 3.281  # Convertendo para metros
    Q = st.number_input('🔹 Vazão de Produção [ft³/s]', value=0.2)

with col2:
    d_relativa = st.number_input('🔹 Densidade Relativa do Óleo', value=0.8)
    mio = st.number_input('🔹 Viscosidade do Óleo [Pa.s]', value=10)

with col3:
    delta_p = st.number_input('🔹 Diferença de Pressão [psi]', value=600)
    di = st.number_input('🔹 Diâmetro Interno da Linha [in]', value=3.75)

ef = st.number_input('🔹 Eficiência da Bomba [%]', value=80) / 100

# Separador visual
st.divider()

# Cálculo da Carga Manométrica
st.subheader('📊 Cálculo da Carga Manométrica')

densidade = d_relativa * 1000  # Convertendo para kg/m³
delta_p_total = delta_p * 6894.76  # Convertendo psi para Pa
H = Hs + (delta_p_total / (densidade * 9.81))  # Cálculo da carga manométrica

st.metric("🔸 Carga Manométrica", f"{H:.2f} m", help="Altura manométrica necessária para o funcionamento da bomba")

# Separador visual
st.divider()

# Cálculo da Potência da Bomba
st.subheader('⚡ Cálculo da Potência da Bomba')

Pb = ((densidade * 9.81 * (Q * 0.0283168) * H) / ef) / 745.7  # Convertendo Q para m³/s e potência para HP
st.metric("🔸 Potência da Bomba", f"{Pb:.2f} HP", help="Potência requerida pela bomba")

# Separador visual
st.divider()

# Efeito de aumento de perda de carga
st.subheader('📈 Efeito do Aumento de 60% na Perda de Carga')

perda = st.number_input('🔹 Aumento da Perda de Carga [%]', value=60) / 100
H_novo = H * (1 + perda)  # Nova altura manométrica com o aumento de 60% na perda de carga

st.metric("🔸 Nova Altura Manométrica", f"{H_novo:.2f} m", help="Altura manométrica considerando o aumento de perda de carga")

# Separador visual
st.divider()

# Relação entre Produção e Altura Manométrica
st.subheader('🔄 Relação entre Produção e Altura Manométrica')

Q_novo = (np.sqrt(H / H_novo) * (Q * 0.0283168)) * 35.315  # Convertendo Q de m³/s para ft³/s
st.metric("🔸 Nova Vazão de Produção", f"{Q_novo:.2f} ft³/s", delta=f"{Q:.2f} ft³/s", delta_color='inverse', help="Variação na vazão de produção devido ao aumento na perda de carga")

# Separador final
st.divider()

# Rodapé e considerações finais
st.info("✅ Todos os cálculos foram realizados com sucesso. Confira os resultados nas métricas acima.")
st.markdown("*Se precisar de mais informações ou ajustes, consulte o engenheiro responsável pelo projeto.*")
