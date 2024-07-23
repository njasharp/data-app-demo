import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
import time

# Function to get cryptocurrency data
def get_crypto_data(symbol, period='1d', interval='60m'):
    data = yf.Ticker(symbol).history(period=period, interval=interval)
    return data

# Main function to run the app
def main():
    st.title('Cryptocurrency Price Dashboard')

    # Sidebar for user input
    crypto_symbol = st.sidebar.text_input('Enter Cryptocurrency Symbol (e.g., BTC-USD)', 'BTC-USD')
    period = st.sidebar.selectbox('Select Time Period', ['1d', '5d', '1mo', '3mo', '6mo', '1y'])
    interval = st.sidebar.selectbox('Select Interval', ['1m', '5m', '15m', '30m', '60m', '1d'])

    # Fetch data
    data = get_crypto_data(crypto_symbol, period, interval)

    # Display current price
    current_price = data['Close'].iloc[-1]
    st.header(f"Current {crypto_symbol} Price: ${current_price:.2f}")

    # Create price chart
    fig = go.Figure(data=[
        go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            increasing_line_color='green',
            decreasing_line_color='red'
        )
    ])
    fig.update_layout(
        title=f"{crypto_symbol} Price Chart",
        xaxis_title="Date",
        yaxis_title="Price",
        xaxis_rangeslider_visible=False
    )
    st.plotly_chart(fig)

    # Create volume bar chart
    vol_fig = go.Figure(data=[
        go.Bar(
            x=data.index,
            y=data['Volume'],
            marker_color=['green' if data['Close'][i] > data['Open'][i] else 'red' for i in range(len(data))],
            name='Volume'
        )
    ])
    vol_fig.update_layout(
        title=f"{crypto_symbol} Volume Chart",
        xaxis_title="Date",
        yaxis_title="Volume",
        xaxis_rangeslider_visible=False
    )
    st.plotly_chart(vol_fig)

    # Display basic stats
    st.subheader('Basic Stats')
    st.write(f"Volume: {data['Volume'].iloc[-1]:.2f}")
    st.write(f"24h Change: {((data['Close'].iloc[-1] - data['Open'].iloc[0]) / data['Open'].iloc[0] * 100):.2f}%")

    # Recent transactions
    st.subheader('Recent Transactions')
    transactions = pd.DataFrame({
        'Date': data.index[-5:],
        'Price': data['Close'].iloc[-5:],
        'Volume': data['Volume'].iloc[-5:]
    })
    st.table(transactions)

    # Refresh every 3 minutes
    if 'last_refresh' not in st.session_state:
        st.session_state.last_refresh = time.time()

    if time.time() - st.session_state.last_refresh > 180:
        st.session_state.last_refresh = time.time()
        st.experimental_rerun()

if __name__ == "__main__":
    main()
st.info("dw v1")
