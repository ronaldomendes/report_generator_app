import streamlit as st

st.set_page_config(layout="wide")

html_code = """
<style>
    footer {visibility: hidden;}
    # header {visibility: hidden;}
    div.block-container{padding: 2rem;}
</style>
<h1>Gerador de relatório</h1>
"""
st.markdown(html_code, unsafe_allow_html=True)

form = st.form("my_form", clear_on_submit=True, border=False)
exp1 = form.expander(expanded=True, label='**Descrição Resumida**')
q1 = exp1.text_input(label='Resumo')

exp2 = form.expander(expanded=True, label='**Descrição Geral**')
q2 = exp2.text_input(label='O que será feito?')
q3 = exp2.text_input(label='Por que será feito?')
q4 = exp2.text_input(label='Resultado esperado?')
q5 = exp2.text_input(label='Mudança Funcional ou Técnica?')
q6 = exp2.text_input(label='Comunicação com a área afetada anexa?')

exp3 = form.expander(expanded=True, label='**Impacto de Implantação**')
q7 = exp3.text_input(label='Qual o possível impacto no ambiente durante a execução da mudança?')
q8 = exp3.text_input(label='Em caso de falha, quais serviços podem ser afetados e qual o impacto na rotina do usuário?')
q9 = exp3.text_input(label='Qual o impacto para o negócio se a mudança não for realizada?')
q10 = exp3.text_input(label='Impactos em caso de Rollback')

exp4 = form.expander(expanded=True, label='**Plano de Implementação**')
q11 = exp4.text_area(label='Descrição de implementação (separado por uma nova linha)')

exp5 = form.expander(expanded=True, label='**Plano de Retorno (Rollback)**')
q12 = exp5.text_area(label='Descrição de retorno (separado por uma nova linha)')

submit = form.form_submit_button("Gerar", use_container_width=True, type='primary')

if submit:
    st.markdown(f"""
    #### 1. **Descrição Resumida:**
    {q1}

    #### 2. **Descrição:**

    - **O que será feito?:** {q2}
    - **Por que será feito?:** {q3}
    - **Resultado esperado:** {q4}
    - **Mudança Funcional ou Técnica:** {q5}
    - **Comunicação com a área afetada anexa:** {q6}

    #### 3. **Impacto de Implantação:**

    - **Qual o possível impacto no ambiente durante a execução da mudança?** {q7}
    - **Em caso de falha, quais serviços podem ser afetados e qual o impacto na rotina do usuário?** {q8}
    - **Qual o impacto para o negócio se a mudança não for realizada?** {q9}
    - **Impactos em caso de Rollback:** {q10}

    #### 4. **Plano de Implementação:**
    <ul>{''.join(str(f'<li>{line}</li>') for line in q11.splitlines())}</ul>

    #### 5. **Plano de Retorno (Rollback):**
    <ul>{''.join(str(f'<li>{line}</li>') for line in q12.splitlines())}</ul>
""", unsafe_allow_html=True)
