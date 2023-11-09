import streamlit as st
import gettext
_ = gettext.gettext

# Título do aplicativo  
st.title("Luís Eduardo Moreira Las Casas")

# URL do seu perfil do LinkedIn
linkedin_url = "https://www.linkedin.com/in/luis-las-casas"

# URL do seu perfil do GitHub
github_url = "https://github.com/dudumlc?tab=repositories"

# Endereço de e-mail
email = "dudu_las-casas@hotmail.com"

# URL do Currículo.pdf
cv = "https://docs.google.com/document/d/13UirL45gQSGSO2MXnev8SQXPdrNAQ9LB/edit?usp=drive_link&ouid=110879567570363521349&rtpof=true&sd=true"

# HTML para criar links clicáveis com as imagens dos ícones e texto
html = f'''
<div style="display: inline-block; margin-right: 20px;">
    <a href="{linkedin_url}" target="_blank">
        <img src="https://cdn.icon-icons.com/icons2/2248/PNG/512/linkedin_icon_135436.png" alt="LinkedIn" width="40">
    </a>
    <p style="text-align: center;"></p>
</div>
<div style="display: inline-block; margin-right: 20px;">
    <a href="{github_url}" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="32">
    </a>
    <p style="text-align: center;"></p>
</div>
<div style="display: inline-block; margin-right: 20px;">
    <a href="mailto:{email}" target="_blank">
        <img src="https://cdn-icons-png.flaticon.com/512/725/725643.png" alt="E-mail" width="32">
    </a>
    <p style="text-align: center;"></p>
</div>
<div style="display: inline-block;">
    <a href="{cv}" target="_blank">
        <img src="https://icon-library.com/images/curriculum-icon/curriculum-icon-15.jpg" alt="Cv" width="32">
    </a>
    <p style="text-align: center;"></p>
</div>
'''

# Renderize o HTML usando st.markdown
st.markdown(html, unsafe_allow_html=True)

# Menu lateral com quatro opções
#url_imagem = ""

#st.sidebar.markdown(f'<img src="{url_imagem}" width="200">', unsafe_allow_html=True)
#menu_opcao = st.sidebar.selectbox("Sections", ["About me", "Education", "Professional experience", "Projects"], format_func=lambda x: x)


aboutme, education, profExperience, projects = st.tabs(["ABOUT ME", "EDUCATION", 'PROFESSIONAL EXPERIENCE', 'PROJECTS'])

# Conteúdo sobre meu perfil
aboutme.header("Personal Informations")
aboutme.write("**Nationality:** *Brazilian*⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ **Date of Birth:** *October 10th, 2002*")

aboutme.header("Description")
aboutme.write("""Organized, dedicated and ambitious professional with excellent attention to detail, 
             and thirst for learning. Interested in working closely with experienced data scientists 
             and contribute to the success of the company's projects. Seeking an entry-level position 
             to begin my data career in a high-level professional environment, where I can utilize my 
             skills and studies background to the maximum and learn day by day with my coworkers about 
             data science and data engineering.
             """)

# Conteúdo sobre minha educação
education.header("Education")

education.markdown('**<span style="color: #F44E3F;">Bachelor of Accountings</span>**', unsafe_allow_html=True)

education.write('Universidade Federal de Minas Gerais (UFMG) - Belo Horizonte, BR⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ Conclusion (Expected Date): 2025')

education.markdown('**<span style="color: #F44E3F;">Specialization in Data Science</span>**', unsafe_allow_html=True)
education.write('Escola DNC - São Paulo, BR')

# Conteúdo sobre minha experiência profissional
profExperience.header("Professional experience")

profExperience.markdown('**<span style="color: #F44E3F;">Data Analysis Intern, ArcelorMittal Brasil - Belo Horizonte, BR</span>**', unsafe_allow_html=True)

profExperience.write('July 2023 - Present')

profExperience.markdown('**<span style="color: #F44E3F;">Finance Intern, Wabtec Corporation - Contagem, BR</span>**', unsafe_allow_html=True)

profExperience.write('July 2022 - July 2023')

profExperience.write("""Assisted with month-end closing processes. Responsible for the monthly invoicing process of one of the company's 
                     most important contracts. Create routine financial reports to track and analyze customer payment of invoices. 
                     Create dashboards to data visualization. Responsible for automating some manual tasks.
                     """)

profExperience.markdown('**<span style="color: #F44E3F;">Search and Mapping Agent, Instituto Brasileiro de Geografia e Estatística (IBGE) - Belo Horizonte, BR</span>**', unsafe_allow_html=True)

profExperience.write('July 2021 - July 2022')

profExperience.write("""I was part of the supervision of economic research in Minas Gerais, BR and in charge of three researches
                     (PIA Produto, IPP and PMS). Responsible for criticizing and analyzing the data sent by the companies in the surveys and 
                     in charge of find and correct incorrect values ​​entered, such as outliers, to clean the database and not compromise the final 
                     result of the surveys. Controlled the deadlines for survey responses and maintained direct contact with companies to ensure it.
                     """)

# Conteúdo sobre meus projetos
projects.header("Projects")
projects.markdown('**<span style="color: #F44E3F;">AMBEV - Water Consumption Tracking Dashboard</span>**', unsafe_allow_html=True)
projects.write("Dashboard to Ambev for tracking the water consumption of the company and analyzing the metrics.")
projects.markdown('**<span style="color: #F44E3F;">Churn Prediction</span>**', unsafe_allow_html=True)
projects.write("Classification and prediction of customers who will stop consuming an establishment's service.")
projects.markdown('**<span style="color: #F44E3F;">Kruskal Wallis Test - Relation between the public and the game result</span>**', unsafe_allow_html=True)
projects.write('Relationship between the number of spectators at a football game and the result of the match')
projects.markdown('**<span style="color: #F44E3F;">Sales Prediction - Forecast of the number of tickets to be sold at a football match</span>**', unsafe_allow_html=True)
projects.write('Prediction of the number of tickets to be sold at a football match.')