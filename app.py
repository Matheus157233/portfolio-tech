import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from sklearn.linear_model import LinearRegression

# =========================
# TÍTULO
# =========================
st.title("📊 Dashboard de Vendas - Premium")

# =========================
# DADOS SIMULADOS REALISTAS
# =========================
np.random.seed(42)

dias = pd.date_range(start="2025-01-01", periods=180)

df = pd.DataFrame({
    "data": dias,
    "produto": np.random.choice(["Notebook", "Mouse", "Teclado", "Monitor", "Headset"], len(dias)),
    "categoria": np.random.choice(["Hardware", "Acessórios", "Periféricos"], len(dias)),
    "quantidade": np.random.randint(1, 20, len(dias)),
    "preco": np.random.randint(50, 5000, len(dias))
})

df["receita"] = df["quantidade"] * df["preco"]

# =========================
# KPIs
# =========================
col1, col2, col3 = st.columns(3)

col1.metric("💰 Receita Total", f"R$ {df['receita'].sum():,.0f}")
col2.metric("📦 Total Vendas", df["quantidade"].sum())
col3.metric("🎯 Ticket Médio", f"R$ {df['receita'].mean():,.2f}")

st.divider()

# =========================
# GRÁFICO 1 - EVOLUÇÃO
# =========================
st.subheader("📈 Evolução da Receita")

df_line = df.groupby("data")["receita"].sum().reset_index()

fig_line = px.line(
    df_line,
    x="data",
    y="receita",
    title="Receita ao longo do tempo"
)

st.plotly_chart(fig_line, use_container_width=True)

# =========================
# GRÁFICO 2 - PIZZA CATEGORIA
# =========================
st.subheader("🍕 Receita por Categoria")

df_cat = df.groupby("categoria")["receita"].sum().reset_index()

fig_pie_cat = px.pie(
    df_cat,
    names="categoria",
    values="receita",
    title="Distribuição por Categoria"
)

st.plotly_chart(fig_pie_cat, use_container_width=True)

# =========================
# GRÁFICO 3 - PIZZA PRODUTO
# =========================
st.subheader("🍕 Receita por Produto")

df_prod = df.groupby("produto")["receita"].sum().reset_index()

fig_pie_prod = px.pie(
    df_prod,
    names="produto",
    values="receita",
    title="Distribuição por Produto"
)

st.plotly_chart(fig_pie_prod, use_container_width=True)

# =========================
# PREVISÃO SIMPLES (ML)
# =========================
st.subheader("🔮 Previsão de Receita")

df_model = df.groupby("data")["receita"].sum().reset_index()
df_model["dia"] = np.arange(len(df_model))

X = df_model[["dia"]]
y = df_model["receita"]

model = LinearRegression()
model.fit(X, y)

# prever próximos 30 dias
future_days = np.arange(len(df_model), len(df_model) + 30).reshape(-1, 1)
future_pred = model.predict(future_days)

df_future = pd.DataFrame({
    "dia": future_days.flatten(),
    "previsao": future_pred
})

fig_pred = px.line()

fig_pred.add_scatter(
    x=df_model["dia"],
    y=df_model["receita"],
    mode="lines",
    name="Histórico"
)

fig_pred.add_scatter(
    x=df_future["dia"],
    y=df_future["previsao"],
    mode="lines",
    name="Previsão"
)

st.plotly_chart(fig_pred, use_container_width=True)

# =========================
# INSIGHTS AUTOMÁTICOS
# =========================
st.subheader("🧠 Insights Automáticos")

top_prod = df_prod.sort_values("receita", ascending=False).iloc[0]
top_cat = df_cat.sort_values("receita", ascending=False).iloc[0]

st.success(f"""
📌 Produto mais forte: {top_prod['produto']}  
📌 Categoria dominante: {top_cat['categoria']}  
💰 Maior impacto vem da categoria com maior receita.
""")

st.info("Modelo de previsão simples baseado em regressão linear (baseline).")
