import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt

class BMICalculator:
    def __init__(self, window):
        self.window = window
        self.window.title("BMI Calculator")

        self.name_label = ttk.Label(window, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = ttk.Entry(window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        self.height_label = ttk.Label(window, text="Height (m):")
        self.height_label.grid(row=1, column=0, padx=10, pady=10)
        self.height_entry = ttk.Entry(window)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)

        self.weight_label = ttk.Label(window, text="Weight (kg):")
        self.weight_label.grid(row=2, column=0, padx=10, pady=10)
        self.weight_entry = ttk.Entry(window)
        self.weight_entry.grid(row=2, column=1, padx=10, pady=10)

        self.save_button = ttk.Button(window, text="Save Data", command=self.save_data)
        self.save_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.display_button_pie = ttk.Button(window, text="Display BMI Pie Chart", command=self.display_bmi_pie_chart)
        self.display_button_pie.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.display_button_bar = ttk.Button(window, text="Display BMI Bar Chart", command=self.display_bmi_bar_chart)
        self.display_button_bar.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def save_data(self):
        try:
            name = self.name_entry.get()
            height = float(self.height_entry.get())
            weight = float(self.weight_entry.get())
            if height <= 0 or weight <= 0:
                raise ValueError("Height and weight must be positive numbers.")
            bmi = weight / (height ** 2)
            category = self.get_bmi_category(bmi)
            with open("user_data.txt", "a") as file:
                file.write(f"{name},{height},{weight},{bmi},{category}\n")
            messagebox.showinfo("Saved", "User data saved successfully.")
            print(f"{name}, your BMI is {bmi:.2f} and you are {category.lower()}.")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid data.")

    def display_bmi_pie_chart(self):
        self.display_bmi_chart(chart_type='pie')

    def display_bmi_bar_chart(self):
        self.display_bmi_chart(chart_type='bar')

    def display_bmi_chart(self, chart_type='pie'):
        try:
            with open("user_data.txt", "r") as file:
                categories = {'Underweight': 0, 'Normal': 0, 'Overweight': 0, 'Obese': 0}
                for line in file:
                    _, _, _, bmi, category = line.strip().split(",")
                    categories[category] += 1

            labels = list(categories.keys())
            sizes = list(categories.values())

            if chart_type == 'pie':
                plt.figure(figsize=(6, 6))
                plt.pie(sizes, labels=labels, autopct='%1.1f%%')
                plt.title('BMI Distribution (Pie Chart)')
                plt.show()
            elif chart_type == 'bar':
                plt.figure(figsize=(6, 6))
                plt.bar(labels, sizes, color=['blue', 'green', 'yellow', 'red'])
                plt.xlabel('BMI Categories')
                plt.ylabel('Number of People')
                plt.title('BMI Distribution (Bar Chart)')
                plt.show()
        except FileNotFoundError:
            messagebox.showinfo("No Data", "No user data available to display BMI chart.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return 'Underweight'
        elif 18.5 <= bmi < 25:
            return 'Normal'
        elif 25 <= bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

def main():
    window = tk.Tk()
    app = BMICalculator(window)
    window.mainloop()


main()
