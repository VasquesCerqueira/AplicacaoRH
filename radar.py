from flask import Flask, render_template, request, jsonify
import pandas as pd
import plotly.graph_objs as go

app = Flask(__name__)

# Caminho para o arquivo Excel
file_path = '/Users/denisecerqueira/NovoRH/recursos_v2.xlsx'


def load_data():
    df = pd.read_excel(file_path, sheet_name='Sheet1',
                       usecols=['ID Recurso', 'Recurso', 'Skill_Comunicacao', 'Skill_DG', 'Skill_IDMC_DG',
                                'Skill_IDMC_DQ', 'Skill_Axon', 'Skill_EDC', 'Skill_TDM', 'Skill_DPM', 'Skill_DEI',
                                'Skill_DEQ', 'Skill_PowerCenter', 'Skill_Purview', 'Skill_Dataplex',
                                'Skill_Databrix_Notebooks', 'Skill_Denodo', 'Skill_OpenMetadata', 'Skill_Python',
                                'Skill_Azure'])
    return df


@app.route('/')
def index():
    df = load_data()
    recursos = df['Recurso'].unique()
    return render_template('index_2.html', recursos=recursos)


@app.route('/update_chart', methods=['POST'])
def update_chart():
    recurso1 = request.form.get('recurso1')
    recurso2 = request.form.get('recurso2')
    df = load_data()

    selected_df = df[(df['Recurso'] == recurso1) | (df['Recurso'] == recurso2)]

    categories = ['Skill_Comunicacao', 'Skill_DG', 'Skill_IDMC_DG', 'Skill_IDMC_DQ', 'Skill_Axon', 'Skill_EDC',
                  'Skill_TDM', 'Skill_DPM', 'Skill_DEI', 'Skill_DEQ', 'Skill_PowerCenter', 'Skill_Purview',
                  'Skill_Dataplex', 'Skill_Databrix_Notebooks', 'Skill_Denodo', 'Skill_OpenMetadata', 'Skill_Python',
                  'Skill_Azure']

    fig = go.Figure()

    for i, row in selected_df.iterrows():
        values = row[categories].values.flatten().tolist()
        values += values[:1]
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories + [categories[0]],
            fill='toself',
            name=row['Recurso']
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 3]
            )),
        showlegend=True
    )

    graphJSON = fig.to_json()
    return jsonify(graphJSON)


if __name__ == '__main__':
    app.run(debug=True)
