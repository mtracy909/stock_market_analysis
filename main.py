import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    info = pd.read_csv("indexInfo.csv")
    raw = pd.read_csv("indexData.csv")
    proc = pd.read_csv("indexProcessed.csv", parse_dates=["Date"])

    nasdaq = proc[proc["Index"] == "IXIC"].sort_values("Date")
    nasdaq.set_index("Date", inplace=True)

    nasdaq["Close"].plot(title="NASDAQ Composite Closing Price", figsize=(10, 5))
    plt.ylabel("USD")
    plt.show()

if __name__ == "__main__":
    main()