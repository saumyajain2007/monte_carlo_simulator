import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def fetch_stock_data(ticker, start_date, end_date):
    """Fetches historical stock data from Yahoo Finance."""
    print(f"Fetching data for {ticker} from {start_date} to {end_date}...")
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            raise ValueError("No data returned for the given ticker and date range.")
        return data['Adj Close']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def monte_carlo_simulation(data, num_simulations, num_days):
    """
    Performs Monte Carlo simulation to predict future stock prices.
    Uses Geometric Brownian Motion.
    """
    # Calculate daily returns
    returns = data.pct_change().dropna()
    
    # Calculate mean and standard deviation of daily returns
    mu = returns.mean()
    sigma = returns.std()
    
    # Calculate drift and standard deviation for the simulation
    drift = mu - 0.5 * sigma**2
    daily_returns_sim = np.random.normal(drift, sigma, size=(num_days, num_simulations))
    
    # Get the last closing price
    last_price = data.iloc[-1]
    
    # Create an array to hold simulated paths
    price_paths = np.zeros_like(daily_returns_sim)
    price_paths[0] = last_price
    
    # Simulate price paths
    for t in range(1, num_days):
        price_paths[t] = price_paths[t - 1] * np.exp(daily_returns_sim[t] * np.sqrt(252))
        
    return pd.DataFrame(price_paths)

def plot_results(simulations_df, historical_data):
    """Plots the simulated paths and key statistics."""
    plt.figure(figsize=(12, 8))
    plt.plot(simulations_df, alpha=0.1, color='blue') # Plot all simulated paths
    plt.title('Monte Carlo Simulation of Stock Price')
    plt.xlabel('Days into the Future')
    plt.ylabel('Simulated Price ($)')
    plt.grid(True)
    
    # Plot the mean and confidence intervals
    final_prices = simulations_df.iloc[-1]
    mean_price = final_prices.mean()
    confidence_95 = np.percentile(final_prices, [2.5, 97.5])
    
    plt.axhline(mean_price, color='red', linestyle='--', label=f'Mean Final Price: ${mean_price:.2f}')
    plt.axhline(confidence_95[0], color='green', linestyle='--', label=f'95% Confidence Interval: [${confidence_95[0]:.2f}, ${confidence_95[1]:.2f}]')
    plt.axhline(confidence_95[1], color='green', linestyle='--')
    
    plt.legend()
    plt.show()

if __name__ == "__main__":
    TICKER = 'AAPL'  # Change to your desired stock ticker
    START_DATE = '2022-01-01'
    END_DATE = '2023-01-01'
    NUM_SIMULATIONS = 1000
    NUM_DAYS = 252 # Approximately one trading year

    # 1. Fetch historical data
    historical_prices = fetch_stock_data(TICKER, START_DATE, END_DATE)

    if historical_prices is not None:
        # 2. Run the Monte Carlo simulation
        simulated_paths = monte_carlo_simulation(historical_prices, NUM_SIMULATIONS, NUM_DAYS)

        # 3. Plot the results
        plot_results(simulated_paths, historical_prices)
