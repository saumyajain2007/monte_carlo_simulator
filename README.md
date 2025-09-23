# Monte Carlo Stock Price Simulator

## Overview
This project utilizes Monte Carlo methods to simulate thousands of future stock price paths, providing a robust model for risk assessment and potential outcomes. It uses the Geometric Brownian Motion model to forecast future stock prices based on historical data.

## Methodology
The simulation uses the following steps:
1.  **Data Acquisition**: Historical daily adjusted closing prices for a chosen stock are fetched using the `yfinance` library.
2.  **Parameter Calculation**: The mean and standard deviation of daily returns are calculated from the historical data. These are used to determine the `drift` and `volatility` of the stock.
3.  **Monte Carlo Simulation**: Thousands of future price paths are simulated. For each path, a random daily return is generated based on the stock's historical drift and volatility.
4.  **Risk Assessment**: The simulation provides a range of potential outcomes. Key metrics like the mean final price and confidence intervals (e.g., 95% confidence) are calculated to assess potential risks and rewards.

## Getting Started

### Prerequisites
Make sure you have Python 3.6 or newer installed.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/saumyajain2007/monte-carlo-stock-simulator.git
