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
    st.title("Portifólio")
    st.write("De Matheus Santos Saraiva")
    st.markdown("""

# 👋 Sobre Mim

Olá! Meu nome é **[Seu Nome]** e sou estudante da área de tecnologia, com foco em **Ciência de Dados, Análise de Dados e Desenvolvimento de Soluções Digitais**.

Atualmente curso o Técnico em Ciência de Dados no Senac Nações Unidas, onde desenvolvo projetos voltados para análise, visualização e interpretação de dados, utilizando ferramentas modernas do mercado.

Tenho interesse especial em transformar dados em informações úteis para apoiar tomadas de decisão. Ao longo da minha formação, venho desenvolvendo dashboards interativos, aplicações web com Python e projetos que unem tecnologia, negócios e análise de dados.

Neste portfólio apresento alguns dos trabalhos que desenvolvi, incluindo dashboards analíticos, estudos de dados e o projeto **Data Byte**, uma plataforma educacional criada para tornar o aprendizado de Ciência de Dados mais acessível e interativo.

---

## 🚀 Principais Competências

* Python
* Ciência de Dados
* Análise de Dados
* Streamlit
* Pandas
* NumPy
* Plotly
* SQL
* Git e GitHub
* Visualização de Dados
* Desenvolvimento de Dashboards

---

## 🎯 Objetivos

Meu objetivo é construir uma carreira sólida na área de tecnologia, aprofundando meus conhecimentos em Ciência de Dados, Inteligência Artificial e Engenharia de Software.

Busco constantemente aprender novas tecnologias, desenvolver projetos cada vez mais completos e aplicar o conhecimento adquirido para resolver problemas reais através dos dados.

Obrigado por visitar meu portfólio!
""")


elif menu == "Data Byte":
    st.title("🧠 Data Byte")
    st.write("Plataforma educacional de dados")
    st.markdown("""
    

## 📌 Visão Geral

O **Data Byte** é uma plataforma interativa desenvolvida com o objetivo de tornar o aprendizado de Ciência de Dados mais acessível, visual e prático.

O projeto foi criado para reunir conceitos fundamentais da área em um ambiente intuitivo, permitindo que usuários explorem conteúdos, análises e visualizações de dados de forma dinâmica.

A proposta surgiu da percepção de que muitos estudantes encontram dificuldades para conectar teoria e prática. Dessa forma, o Data Byte busca reduzir essa distância por meio de dashboards interativos, exemplos práticos e exploração de dados.

---

## 🚀 Como o Projeto Foi Desenvolvido

O desenvolvimento foi realizado utilizando **Python** como tecnologia principal, aproveitando seu amplo ecossistema voltado para análise de dados e desenvolvimento de aplicações.

A interface foi construída com **Streamlit**, permitindo criar uma experiência web moderna e interativa. Para manipulação e tratamento dos dados foi utilizada a biblioteca **Pandas**, enquanto **NumPy** auxiliou em cálculos e simulações.

As visualizações foram desenvolvidas com **Plotly**, proporcionando gráficos dinâmicos e interativos para melhor interpretação das informações.

---

## 🛠️ Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* Git
* GitHub
* Streamlit Cloud

---

## 📊 Funcionalidades

✅ Interface web interativa

✅ Visualização de dados em tempo real

✅ Gráficos dinâmicos e intuitivos

✅ Demonstrações práticas de Ciência de Dados

✅ Estrutura escalável para novos módulos

---

## 🎯 Aprendizados Obtidos

Durante o desenvolvimento do Data Byte foram aplicados conhecimentos de:

* Programação em Python
* Ciência de Dados
* Visualização de Dados
* Desenvolvimento Web
* Versionamento com Git
* Deploy de aplicações em nuvem

---

## 💡 Conclusão

O Data Byte representa a união entre educação e tecnologia, demonstrando como ferramentas modernas de Ciência de Dados podem ser utilizadas para criar experiências de aprendizado mais envolventes e eficazes.

Além de servir como plataforma educacional, o projeto evidencia competências em desenvolvimento de software, análise de dados e construção de dashboards interativos.
""")

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
