import plotly.graph_objects as go
import numpy as np
from plotly.subplots import make_subplots
import pandas as pd

fig = make_subplots(rows=2, cols=2, vertical_spacing=0.05, horizontal_spacing=0.15, column_widths=[0.25, 0.75], \
                    specs=[[{'rowspan': 1, 'b':0.1}, {}], [{'rowspan': 1, 'b':0.1}, {}]])

df = pd.read_csv(r"data_for_plot.csv")
df_noise = pd.read_csv(r"data_for_plot_with_noise.csv")
xs = df[df["t"] == 0]['x']
t = df[df["x"] == -1]['t']

x = -1.0
actual_normal = df['actual_normal'].sum()
actual_physics = df['actual_physics'].sum()
du_dv_normal = df['du_dv_normal'].sum()
du_dv_physics = df['du_dv_physics'].sum()
actual_normal_noise = df_noise['actual_normal_noise'].sum()
actual_physics_noise = df_noise['actual_physics_noise'].sum()
du_dv_normal_noise = df_noise['du_dv_normal_noise'].sum()
du_dv_physics_noise = df_noise['du_dv_physics_noise'].sum()

var_1 = 'u<sup>error</sup> (Neural Network)'
var_2 = 'u<sup>error</sup> (Physics Informed NN)'
var_3 = 'u<sup>error</sup> (Neural Network with Noise)'
var_4 = 'u<sup>error</sup> (Physics Informed NN with Noise)'
var_5 = 'u<sub>t</sub><sup>error</sup> (Neural Network)'
var_6 = 'u<sub>t</sub><sup>error</sup> (Physics Informed NN)'
var_7 = 'u<sub>t</sub><sup>error</sup> (Neural Network with Noise)'
var_8 = 'u<sub>t</sub><sup>error</sup> (Physics Informed NN with Noise)'

fig.add_trace(go.Bar(y=[var_4, var_3, var_2 , var_1],\
                     x=[actual_physics_noise, actual_normal_noise, actual_physics, actual_normal], showlegend=False, orientation='h', width=.5, \
                     marker_color=['green', 'red', 'green', 'red']), row=1, col=1)
fig.add_trace(go.Bar(y=[var_8, var_7, var_6, var_5], \
                     x=[du_dv_physics_noise, du_dv_normal_noise, du_dv_physics, du_dv_normal], showlegend=False, orientation='h', width=.5, \
                     marker_color=['green', 'red', 'green', 'red'], name="Network"), row=2, col=1)
fig.add_trace(go.Scatter(x=t, y=df[df["x"] == x]['du_normal'], name="u<sub>t</sub> (Neural Network) = u<sub>t</sub>", \
                         line = dict(color='red', dash='dash')), row=2, col=2)
fig.add_trace(go.Scatter(x=t, y=df[df["x"] == x]['dv_normal'], name="u<sub>t</sub> (Neural Network) = -uu<sub>x</sub>+(0.01/&#960;)u<sub>xx</sub>", \
                         fill='tonexty', mode="lines", line = dict(color='red', dash='dot')), row=2, col=2)
fig.add_trace(go.Scatter(x=t, y=df[df["x"] == x]['du_physics'], name="u<sub>t</sub> (Physics Informed NN) = u<sub>t</sub>", \
                         line = dict(color='green', dash='dash')), row=2, col=2)
fig.add_trace(go.Scatter(x=t, y=df[df["x"] == x]['dv_physics'], name="u<sub>t</sub> (Physics Informed NN) = -uu<sub>x</sub>+(0.01/&#960;)u<sub>xx</sub>", \
                         fill='tonexty', mode="lines", line = dict(color='green', dash='dot')), row=2, col=2)
fig.add_trace(go.Scatter(x=t, y=df[df["x"] == x]['u_actual'], name="u (Observed Data) <br>", \
                         line = dict(color='blue')), row=1, col=2)
fig.add_trace(go.Scatter(x=t, y=df[df["x"] == x]['u_normal'], name="u (Neural Network)", \
                         fill='tonexty', mode="lines", line = dict(color='red')), row=1, col=2)
fig.add_trace(go.Scatter(x=t, y=df[df["x"] == x]['u_actual'], name="u (Observed Data)", \
                         showlegend=False, line = dict(color='blue')), row=1, col=2)
fig.add_trace(go.Scatter(x=t, y=df[df["x"] == x]['u_physics'], name="u (Physics Informed NN)", \
                         fill='tonexty', mode="lines", line = dict(color='green')), row=1, col=2)

frames = []
for x in xs:  
    frames.append(go.Frame(data=[go.Bar(y=[var_4, var_3, var_2, var_1],\
                                        x=[actual_physics_noise, actual_normal_noise, actual_physics, actual_normal]),
                            go.Bar(y=[var_8, var_7, var_6, var_5], \
                                   x=[du_dv_physics_noise, du_dv_normal_noise, du_dv_physics, du_dv_normal]),
                            go.Scatter(x=t, y=df[df["x"] == x]['du_normal']),
                            go.Scatter(x=t, y=df[df["x"] == x]['dv_normal']),
                            go.Scatter(x=t, y=df[df["x"] == x]['du_physics']),
                            go.Scatter(x=t, y=df[df["x"] == x]['dv_physics']),
                            go.Scatter(x=t, y=df[df["x"] == x]['u_actual']),
                            go.Scatter(x=t, y=df[df["x"] == x]['u_normal']),
                            go.Scatter(x=t, y=df[df["x"] == x]['u_actual']),
                            go.Scatter(x=t, y=df[df["x"] == x]['u_physics']),],
                            name = x,
                            traces=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


fig.frames=frames

play = dict(
             label='Play',
             method='animate',
             args=[None, dict(frame=dict(duration=100, redraw=False), 
                              transition=dict(duration=0),
                              fromcurrent=True,
                              mode='immediate')])
pause = {
                "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                  "mode": "immediate",
                                  "transition": {"duration": 0}}],
                "label": "Pause",
                "method": "animate"
            }

fig.update_layout(updatemenus=[dict(type='buttons',
                              showactive=False,
                              y=0,
                              x=1.05,
                              xanchor='left',
                              yanchor='bottom',
                              buttons=[play, pause] )
                                      ],
                 width=1350, height=600)

steps = []
i = 0             
for x in xs:
    # fig_dict["frames"].append(go.Frame(f[i]))
    s = str(x)
    dot = s.find('.')
    s = s[:dot+4]
    step = {"args": [
        [x],
        {"frame": {"duration": 100, "redraw": False},
         "mode": "immediate",
         "fromcurrent" : True,
         "transition": {"duration": 0}}
    ],
        "label": s,
        "method": "animate"}
    
    steps.append(step)
    i += 1

sliders = {
    "active": 0,
    "yanchor": "top",
    "xanchor": "left",
    "currentvalue": {
        "font": {"size": 20},
        "prefix": "x:",
        "visible": True,
        "xanchor": "right"
    },
    "transition": {"duration": 0, "easing": "cubic-in-out"},
    "pad": {"b": 10, "t": 50},
    "len": 1.0,
    "x": 0,
    "y": 0,
    "steps": steps
}
                              
fig.update_yaxes(range=[-1.5, 1.5], row=1, col=2, title='u')
fig.update_yaxes(range=[-3.2, 3.2], row=2, col=2, title='u<sub>t</sub>')
fig.update_xaxes(row=1, col=1, title='u<sup>error</sup> = &#8721;|u<sub>Predicted</sub> - u<sub>Observed Data</sub>|')
fig.update_xaxes(row=2, col=1, title='u<sub>t</sub><sup>error</sup> = &#8721;|u<sub>t</sub> - (-uu<sub>x</sub>+(0.01/&#960;)u<sub>xx</sub>)|')

fig.update_layout(sliders=[sliders], margin = { 'l': 20, 'r': 20, 'b': 20, 't': 20})
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.update_xaxes(title='t', row=2, col=2)
fig.update_xaxes(showticklabels=False, row=1, col=2)
fig.update_xaxes(tickvals = [0, 2000, 4000, 6000, 8000], ticktext = ['0', '2k', '4k', '6k', '8k'], row=1, col=1)
fig.update_layout(legend=dict(yanchor="top", y=0.65, xanchor="left"))

fig.write_html("index.html", auto_play=False)
