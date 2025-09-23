# Monte Carlo Stock Price Simulation

This Python script performs a **Monte Carlo simulation** to forecast potential future stock prices. The simulation uses historical price data to model the stock's future path, considering its historical volatility and average daily return.

![Monte Carlo Simulation of Stock Price](monte_carlo_simulation.png)

***

### Features

-   Generates a Monte Carlo simulation of stock price movements using the **Geometric Brownian Motion (GBM)** model.
-   Calculates key metrics like daily returns and volatility from historical data.
-   Visualizes the simulation results with an easy-to-read chart, saving it as a `.png` file.
-   Exports all simulation data to a `.csv` file for further analysis.

***

### Theoretical Basis

A **Monte Carlo simulation** is a computational technique that uses repeated random sampling to model the probability of different outcomes in a process that is difficult to predict. In finance, it is a powerful tool for valuing assets and forecasting price movements.

#### Geometric Brownian Motion (GBM)

The theoretical foundation for this script is **Geometric Brownian Motion (GBM)**, a widely used model in mathematical finance to describe the random movement of stock prices. It assumes that stock price returns follow a **log-normal distribution**.

The core of the simulation is a discretized version of the GBM formula:

$$S_t = S_0 \cdot e^{(\mu - \frac{1}{2}\sigma^2)t + \sigma W_t}$$

Where:
* $S_t$: The stock price at time $t$.
* $S_0$: The initial stock price.
* $\mu$: The expected annualized return (drift).
* $\sigma$: The annualized volatility (standard deviation of returns).
* $W_t$: The Wiener process, a random variable from a standard normal distribution.

The script repeatedly applies this formula over a specified time horizon, generating thousands of possible future price paths.

***

### Getting Started

#### Prerequisites

To run this script, you need to have **Python 3** and the following libraries installed. You can install them using `pip`:

```bash
pip install numpy pandas matplotlib
```

#### Running the Script

1.  Save the code: Save the provided Python code as a file named a.py.

2.  Execute from the terminal: Open your terminal, navigate to the directory where you saved the file, and run the script:

```bash
python3 monte_carlo_simulation.py
```
#### Understanding the Output

After running the script, two files will be created in the same directory

1.  monte_carlo_simulation.png: A visual chart showing the many simulated price paths over the specified time horizon.

2.  monte_carlo_simulations.csv: A spreadsheet containing all the raw data from the simulation for each day and each path.

#### Customization

You can easily modify the simulation parameters by changing the values at the top of the monte_carlo_simulation.py script:

1.ticker: Change this to the ticker symbol of your desired stock (e.g., 'GOOGL').

2.start_date and end_date: Adjust the date range for the historical data used.

3.num_simulations: Increase or decrease the number of simulation paths to run.

4.time_horizon: Change the number of trading days to forecast into the future.
