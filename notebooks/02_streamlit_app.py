import streamlit as st

st.header('Hello, World!')
st.sidebar.header('Menu')

st.write('Bem-vindo ao Streamlit')

st.write('-----')

st.markdown('Hello **World**, :wave:')

st.latex(r'f(x) = x^2 + 2x + 3')

st.code("print('codigo')")

#### Interatividade

### Checkbox

feature_flag = st.checkbox('Enable feature flag?')

st.write(f"Feature is `{'enabled' if feature_flag else 'disabled'}`")

### Botao
if st.button("celebrate"):
    st.balloons()

### Radio
st.subheader("Radio buttons")


option = st.radio('Escolha uma cor', ['Azul', 'Vermelho'])

st.write(f'Voce escolheu {option}')

### SelectBox

st.subheader('SelectBox')
option = st.selectbox('Escolha uma cor', ['Azul', 'Vermelho'])

### MultiSelect

st.subheader('MultiSelect')

option = st.multiselect('Escolha uma ou mais cores', ['Azul', 'Vermelho', 'Amarelo', 'Branco'])

name = st.text_input('Qual o seu nome?', value='-')
st.write(f'Hello, {name} :wave:')


senha = st.text_input('Qual a senha?', type='password')
st.write(f'Sua senha é: {senha}')


#### TextArea

st.subheader('TextArea')
texto = st.text_area('Insira um textão')

#### Datas

st.header('Misc')
st.write('-----')
st.subheader('Data input')
data = st.date_input('Que dia é hoje?')
st.write(f'Hoje é {data}')

st.header('File Upload')

csv = st.file_uploader('Escolha o arquivo CSV', type='csv', encoding='utf-8')

import pandas as pd

df = pd.read_csv(csv)

linhas = st.slider('Quantas linhas?', 5, int(df.shape[0]*0.3), 25)
st.table(df.head(linhas))

#### Gráficos

import numpy as np
import time

st.write('Gráfico dinamico')
data = np.random.randn(10,2)

add_data = st.checkbox('Atualizar grafico dinamicamente?')

chart = st.line_chart(data)

while add_data:
    chart.add_rows(np.random.randn(1,2))
    time.sleep(0.5)

df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

plot_types = {'bar': st.bar_chart, 'line': st.line_chart, 'area' : st.area_chart} 

plot_type = st.selectbox('Qual gráfico voce quer?', list(plot_types), index=0)

plot_types[plot_type](df)

import altair as alt

chart = alt.Chart(df).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b'])

st.altair_chart(chart)

st.subheader('Plotly')
import plotly.express as px

fig = px.scatter(df, x='a', y='b')
st.plotly_chart(fig)

st.header('3D maps and graphs')

lat, long = -23.5489 , -45.6388

df = pd.DataFrame(np.random.randn(1000,2) / [60,60] + [lat, long] , columns =['lat', 'lon'])

st.dataframe(df)

st.map(df)

import pydeck as pdk

st.pydeck_chart(pdk.Deck(map_style='mapbox://styles/mapbox/light-v9',
initial_view_state=pdk.ViewState(latitude=lat, longitude=long, zoom=11, pitch=50), 
layers=[pdk.Layer('HexagonLayer', data=df, get_position='[lon, lat]', radius=200, elevation_scale=4, elevation_range=[0,1000], pickable=True, extruded=True,
),
pdk.Layer('ScatterplotLater',
data=df,
get_position='[lon, lat]',
get_color='[200,30, 0, 160]',
get_radius=200,
),
],
))
























































































