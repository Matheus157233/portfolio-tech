import streamlit as st

st.set_page_config(
    page_title="Data Portfolio",
    page_icon="📊",
    layout="wide"
)

# Título
st.title("📊 Meu Portfólio de Dados")
st.subheader("Transformando dados em insights e decisões")

st.divider()

# Sobre você
st.header("👨‍💻 Sobre mim")
st.write("""
Sou estudante de Ciência de Dados com foco em análise, visualização e criação de dashboards com Python e Streamlit.
Tenho projetos aplicados em dados reais e simulados, com foco em resolver problemas de negócio.
""")

st.divider()

# Projetos
st.header("📁 Projetos")

st.subheader("🧠 Data Byte")
st.write("Plataforma educacional interativa de Ciência de Dados.")
st.write("Tecnologias: Python, Streamlit, Pandas")

st.subheader("📊 Dashboard de Vendas")
st.write("Análise de vendas com KPIs, gráficos e insights de negócio.")

st.subheader("💰 Dashboard Financeiro")
st.write("Controle financeiro com receitas, despesas e lucro.")

st.divider()

# Contato
st.header("📞 Contato")
st.write("GitHub: seuusuario")
st.write("LinkedIn: seu-link-aqui")

st.success("Portfólio em construção 🚧")
