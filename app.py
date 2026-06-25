import streamlit as st

st.set_page_config(
    page_title="Data Portfolio",
    page_icon="📊",
    layout="wide"
)

# MENU LATERAL (MÓDULOS)
menu = st.sidebar.selectbox(
    "📂 Navegação",
    ["Home", "Data Byte", "Dashboard de Vendas", "Dashboard Financeiro"]
)

# =========================
# HOME
# =========================
if menu == "Home":
    st.title("📊 Meu Portfólio de Dados")
    st.subheader("Projetos em Ciência de Dados com Python")

    st.write("""
    Bem-vindo ao meu portfólio.

    Aqui você encontra projetos de:
    - Análise de dados
    - Dashboards interativos
    - Visualização de dados
    """)

    st.success("Selecione um projeto na barra lateral 👈")


# =========================
# DATA BYTE
# =========================
elif menu == "Data Byte":
    st.title("🧠 Data Byte")
    st.subheader("Plataforma educacional de Ciência de Dados")

    col1, col2 = st.columns(2)

    with col1:
        st.header("📌 Sobre")
        st.write("""
        Plataforma criada para ensino prático de Ciência de Dados com Python e Streamlit.
        """)

    with col2:
        st.header("⚙️ Tecnologias")
        st.write("- Python\n- Streamlit\n- Pandas\n- Plotly")

    st.divider()

    st.header("🎯 Problema")
    st.write("Ensinar Ciência de Dados de forma visual e prática.")

    st.info("Aqui você pode adicionar prints do projeto depois")


# =========================
# DASHBOARD VENDAS
# =========================
elif menu == "Dashboard de Vendas":
    st.title("📈 Dashboard de Vendas")

    st.write("Projeto ainda em construção...")

    st.info("Aqui vamos colocar KPIs, gráficos e insights reais")


# =========================
# DASHBOARD FINANCEIRO
# =========================
elif menu == "Dashboard Financeiro":
    st.title("💰 Dashboard Financeiro")

    st.write("Projeto ainda em construção...")

    st.info("Controle de receitas, despesas e lucro")
