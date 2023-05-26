import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np

# Set the factors and their impact on performance metrics
factors = ['AutoML', 'Hyperdrive', 'ONNX', 'Azure Machine Learning', 'Azure IoT Hub', 'Azure Function']
factor_impact = {
    'AutoML': {'model_size': -10, 'inference_time': -5, 'training_time': -7},
    'Hyperdrive': {'model_size': -5, 'inference_time': -3, 'training_time': -4},
    'ONNX': {'model_size': -3, 'inference_time': -2, 'training_time': -2},
    'Azure Machine Learning': {'model_size': -15, 'inference_time': -8, 'training_time': -10},
    'Azure IoT Hub': {'model_size': -8, 'inference_time': -4, 'training_time': -6},
    'Azure Function': {'model_size': -5, 'inference_time': -3, 'training_time': -4}
}

# Set the initial performance metrics for the green AI model and the traditional AI model
initial_model_size = 0
initial_inference_time = 0
initial_training_time = 0

# Initialize empty lists for the performance metrics
green_ai_model_size = [initial_model_size]
traditional_ai_model_size = [initial_model_size] + 1
green_ai_inference_time = [initial_inference_time] +2
traditional_ai_inference_time = [initial_inference_time] 
green_ai_training_time = [initial_training_time]
traditional_ai_training_time = [initial_training_time]

# Calculate the performance metrics for the green AI model and the traditional AI model after applying each technique
for factor in factors:
    green_ai_model_size.append(green_ai_model_size[-1] + factor_impact[factor]['model_size'])
    traditional_ai_model_size.append(traditional_ai_model_size[-1] - factor_impact[factor]['model_size'])
    green_ai_inference_time.append(green_ai_inference_time[-1] + factor_impact[factor]['inference_time'])
    traditional_ai_inference_time.append(traditional_ai_inference_time[-1] - factor_impact[factor]['inference_time'])
    green_ai_training_time.append(green_ai_training_time[-1] + factor_impact[factor]['training_time'])
    traditional_ai_training_time.append(traditional_ai_training_time[-1] - factor_impact[factor]['training_time'])

# Create the figure and subplots
fig = make_subplots(rows=3, cols=1, shared_xaxes=True, vertical_spacing=0.1)

# Add traces for model size
fig.add_trace(
    go.Scatter(x=factors, y=green_ai_model_size, name='Green AI Model', mode='lines+markers', marker=dict(color='white')),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=factors, y=traditional_ai_model_size, name='Traditional AI Model', mode='lines+markers', marker=dict(color='white')),
    row=1, col=1
)


# Add traces for inference time
fig.add_trace(
    go.Scatter(x=factors, y=green_ai_inference_time, name='Green AI Model', mode='lines+markers', marker=dict(color='white')),
    row=2, col=1
)
fig.add_trace(
    go.Scatter(x=factors, y=traditional_ai_inference_time, name='Traditional AI Model', mode='lines+markers', marker=dict(color='white')),
    row=2, col=1
)



# Add traces for training time
fig.add_trace(
    go.Scatter(x=factors, y=green_ai_training_time, name='Green AI Model', mode='lines+markers', marker=dict(color='white')),
    row=3, col=1
)
fig.add_trace(
    go.Scatter(x=factors, y=traditional_ai_training_time, name='Traditional AI Model', mode='lines+markers', marker=dict(color='white')),
    row=3, col=1
)

# Set the layout and plot configuration
fig.update_layout(
    title='Effect of Techniques on AI Performance Metrics (Size, Inference time and Training time)',
    xaxis=dict(title='Technique'),
    yaxis=dict(title='Percentage'),
    plot_bgcolor='#aebea6',
    paper_bgcolor='#181a23',
    font=dict(color='#ffffff')
)

# Define the animation frames
frames = [go.Frame(data=[
    go.Scatter(x=factors[:i+1], y=green_ai_model_size[:i+2], name='Green AI Model', mode='lines+markers', marker=dict(color='black')),
    go.Scatter(x=factors[:i+1], y=traditional_ai_model_size[:i+2], name='Traditional AI Model', mode='lines+markers', marker=dict(color='green')),
    go.Scatter(x=factors[:i+1], y=green_ai_inference_time[:i+2], name='Green AI Model', mode='lines+markers', marker=dict(color='green')),
    go.Scatter(x=factors[:i+1], y=traditional_ai_inference_time[:i+2], name='Traditional AI Model', mode='lines+markers', marker=dict(color='red')),
    go.Scatter(x=factors[:i+1], y=green_ai_training_time[:i+2], name='Green AI Model', mode='lines+markers', marker=dict(color='blue')),
    go.Scatter(x=factors[:i+1], y=traditional_ai_training_time[:i+2], name='Traditional AI Model', mode='lines+markers', marker=dict(color='yellow'))
]) for i in range(len(factors))]

# Add the frames to the figure
fig.frames = frames

# Create the updatemenus
updatemenus = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 1000, 'redraw': False}, 'fromcurrent': True, 'transition': {'duration': 500}}],
                'label': 'strat_training',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                'label': 'stop',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]

# Add the updatemenus to the figure
fig.update_layout(updatemenus=updatemenus)

# Show the plot
fig.show()
