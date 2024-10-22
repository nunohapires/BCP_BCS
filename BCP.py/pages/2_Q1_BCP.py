import streamlit as st
import numpy as np

# Configuração da página
st.set_page_config(
    page_title="Projeto BCP",
    page_icon="⚙",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar com a imagem e descrição do autor
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
st.title('Projeto BCP ⚙🛢')
st.subheader('Unidade de Bombeio')

# Separador visual
st.divider()

# Seção de entrada de dados
st.subheader('🔧 Características do Fluido e Dados Iniciais')

col1, col2 = st.columns(2)

with col1:
    d_relativa = st.number_input('🔷 Densidade Relativa', value=0.8, help="Densidade relativa do fluido")
    Mo = st.number_input('🔷 Viscosidade do Óleo [Pa.s]', value=10, help="Viscosidade do óleo em Pascal-segundo")
    dp = st.number_input('🔷 Delta de Pressão [Psi]', value=600, help="Diferença de pressão aplicada")
    di = st.number_input('🔷 Diâmetro Interno [pol]', value=3.75, help="Diâmetro interno da tubulação")

with col2:
    N = st.number_input('🔷 Rotação da Bomba [rpm]', value=300, help="Velocidade de rotação da bomba")
    Ps = st.number_input('🔷 Passo do Estator [mm]', value=180, help="Distância de um ciclo completo do estator") * 1/25.4  # Convertendo para polegadas
    e = st.number_input('🔷 Excentricidade [mm]', value=4, help="Distância de deslocamento") * 1/25.4  # Convertendo para polegadas

# Cálculos do deslocamento, torque e potência
PD = 4 * e * di * Ps  # Deslocamento da bomba (bbl/d)
Th = 0.111 * PD * dp  # Torque sobre a bomba (lbf.ft)
Pot = 0.000191 * Th * N  # Potência da bomba (Hp)

# Separador visual
st.divider()

# Exibição dos resultados de Deslocamento, Torque e Potência
st.subheader('📊 Resultados de Desempenho da Bomba')
col1, col2, col3 = st.columns(3)

col1.metric("Deslocamento da Bomba", f"{PD:.2f} bbl/d", help="Volume deslocado pela bomba por dia")
col2.metric("Torque sobre a Bomba", f"{Th:.2f} lbf.ft", help="Força rotacional sobre a bomba")
col3.metric("Potência da Bomba", f"{Pot:.2f} hp", help="Potência necessária para o funcionamento da bomba")

# Separador visual
st.divider()

# Seção para capacidade de gerar pressão
st.subheader('🔧 Capacidade de Gerar Pressão')

cavidade = Ps / 2
option = st.selectbox("Quantos Módulos serão Utilizados?", ["Single Lobe", "Dual Lobe", "Multi Lobe"])

# Condicional para o tipo de módulo selecionado
if option == 'Single Lobe':
    capacidade = 4.5 * 14.696
elif option == 'Dual Lobe':
    capacidade = 1.5 * 4.5 * 14.696
else:
    capacidade = 2 * 4.5 * 14.696

st.metric("Capacidade", f"{capacidade:.2f} Psi/cavidade", help="Capacidade de pressão gerada por cavidade")

# Separador visual
st.divider()

# Cálculo do número de estágios
st.subheader('🔧 Cálculo do Número de Estágios')

z = st.number_input('🔷 Tamanho do Poço [m]', value=1100, help="Profundidade do poço em metros") * 3.281  # Convertendo para pés
Ne = (z / Ps) - 1
st.metric("Número de Estágios", f"{Ne:.0f}", help="Número de estágios necessários para a operação da bomba")

# Separador visual
st.divider()

# Cálculo do Head da bomba
st.subheader('🔧 Head da Bomba')

P_cabeca = (2 * N - 1) * capacidade
st.metric("Head da Bomba", f"{P_cabeca:.2f} Psi", help="Pressão máxima gerada na cabeça da bomba")

# Separador visual
st.divider()

# Cálculo da Carga Axial de Rolamento
st.subheader('🔧 Carga Axial de Rolamento')

Fb = ((np.pi) / 4) * ((2 * e + di)**2) * P_cabeca
st.metric("Carga Axial de Rolamento", f"{Fb:.2f} lbf", help="Força axial atuante sobre o rolamento")

# Separador visual
st.divider()

# Cálculo da Carga Axial Total
st.subheader('🔧 Carga Axial Total')

peso_especifico = st.number_input('🔷 Peso Específico [lbf/ft³]', value=490, help="Peso específico do material")
Area = np.pi * ((di / 12) / 2)**2
Wr = z * Area * peso_especifico
F = Fb + Wr
st.metric("Carga Axial Total", f"{F:.2f} lbf", help="Força axial total atuante na bomba")

# Separador visual
st.divider()

# Cálculo da Tensão Axial Total
st.subheader('🔧 Tensão Axial Total (psi)')

vo = 0.028 * di * e * Ps
T = (vo * P_cabeca) / e
sig = (4 / (np.pi * di**3)) * np.sqrt(F**2 * di**2 + T**2)

st.metric("Tensão Axial Total", f"{sig:.2f} psi", help="Tensão axial total exercida sobre a bomba")

# Separador final
st.divider()

# Considerações finais e rodapé
st.info("✅ Todos os cálculos foram realizados com sucesso. Confira os resultados nas métricas acima.")
st.markdown("*Se precisar de mais informações ou ajustes, consulte o engenheiro responsável pelo projeto.*")
