import plotly.graph_objs as go

# Set the factors and their impact on energy consumption
factors = ['AutoML', 'Hyperdrive', 'ONNX', 'Azure Machine Learning', 'Azure IoT Hub', 'Azure Function']
factor_impact = [15, 7.5, 2.5, 25, 12.5, 7.5]

# Set the initial energy consumption values for the green AI model and the traditional AI model
green_ai_energy = [100]
traditional_ai_energy = [100]

# Calculate the energy consumption values for the green AI model and the traditional AI model at each iteration
for i in range(len(factors)):
    green_ai_energy.append(green_ai_energy[-1] - factor_impact[i])
    traditional_ai_energy.append(traditional_ai_energy[-1] + factor_impact[i])

# Set the threshold for good energy consumption
threshold = 120

# Create an animated bar chart to compare the energy consumption of the green AI model and the traditional AI model
frames = [go.Frame(data=[go.Bar(name='Green AI Model', x=['Green AI Model'], y=[green_ai_energy[i]], marker_color='green', text=f'{green_ai_energy[i]-green_ai_energy[i-1]:+.1f}%', textposition='auto'),
                          go.Bar(name='Traditional AI Model', x=['Traditional AI Model'], y=[traditional_ai_energy[i]], marker_color='red' if traditional_ai_energy[i] > threshold else 'blue', text=f'{traditional_ai_energy[i]-traditional_ai_energy[i-1]:+.1f}%', textposition='auto'),
                          go.Scatter(x=['Green AI Model', 'Traditional AI Model'], y=[threshold, threshold], mode='lines', line=dict(color='black', width=2, dash='dash'))],
                    layout=go.Layout(title=f'Comparison of Energy Consumption (Iteration {i+1}, {factors[i]} applied)')) for i in range(1, len(factors))]
fig = go.Figure(frames=frames)
fig.add_trace(go.Bar(name='Green AI Model', x=['Green AI Model'], y=[green_ai_energy[0]], marker_color='green'))
fig.add_trace(go.Bar(name='Traditional AI Model', x=['Traditional AI Model'], y=[traditional_ai_energy[0]], marker_color='blue'))
fig.add_trace(go.Scatter(x=['Green AI Model', 'Traditional AI Model'], y=[threshold, threshold], mode='lines', line=dict(color='black', width=2, dash='dash')))
fig.frames = frames
fig.layout.updatemenus = [dict(type='buttons',
                                showactive=False,
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None])])]
fig.layout.title = 'Comparison of Energy Consumption'
fig.layout.yaxis.title = 'Energy Consumption'

# Show the plot
fig.show()
