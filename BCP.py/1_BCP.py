# Importações necessárias  
import streamlit as st 

# Configurações da página 
st.set_page_config(
    layout="wide",
    page_title="Projeto BCS - Home",
    initial_sidebar_state="expanded",
    page_icon="⚙",
)

# Cabeçalho e Sidebar
st.markdown("# Bem-vindo ao Projeto BCS! ⚙🛢") 
st.sidebar.image('logo_nuno.jpg', use_column_width=True)
st.sidebar.markdown("""
*Desenvolvido por*  
**Nuno Henrique Albuquerque Pires**  
*Estudante de Engenharia de Petróleo*  
[Universidade Federal de Alagoas]  
""")

# Expansível com mais informações
with st.expander("ℹ️ Informações Adicionais"):
    st.markdown("""
    - Este web app foi projetado para realizar cálculos e análises de dimensionamento em sistemas de **Bombeio Centrífugo Submerso (BCS)**.
    - Utiliza ferramentas de automação e cálculos baseados em métodos de engenharia, com uma interface interativa desenvolvida em **Streamlit**.
    - **Referência:** Guo, Boyun, Xinghui Liu, e Xuehao Tan. *Petroleum Production Engineering*, 2ª ed., Gulf Professional Publishing, 2017.
    [Acesse o livro aqui](https://www.amazon.com/Petroleum-Production-Engineering-Boyun-Guo/dp/0128093749)
    """)

# Descrição do projeto
st.markdown("""
### Sobre o Projeto

Este projeto foca no desenvolvimento e dimensionamento de sistemas de **Bombeio Centrífugo Submerso (BCS)**, amplamente usados na indústria de petróleo para a elevação artificial.  
Utilizando **Python** e o framework **Streamlit**, a plataforma automatiza os cálculos e oferece uma interface intuitiva para análises rápidas e precisas dos sistemas de BCS.  
Com base nas equações do livro *Petroleum Production Engineering, Second Edition*, os cálculos abordam desde a determinação da carga manométrica, potência da bomba, até a análise do efeito de variações de perda de carga.

#### Objetivos do Projeto:

- Simular as condições de operação de um sistema de BCS.
- Estimar a potência necessária para operação da bomba, considerando as variáveis de entrada fornecidas.
- Avaliar o impacto de mudanças nas condições operacionais, como aumento de perdas de carga e vazão.
- Fornecer visualizações claras para facilitar a tomada de decisões.
  
O objetivo é fornecer uma solução completa para estudantes e profissionais da área de engenharia de petróleo, que buscam um sistema de dimensionamento eficiente, customizável e de fácil utilização.

#### Características Principais:
- **Automação de Cálculos:** A plataforma automatiza o processo de cálculo para determinar a carga manométrica, a potência da bomba, e o efeito de variações operacionais.
- **Interface Amigável:** Todos os dados podem ser facilmente inseridos e visualizados através de uma interface gráfica simples e direta.
- **Análise de Cenários:** Inclui a possibilidade de simulação com diferentes cenários, como aumento da perda de carga e mudanças na vazão de produção.
""")

# Finalizando com uma chamada para ação
st.info("🔧 Explore a aba lateral para começar os cálculos ou simular diferentes cenários no dimensionamento de um sistema BCS.")

