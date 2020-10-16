import streamlit as st
import random


def draw_diagonal(x, y, x2, y2, color='black'):
	#format a line for svg 
    return f'<line x1="{x}" y1="{y}" x2="{x2}" \
            y2="{y2}" stroke="{color}" />'

def make_maze(num, color = "black" , height = 500):
	#num is the number of diagonals across and down
	#filename is the output file name
    width = height
    header = f'<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    
    step=height // num
    #write the header for the file
    txt = header
    #loop through 
    for row in range(0, height, step):
      for col in range(0, width, step):
        #choose a random direction for the diagonal line
        if random.choice([0, 1]) == 0:
        	#write the line
            txt += draw_diagonal(col, row, col + step, row + step, color)
        else:
        	#write the line
            txt += draw_diagonal(col + step, row, col, row + step, color)
    #write the footer
    footer = f'</svg>'
    txt += footer
    return txt

if __name__ == "__main__":
    svg = make_maze(50, color="darkviolet" )
    st.image(svg)
    
