import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup


lol = {}
def fetch_currency_rates():
    url = "https://cbr.ru/currency_base/daily/"
    try:
        req = requests.get(url)
        req.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Ошибка при загрузке данных: {e}")
    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    data = soup.find_all('td')
    full_data = []
    for i in range(0, len(data), 5):
        full_data.append(data[i:i + 5])
    for i in full_data:
        a, b, c, d, f = i[0].text, i[1].text, i[2].text, i[3].text, i[4].text.replace(',', '.')
        lol[b] = float(f) / int(c)
    return lol

def convert():
    try:
        amount = float(entry_amount.get())
        from_cur = combo_ot.get()
        to_cur = combo_to.get()
        result = amount * lol[from_cur] / lol[to_cur]
        messagebox.showinfo("Результат", f"{amount} {from_cur} = {result:.4f} {to_cur}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка конвертации: {e}")

currency_list = sorted(fetch_currency_rates().keys())


root = tk.Tk()
root.title("Конвертер валют")

tk.Label(root, text="Сумма:").grid(row=0, column=0, sticky='e')
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Из валюты:").grid(row=1, column=0, sticky='e')
combo_ot = ttk.Combobox(root, values=currency_list, state="readonly")
combo_ot.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="В валюту:").grid(row=2, column=0, sticky='e')
combo_to = ttk.Combobox(root, values=currency_list, state="readonly")
combo_to.grid(row=2, column=1, padx=5, pady=5)

btn_convert = tk.Button(root, text="Конвертировать", command=convert)
btn_convert.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()

if __name__ == "__main__":
    fetch_currency_rates()
#### https://yandex.ru/video/preview/4747738968122974291