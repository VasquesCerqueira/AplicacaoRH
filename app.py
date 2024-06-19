from flask import Flask, render_template, request, redirect, url_for, flash
import pandas as pd
import os
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

def generate_resource_id():
    return str(random.randint(100, 999))

def skill_mapping(skill_value):
    mapping = {"Alta": 1, "Média": 2, "Baixa": 3}
    return mapping.get(skill_value, "")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    # Captura os dados do formulário
    Recurso = request.form.get('Recurso')
    Perfil = request.form.get('Perfil')
    Disponibilidade_DG = request.form.get('Disponibilidade_DG')
    Disponibilidade_IA = request.form.get('Disponibilidade_IA')
    Ingresso_ao_Time = request.form.get('Ingresso_ao_Time')
    Ate = request.form.get('Ate')
    Duracao = request.form.get('Duracao')
    Ano_de_ate = request.form.get('Ano_de_ate')
    email = request.form.get('email')
    Local_de_atuacao = request.form.get('Local_de_atuacao')
    Celular = request.form.get('Celular')
    Qtd_Atuacoes = request.form.get('Qtd_Atuacoes')
    Alocacao = request.form.get('Alocacao')
    reuniao_one_on_one = request.form.get('reuniao_one_on_one')
    gestor_one_on_one = request.form.get('gestor_one_on_one')
    Skill_Comunicacao = request.form.get('Skill_Comunicacao')
    Skill_DG = request.form.get('Skill_DG')
    Skill_IDMC_DG = request.form.get('Skill_IDMC_DG')
    Skill_IDMC_DQ = request.form.get('Skill_IDMC_DQ')
    Skill_Axon = request.form.get('Skill_Axon')
    Skill_EDC = request.form.get('Skill_EDC')
    Skill_TDM = request.form.get('Skill_TDM')
    Skill_DPM = request.form.get('Skill_DPM')
    Skill_DEI = request.form.get('Skill_DEI')
    Skill_DEQ = request.form.get('Skill_DEQ')
    Skill_PowerCenter = request.form.get('Skill_PowerCenter')
    Skill_Purview = request.form.get('Skill_Purview')
    Skill_Dataplex = request.form.get('Skill_Dataplex')
    Skill_Databrix_Notebooks = request.form.get('Skill_Databrix_Notebooks')
    Skill_Denodo = request.form.get('Skill_Denodo')
    Skill_OpenMetadata = request.form.get('Skill_OpenMetadata')
    Skill_Python = request.form.get('Skill_Python')
    Skill_Azure = request.form.get('Skill_Azure')

    # Gera um ID único para o recurso
    id_recurso = generate_resource_id()

    # Tela de entrada dos dados do formulário
    flash(f"Cadastro de Recurso: ID Recurso: {id_recurso}, Recurso: {Recurso}, Perfil: {Perfil}")

    # Adiciona os dados ao arquivo Excel
    file_path = 'recursos_v2.xlsx'

    # Verifica se o arquivo já existe
    if os.path.exists(file_path):
        df = pd.read_excel(file_path)
    else:
        df = pd.DataFrame(columns=['ID Recurso', 'Recurso', 'Perfil', 'Disponibilidade_DG', 'Disponibilidade_IA', 'Ingresso_ao_Time', 'Ate',
                                   'Duracao', 'Ano_de_ate', 'email', 'Local_de_atuacao', 'Celular', 'Qtd_Atuacoes', 'Alocacao',
                                   'reuniao_one_on_one', 'gestor_one_on_one', 'Skill_Comunicacao', 'Skill_DG', 'Skill_IDMC_DG',
                                   'Skill_IDMC_DQ', 'Skill_Axon', 'Skill_EDC', 'Skill_TDM', 'Skill_DPM', 'Skill_DEI', 'Skill_DEQ',
                                   'Skill_PowerCenter', 'Skill_Purview', 'Skill_Dataplex', 'Skill_Databrix_Notebooks', 'Skill_Denodo',
                                   'Skill_OpenMetadata', 'Skill_Python', 'Skill_Azure',
                                   'De_Para_Skill_Comunicacao', 'De_Para_Skill_DG', 'De_Para_Skill_IDMC_DG',
                                   'De_Para_Skill_IDMC_DQ', 'De_Para_Skill_Axon', 'De_Para_Skill_EDC', 'De_Para_Skill_TDM',
                                   'De_Para_Skill_DPM', 'De_Para_Skill_DEI', 'De_Para_Skill_DEQ', 'De_Para_Skill_PowerCenter',
                                   'De_Para_Skill_Purview', 'De_Para_Skill_Dataplex', 'De_Para_Skill_Databrix_Notebooks',
                                   'De_Para_Skill_Denodo', 'De_Para_Skill_OpenMetadata', 'De_Para_Skill_Python', 'De_Para_Skill_Azure'])

    new_data = {
        'ID Recurso': id_recurso,
        'Recurso': Recurso,
        'Perfil': Perfil,
        'Disponibilidade_DG': 'Sim' if Disponibilidade_DG == 'True' else 'Não',
        'Disponibilidade_IA': 'Sim' if Disponibilidade_IA == 'True' else 'Não',
        'Ingresso_ao_Time': Ingresso_ao_Time,
        'Ate': Ate,
        'Duracao': Duracao,
        'Ano_de_ate': Ano_de_ate,
        'email': email,
        'Local_de_atuacao': Local_de_atuacao,
        'Celular': Celular,
        'Qtd_Atuacoes': Qtd_Atuacoes,
        'Alocacao': Alocacao,
        'reuniao_one_on_one': reuniao_one_on_one,
        'gestor_one_on_one': gestor_one_on_one,
        'Skill_Comunicacao': Skill_Comunicacao,
        'Skill_DG': Skill_DG,
        'Skill_IDMC_DG': Skill_IDMC_DG,
        'Skill_IMDC_DQ': Skill_IDMC_DQ,
        'Skill_Axon': Skill_Axon,
        'Skill_EDC': Skill_EDC,
        'Skill_TDM': Skill_TDM,
        'Skill_DPM': Skill_DPM,
        'Skill_DEI': Skill_DEI,
        'Skill_DEQ': Skill_DEQ,
        'Skill_PowerCenter': Skill_PowerCenter,
        'Skill_Purview': Skill_Purview,
        'Skill_Dataplex': Skill_Dataplex,
        'Skill_Databrix_Notebooks': Skill_Databrix_Notebooks,
        'Skill_Denodo': Skill_Denodo,
        'Skill_OpenMetadata': Skill_OpenMetadata,
        'Skill_Python': Skill_Python,
        'Skill_Azure': Skill_Azure,
        'De_Para_Skill_Comunicacao': skill_mapping(Skill_Comunicacao),
        'De_Para_Skill_DG': skill_mapping(Skill_DG),
        'De_Para_Skill_IDMC_DG': skill_mapping(Skill_IDMC_DG),
        'De_Para_Skill_IMDC_DQ': skill_mapping(Skill_IDMC_DQ),
        'De_Para_Skill_Axon': skill_mapping(Skill_Axon),
        'De_Para_Skill_EDC': skill_mapping(Skill_EDC),
        'De_Para_Skill_TDM': skill_mapping(Skill_TDM),
        'De_Para_Skill_DPM': skill_mapping(Skill_DPM),
        'De_Para_Skill_DEI': skill_mapping(Skill_DEI),
        'De_Para_Skill_DEQ': skill_mapping(Skill_DEQ),
        'De_Para_Skill_PowerCenter': skill_mapping(Skill_PowerCenter),
        'De_Para_Skill_Purview': skill_mapping(Skill_Purview),
        'De_Para_Skill_Dataplex': skill_mapping(Skill_Dataplex),
        'De_Para_Skill_Databrix_Notebooks': skill_mapping(Skill_Databrix_Notebooks),
        'De_Para_Skill_Denodo': skill_mapping(Skill_Denodo),
        'De_Para_Skill_OpenMetadata': skill_mapping(Skill_OpenMetadata),
        'De_Para_Skill_Python': skill_mapping(Skill_Python),
        'De_Para_Skill_Azure': skill_mapping(Skill_Azure)
    }

    # Converte os novos dados para um DataFrame
    new_data_df = pd.DataFrame([new_data])

    # Adiciona os novos dados ao DataFrame
    df = pd.concat([df, new_data_df], ignore_index=True)

    # Salva o DataFrame atualizado no arquivo Excel
    df.to_excel(file_path, index=False)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
