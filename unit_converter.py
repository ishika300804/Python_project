import tkinter as tk
from tkinter import ttk, messagebox

# --- Conversion Logic ---
def convert_units():
    try:
        value = float(entry_value.get())
        category = combo_category.get()
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        if category == "Length":
            conversions = {
                "Meter": 1,
                "Kilometer": 1000,
                "Centimeter": 0.01,
                "Millimeter": 0.001,
                "Mile": 1609.34,
                "Yard": 0.9144,
                "Foot": 0.3048,
                "Inch": 0.0254
            }
        elif category == "Weight":
            conversions = {
                "Kilogram": 1,
                "Gram": 0.001,
                "Milligram": 0.000001,
                "Pound": 0.453592,
                "Ounce": 0.0283495
            }
        elif category == "Temperature":
            def temp_convert(val, from_u, to_u):
                if from_u == to_u:
                    return val
                if from_u == "Celsius":
                    return (val * 9/5 + 32) if to_u == "Fahrenheit" else (val + 273.15)
                if from_u == "Fahrenheit":
                    return ((val - 32) * 5/9) if to_u == "Celsius" else ((val - 32) * 5/9 + 273.15)
                if from_u == "Kelvin":
                    return (val - 273.15) if to_u == "Celsius" else ((val - 273.15) * 9/5 + 32)
            converted = temp_convert(value, from_unit, to_unit)
            result_label.config(text=f"{value:.2f} {from_unit} = {converted:.2f} {to_unit}")
            return
        else:
            messagebox.showerror("Error", "Invalid category selected.")
            return

        if from_unit in conversions and to_unit in conversions:
            base = value * conversions[from_unit]
            converted = base / conversions[to_unit]
            result_label.config(text=f"{value:.2f} {from_unit} = {converted:.2f} {to_unit}")
        else:
            messagebox.showerror("Error", "Invalid units selected.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# --- GUI Setup ---
window = tk.Tk()
window.title("Unit Converter")
window.geometry("400x400")
window.configure(bg="#1a1a1a")

# Title
tk.Label(window, text="Unit Converter", font=("Arial", 20), bg="#1a1a1a", fg="#ff69b4").pack(pady=10)

# Value Entry
entry_value = tk.Entry(window, font=("Arial", 14), justify="center")
entry_value.pack(pady=10)

# Category Selection
categories = ["Length", "Weight", "Temperature"]
combo_category = ttk.Combobox(window, values=categories, state="readonly", font=("Arial", 12), width=20)
combo_category.set("Length")
combo_category.pack(pady=10)

# Unit Selection
frame_units = tk.Frame(window, bg="#1a1a1a")
frame_units.pack()

combo_from = ttk.Combobox(frame_units, state="readonly", width=10, font=("Arial", 12))
combo_from.grid(row=0, column=0, padx=10)

tk.Label(frame_units, text="to", bg="#1a1a1a", fg="white", font=("Arial", 12)).grid(row=0, column=1)

combo_to = ttk.Combobox(frame_units, state="readonly", width=10, font=("Arial", 12))
combo_to.grid(row=0, column=2, padx=10)

# Update Units when Category Changes
def update_units(event=None):
    selected = combo_category.get()
    if selected == "Length":
        units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
    elif selected == "Weight":
        units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    elif selected == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    else:
        units = []

    combo_from['values'] = units
    combo_to['values'] = units
    if units:
        combo_from.set(units[0])
        combo_to.set(units[1])

combo_category.bind("<<ComboboxSelected>>", update_units)
update_units()

# Convert Button
convert_button = tk.Button(window, text="Convert", command=convert_units, bg="#ff69b4", fg="white", font=("Arial", 14))
convert_button.pack(pady=20)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 14), bg="#1a1a1a", fg="white")
result_label.pack()

# Run App
window.mainloop()
