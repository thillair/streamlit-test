import streamlit as st
import random


def draw_diagonal(x, y, x2, y2, color='black'):
	#format a line for svg 
    return f'<line x1="{x}" y1="{y}" x2="{x2}" \
            y2="{y2}" stroke="{color}" />'


def make_maze(num, color=('lightblue', 'pink') , height=500):
    #num is the number of diagonals across and down
	
    width = height
    header = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'
    
    step=height // num
    #write the header 
    txt = header
    #loop through 
    for row in range(0, height, step):
      for col in range(0, width, step):
        #choose a random direction for the diagonal line
        if random.choice([0, 1]) == 0:
            #write the line
            txt += draw_diagonal(col, row, col + step, row + step, color[0])
        else:
            #write the line
            txt += draw_diagonal(col + step, row, col, row + step, color[1])
    #write the footer
    footer = f'</svg>'
    txt += footer
    return txt

if __name__ == "__main__":
    st_num_lines = st.sidebar.slider('# lines: ', min_value=1, max_value=100, step=1, value=50)	
    st_col1 = st.sidebar.beta_color_picker('Pick a color: ', value='#ADD8E6')
    st_col2 = st.sidebar.beta_color_picker('Pick another color: ', value='#FFC0CB')
    st.markdown('## Maze!')
    svg = make_maze(st_num_lines, color=[st_col1, st_col2])
    #st.write(svg)
    st.image(svg)
    
    st.text('adapted from https://github.com/hogesonline/svg_play/blob/master/maze.py')
