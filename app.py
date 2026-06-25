import streamlit as st

st.set_page_config(
    page_title="Data Portfolio",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Portfolio")
st.subheader("Transformando dados em decisões")

st.write("""
Bem-vindo ao meu portfólio de projetos em Ciência de Dados.

Aqui você vai encontrar dashboards, análises e aplicações criadas com Python e Streamlit.
""")

st.markdown("### 📌 Projetos")
st.write("- Data Byte")
st.write("- Dashboard de Vendas")
st.write("- Dashboard Financeiro")

st.success("Escolha um projeto no menu lateral 👈")
