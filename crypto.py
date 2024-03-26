import tkinter as tk
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time
import threading

class CryptoSimulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Highly Advanced Crypto Simulator")
        self.root.geometry("800x600")

        self.currencies = ["BTC", "ETH", "XRP", "LTC", "ADA"]
        self.prices = {currency: 1000 for currency in self.currencies}
        self.labels = {}

        self.setup_ui()
        self.update_prices()
        self.root.mainloop()

    def setup_ui(self):
        for i, currency in enumerate(self.currencies):
            label = tk.Label(self.root, text=currency)
            label.grid(row=i, column=0, padx=10, pady=10)
            self.labels[currency] = tk.Label(self.root, text="$1000")
            self.labels[currency].grid(row=i, column=1, padx=10, pady=10)

        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.grid(row=0, column=2, rowspan=len(self.currencies), padx=10, pady=10)
        self.plot_figure, self.plot_axes = plt.subplots()
        self.plot_canvas = FigureCanvasTkAgg(self.plot_figure, master=self.plot_frame)
        self.plot_canvas.get_tk_widget().pack()

    def update_prices(self):
        def fetch_price(currency):
            url = f"https://api.coingecko.com/api/v3/simple/price?ids={currency.lower()}&vs_currencies=usd"
            response = requests.get(url)
            price_data = response.json()
            return price_data[currency.lower()]["usd"]

        def update_gui():
            for currency in self.currencies:
                price = fetch_price(currency)
                self.prices[currency] = price
                self.labels[currency].config(text=f"${price:.2f}")

            self.plot_prices()
            self.root.after(5000, self.update_prices)

        threading.Thread(target=update_gui).start()

    def plot_prices(self):
        self.plot_axes.clear()
        x = np.arange(len(self.currencies))
        prices = [self.prices[currency] for currency in self.currencies]
        self.plot_axes.bar(x, prices, color='skyblue')
        self.plot_axes.set_xticks(x)
        self.plot_axes.set_xticklabels(self.currencies)
        self.plot_axes.set_title('Crypto Prices')
        self.plot_canvas.draw()

if __name__ == "__main__":
    CryptoSimulator()
