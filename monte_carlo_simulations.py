
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
ticker = 'AAPL'
start_date = '2020-01-01'
end_date = '2023-01-01'
num_simulations = 100
time_horizon = 252  # Trading days in a year

# Simulate historical data (replace with yfinance if online)
np.random.seed(42)
simulated_prices = np.cumprod(1 + np.random.normal(0.0005, 0.02, 756)) * 150  # 3 years of prices
closing_prices = pd.Series(simulated_prices[-252:])  # Use last year as "recent" prices

# Calculate daily returns and volatility
daily_returns = closing_prices.pct_change().dropna()
mean_return = daily_returns.mean()
volatility = daily_returns.std()

# Starting price
last_price = closing_prices.iloc[-1]

# Monte Carlo simulation
simulations = np.zeros((time_horizon, num_simulations))
for i in range(num_simulations):
    price_series = [last_price]
    for _ in range(time_horizon - 1):
        price = price_series[-1] * np.exp((mean_return - 0.5 * volatility**2) + volatility * np.random.normal())
        price_series.append(price)
    simulations[:, i] = price_series

# Plotting
plt.figure(figsize=(12, 6))
for i in range(num_simulations):
    plt.plot(simulations[:, i], linewidth=0.7, alpha=0.7)
plt.title(f'Monte Carlo Simulation of {ticker} Stock Price')
plt.xlabel('Days')
plt.ylabel('Price')
plt.grid(True)
plt.tight_layout()
plt.savefig("monte_carlo_simulation.png", dpi=300)
plt.close()

# Optional: Save simulation data
sim_df = pd.DataFrame(simulations)
sim_df.to_csv("monte_carlo_simulations.csv", index=False)

