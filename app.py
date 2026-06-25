import streamlit as st

st.set_page_config(
    page_title="Data Portfolio",
    page_icon="📊",
    layout="wide"
)

# ===== CSS PERSONALIZADO (visual SaaS) =====
st.markdown("""
<style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 0px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-top: 0px;
    }

    .card {
        padding: 20px;
        border-radius: 12px;
        background-color: #111827;
        color: white;
        margin-bottom: 15px;
    }

    .small-text {
        color: #9ca3af;
    }
</style>
""", unsafe_allow_html=True)

# ===== SIDEBAR =====
menu = st.sidebar.selectbox(
    "📂 Menu",
    ["Home", "Data Byte", "Dashboard de Vendas", "Dashboard Financeiro"]
)

# =========================
# HOME (STARTUP STYLE)
# =========================
if menu == "Home":

    st.markdown('<p class="main-title">📊 Data Portfolio</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Transformando dados em decisões de negócio</p>', unsafe_allow_html=True)

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <h3>🧠 Data Byte</h3>
        <p class="small-text">Plataforma educacional de dados</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h3>📈 Vendas</h3>
        <p class="small-text">Dashboard comercial</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <h3>💰 Financeiro</h3>
        <p class="small-text">Controle financeiro</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.success("Selecione um projeto no menu lateral 👈")


# =========================
# DATA BYTE
# =========================
elif menu == "Data Byte":

    st.title("🧠 Data Byte")

    st.write("Plataforma interativa de aprendizado em Ciência de Dados")

    st.divider()

    st.subheader("📌 O que você aprende aqui")

    st.markdown("""
    - Análise de dados na prática  
    - Visualização com Python  
    - Interpretação de dados reais  
    - Construção de dashboards  
    """)

    st.divider()
    
    st.subheader("📊 Exemplo de aplicação")
    
    st.info("Aqui você pode integrar notebooks, gráficos ou mini dashboards")
    
    st.success("Projeto focado em aprendizado prático e visual")

# =========================
# VENDAS
# =========================
elif menu == "Dashboard de Vendas":

    st.title("📈 Dashboard de Vendas")

    st.info("Projeto em construção — próximo nível será com gráficos reais")


# =========================
# FINANCEIRO
# =========================
elif menu == "Dashboard Financeiro":

    st.title("💰 Dashboard Financeiro")

    st.info("Controle de receitas, despesas e lucro")
