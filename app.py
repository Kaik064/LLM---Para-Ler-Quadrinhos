import streamlit as st
from main import analisarQuadrinho

st.title ("LLM para ler quadrinhos")

st.write (
    "Envie uma imagem de quadrinhos para ser lida com IA."
)

uploaded_file = st.file_uploader(
    "Envie uma imagem",
    type=["jpeg","jpg","png","webp"]
)
if uploaded_file is not None:    
    st.image(uploaded_file)

    st.write (
        "-- IA analisando quadrinho --"
    )

    resposta_Da_Ia = analisarQuadrinho(uploaded_file)

    st.subheader(
        "-- O quadrinho enviado possui a seguinte história --"
    )

    st.markdown(
        f"""
        <div style ="
        border: 2px solid white;
        padding: 20px;
        border-radius:10px;
        background-color#1e1e1e;
        ">
            {resposta_Da_Ia}
        </div>
        """,
        unsafe_allow_html= True
    )
