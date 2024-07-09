import plotly.graph_objects as go
from plotly.subplots import make_subplots

def create_RSI_graph(df, ticker):
    
    fig = go.Figure()
    
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                    vertical_spacing=0.1, row_heights=[0.7, 0.3])

    fig.add_shape(
        type="line",
        x0=df.index.min(), x1=df.index.max(),
        y0=30, y1=30,
        line=dict(color="grey", width=2, dash="dash"),
        row=2, col=1
    )

    fig.add_shape(
        type="line",
        x0=df.index.min(), x1=df.index.max(),
        y0=70, y1=70,
        line=dict(color="grey", width=2, dash="dash"),
        row=2, col=1
    )

    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['Adj Close'],
        name='Adj Close',
        line=dict(color='blue'),
        yaxis='y1'
    ), row = 1, col = 1)
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['RSI'],
        name='RSI',
        line=dict(color='orange'),
        yaxis='y2'
    ), row = 2, col = 1)

    fig.update_layout(
        title=f'{ticker} x RSI',
        font=dict(size=15),
        legend=dict(font=dict(size=15)),
        xaxis=dict(title='Date'),
        yaxis=dict(title='Price', titlefont=dict(color='blue'), tickfont=dict(color='blue')),
        yaxis2=dict(title='RSI', titlefont=dict(color='blue'), tickfont=dict(color='blue')),
        template='plotly_white',
        height=700,  # Adjust height to make room for both plots
        showlegend=False
    )
    
    fig.update_yaxes(title_text="Price", row=1, col=1)
    fig.update_yaxes(title_text="RSI", row=2, col=1)

    config = {'responsive': True, 'modeBarButtonsToRemove': ['resetScale2d'], 'displaylogo': False}
    price_rsi = fig.to_html(full_html=False, include_plotlyjs='cdn', config=config)
    return price_rsi

def create_bollinger_graph(df, ticker):

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=df.index, y=df['Adj Close'], mode='lines', name='Adj Close', line=dict(color='darkblue', width=1)))
    fig.add_trace(go.Scatter(x=df.index, y=df['RM'], mode='lines', name='RM', line=dict(color='orange', width=1)))
    fig.add_trace(go.Scatter(x=df.index, y=df['Sup_Band'], mode='lines', name='Sup_Band', line=dict(color='green', width=1)))
    fig.add_trace(go.Scatter(x=df.index, y=df['Inf_Band'], mode='lines', name='Inf_Band', line=dict(color='red', width=1)))

    fig.update_layout(
        title=f'{ticker} - Bollinger Bands',
        xaxis_title='Date',
        yaxis_title='Price',
        font=dict(size=15),
        legend=dict(font=dict(size=15)),
        autosize=False,
        width=800,
        height=600,
        template='plotly_white'
    )

    config = {'responsive': True, 'modeBarButtonsToRemove': ['resetScale2d'], 'displaylogo': False}
    div_html = fig.to_html(full_html=False, include_plotlyjs='cdn', config=config)
    return div_html