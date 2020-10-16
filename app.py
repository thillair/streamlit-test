import streamlit as st
import streamlit.components.v1 as components
import random
import requests


def get_color():
    resp = requests.get('https://api.noopschallenge.com/hexbot')
    data = resp.json()
    color = data['colors'][0]['value']
    #st.write('response:', data)
    #st.write('color: ', color)
    return color


def draw_diagonal(x, y, x2, y2, color='black'):
	#format a line for svg 
    return f'<line x1="{x}" y1="{y}" x2="{x2}" \
            y2="{y2}" stroke="{color}" />'


def make_maze(num, color=('lightblue', 'pink') , height=500):
    #num is the number of diagonals across and down
	
    width = height
    header = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    
    step = height // num
    #write the header 
    txt = header
    #loop through 
    cnt_lines = 0
    for row in range(0, height, step):
      for col in range(0, width, step):
        #choose a random direction for the diagonal line
        if random.choice([0, 1]) == 0:
            #write the line
            cnt_lines += 1
            txt += draw_diagonal(col, row, col + step, row + step, color[0])
        else:
            #write the line
            cnt_lines += 1
            txt += draw_diagonal(col + step, row, col, row + step, color[1])
    #write the footer
    footer = f'</svg>'
    txt += footer
    st.write('count of lines: ', cnt_lines)
    return txt

if __name__ == "__main__":
    st_random = st.sidebar.radio('Random inputs: ', options=['Yes', 'No'], index=0)
    if st_random == 'Yes':
        st_num_lines = random.choice([x for x in range(1, 101)])
        st_col1 = get_color()
        st_col2 = get_color()
    else:
        st_num_lines = st.sidebar.slider('# lines: ', min_value=1, max_value=100, step=1, value=50)	
        st_col1 = st.sidebar.beta_color_picker('Pick a color: ', value='#ADD8E6')
        st_col2 = st.sidebar.beta_color_picker('Pick another color: ', value='#FFC0CB')
    
    st.markdown('## Maze!')
    if st.sidebar.button('GO!'):
        svg = make_maze(st_num_lines, color=[st_col1, st_col2])
        st.image(svg)
        st.markdown(f' lines {st_num_lines}, color1 {st_col1}, color2 {st_col2}')
	
        html = f""" <div style="background-color: {get_color()}"> </div>"""
        components.html(html, height=100, width=100, scrolling=False)
	 
    st.text('adapted from https://github.com/hogesonline/svg_play/blob/master/maze.py')
