import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Data Portfolio",
    page_icon="📊",
    layout="wide"
)

# =========================
# MENU PRINCIPAL (ABAS)
# =========================
menu = st.sidebar.radio(
    "📂 Navegação",
    ["👤 Quem sou eu", "📁 Trabalhos feitos", "🧠 Data Byte", "📊 Dashboard de Vendas", "💰 Dashboard Financeiro"]
)

# =========================
# 👤 QUEM SOU EU
# =========================
if menu == "👤 Quem sou eu":

    st.title("👨‍💻 Sobre mim")

    st.write("""
    Sou estudante e desenvolvedor focado em Ciência de Dados.

    Trabalho com:
    - Análise de dados
    - Criação de dashboards
    - Visualização de dados
    - Python e Streamlit
    """)

    st.divider()

    st.subheader("⚙️ Tecnologias")
    st.write("Python | Pandas | NumPy | Plotly | Streamlit")

    st.success("Foco: transformar dados em decisões reais de negócio")


# =========================
# 📁 TRABALHOS FEITOS
# =========================
elif menu == "📁 Trabalhos feitos":

    st.title("📁 Meus Projetos")

    st.subheader("🧠 Data Byte")
    st.write("Plataforma educacional de Ciência de Dados.")
    st.write("🔗 Aqui você vai colocar o link do Streamlit Cloud")
    st.write("📸 Aqui você pode adicionar prints do projeto")

    st.markdown("---")

    st.subheader("📊 Dashboard de Vendas")
    st.write("Análise de vendas com KPIs e gráficos interativos.")
    st.write("Tecnologias: Python, Pandas, Plotly, Streamlit")

    st.markdown("---")

    st.subheader("💰 Dashboard Financeiro")
    st.write("Controle financeiro com análise de receitas e despesas.")
    st.write("Tecnologias: Python, Pandas, Plotly, Streamlit")


# =========================
# 🧠 DATA BYTE
# =========================
elif menu == "🧠 Data Byte":

    st.title("🧠 Data Byte")

    st.write("""
    Plataforma interativa de aprendizado em Ciência de Dados.

    👉 Projeto focado em transformar teoria em prática visual.
    """)

    st.info("🔗 Adicione aqui o link do seu projeto no Streamlit Cloud")

    st.success("📸 Espaço para prints do sistema")

    st.write("Tecnologias usadas: Python, Streamlit, Pandas")


# =========================
# 📊 DASHBOARD DE VENDAS (REAL)
# =========================
elif menu == "📊 Dashboard de Vendas":

    st.title("📊 Dashboard de Vendas")

    # ===== DADOS SIMULADOS REALISTAS =====
    np.random.seed(42)

    df = pd.DataFrame({
        "data": pd.date_range(start="2025-01-01", periods=150),
        "produto": np.random.choice(["Notebook", "Mouse", "Teclado", "Monitor", "Headset"], 150),
        "categoria": np.random.choice(["Hardware", "Acessórios"], 150),
        "vendas": np.random.randint(1, 15, 150),
        "preco_unit": np.random.randint(50, 4000, 150)
    })

    df["receita"] = df["vendas"] * df["preco_unit"]

    # ===== KPIs =====
    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Receita Total", f"R$ {df['receita'].sum():,.0f}")
    col2.metric("📦 Vendas Totais", df["vendas"].sum())
    col3.metric("🎯 Ticket Médio", f"R$ {df['receita'].mean():,.2f}")

    st.divider()

    # ===== GRÁFICO 1 =====
    st.subheader("📈 Receita ao longo do tempo")

    fig1 = px.line(df, x="data", y="receita", title="Evolução da Receita")
    st.plotly_chart(fig1, use_container_width=True)

    # ===== GRÁFICO 2 =====
    st.subheader("📊 Receita por Produto")

    prod = df.groupby("produto")["receita"].sum().reset_index()

    fig2 = px.bar(prod, x="produto", y="receita", title="Produtos mais lucrativos")
    st.plotly_chart(fig2, use_container_width=True)

    # ===== INSIGHTS =====
    st.subheader("🧠 Insights automáticos")

    top_produto = prod.sort_values("receita", ascending=False).iloc[0]

    st.success(f"""
    📌 Produto mais lucrativo: {top_produto['produto']}  
    💰 Receita gerada: R$ {top_produto['receita']:,.0f}
    """)


# =========================
# 💰 DASHBOARD FINANCEIRO (BASE)
# =========================
elif menu == "💰 Dashboard Financeiro":

    st.title("💰 Dashboard Financeiro")

    df = pd.DataFrame({
        "mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
        "receita": [5000, 7000, 6500, 8000, 9000, 11000],
        "despesa": [3000, 3500, 4000, 4200, 5000, 6000]
    })

    df["lucro"] = df["receita"] - df["despesa"]

    fig = px.bar(df, x="mes", y=["receita", "despesa"], barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    st.line_chart(df.set_index("mes")["lucro"])
