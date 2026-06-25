import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression
import hashlib
from supabase import create_client

SUPABASE_URL = "https://qzegvxfsyxklezbxhxbt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF6ZWd2eGZzeXhrbGV6YnhoeGJ0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MjQxNTE1OCwiZXhwIjoyMDk3OTkxMTU4fQ.jIHrymCIumRyJvY7FPiby5Dd5h3MCDRTbNF7oY_2Zdo"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(email, password):
    try:
        result = supabase.table("users").insert({
            "email": email,
            "password": hash_password(password)
        }).execute()

        st.write(result)
        return True

    except Exception as e:
        st.error(f"Erro: {e}")
        return False

def login_user(email, password):
    res = supabase.table("users") \
        .select("*") \
        .eq("email", email) \
        .eq("password", hash_password(password)) \
        .execute()

    return len(res.data) > 0

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    
if "user" not in st.session_state:
    st.session_state.user = None

def auth_page():
    st.title("🔐 Data Portfolio SaaS")

    tab1, tab2 = st.tabs(["Login", "Cadastro"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            if login_user(email, password):
                st.session_state.logged_in = True
                st.session_state.user = email
                st.rerun()
            else:
                st.error("Login inválido")
                
    with tab2:
        new_email = st.text_input("Novo email")
        new_password = st.text_input("Nova senha", type="password")

        if st.button("Criar conta"):
            if register_user(new_email, new_password):
                st.success("Conta criada!")
            else:
                st.error("Erro ao criar conta")

def logout():

    if st.session_state.user:
        st.sidebar.write(f"👤 {st.session_state.user}")

    if st.sidebar.button("Sair"):
        st.session_state.logged_in = False
        st.session_state.user = None
        st.rerun()

    if not st.session_state.logged_in:
        auth_page()
        st.stop()
    
menu = st.sidebar.radio(
    "📂 Navegação",
    ["Home", "Data Byte", "Dashboard de Vendas", "Dashboard Financeiro"]
)

logout()

if menu == "Home":
    st.title("📊 Data Portfolio SaaS")
    st.write("Sistema de análise de dados estilo startup")

elif menu == "Data Byte":
    st.title("🧠 Data Byte")
    st.write("Plataforma educacional de dados")

elif menu == "Dashboard de Vendas":

    st.title("📊 Sales Dashboard")

    np.random.seed(42)

    df = pd.DataFrame({
        "data": pd.date_range("2025-01-01", periods=200),
        "produto": np.random.choice(["Notebook", "Mouse", "Teclado"], 200),
        "categoria": np.random.choice(["Hardware", "Acessórios"], 200),
        "qtd": np.random.randint(1, 10, 200),
        "preco": np.random.randint(100, 3000, 200)
    })

    df["receita"] = df["qtd"] * df["preco"]

    st.metric("Receita", f"R$ {df['receita'].sum():,.0f}")

    # pizza categoria
    cat = df.groupby("categoria")["receita"].sum().reset_index()
    fig1 = px.pie(cat, names="categoria", values="receita")
    st.plotly_chart(fig1)

    # pizza produto
    prod = df.groupby("produto")["receita"].sum().reset_index()
    fig2 = px.pie(prod, names="produto", values="receita")
    st.plotly_chart(fig2)

    # previsão
    df_ml = df.groupby("data")["receita"].sum().reset_index()
    df_ml["x"] = np.arange(len(df_ml))

    model = LinearRegression()
    model.fit(df_ml[["x"]], df_ml["receita"])

    future = np.arange(len(df_ml), len(df_ml)+30).reshape(-1,1)
    pred = model.predict(future)

    st.line_chart(df_ml.set_index("data")["receita"])

elif menu == "Dashboard Financeiro":

    st.title("💰 Financeiro")

    df = pd.DataFrame({
        "mes": ["Jan","Fev","Mar","Abr"],
        "receita": [5000,7000,9000,11000],
        "despesa": [3000,4000,5000,6000]
    })

    df["lucro"] = df["receita"] - df["despesa"]

    st.bar_chart(df.set_index("mes")[["receita","despesa"]])
    st.line_chart(df.set_index("mes")["lucro"])
