import tkinter as tk
from tkinter import messagebox  

# -------------------------------
# تابع جمع دو عدد
# -------------------------------
def calculate_sum():
    try:
        # گرفتن عدد اول و دوم از ورودی‌ها
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        
        # محاسبه جمع
        result = num1 + num2
        
        # نمایش نتیجه روی لِیبل
        lbl_result.config(text=f"جواب: {result}")
    except ValueError:
        # نمایش خطا در صورت وارد کردن غیر عدد
        messagebox.showerror("خطا", "فقط عدد وارد کنيد!")

# -------------------------------
# تابع تفریق دو عدد
# -------------------------------
def calculate_sub():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        
        # محاسبه تفریق
        result = num1 - num2
        
        # نمایش نتیجه روی لِیبل
        lbl_result.config(text=f"جواب: {result}")
    except ValueError:
        messagebox.showerror("خطا", "فقط عدد وارد کنيد!")

# -------------------------------
# تابع ضرب دو عدد
# -------------------------------
def calculate_Multiplication():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        
        # محاسبه ضرب
        result = num1 * num2
        
        # نمایش نتیجه روی لِیبل
        lbl_result.config(text=f"جواب: {result}")
    except ValueError:
        messagebox.showerror("خطا", "فقط عدد وارد کنيد!")

# -------------------------------
# تابع تقسیم دو عدد
# -------------------------------
def calculate_Division():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        
        # جلوگیری از تقسیم بر صفر
        if num2 == 0:
            messagebox.showerror("خطا", "تقسيم بر صفر مجاز نيست!")
        else:
            # محاسبه تقسیم
            result = num1 / num2
            # نمایش نتیجه روی لِیبل
            lbl_result.config(text=f"جواب: {result}")
    except ValueError:
        messagebox.showerror("خطا", "فقط عدد وارد کنيد!")

# -------------------------------
# ساخت پنجره اصلی برنامه
# -------------------------------
root = tk.Tk()
root.title("ماشين حساب ساده")

# -------------------------------
# لِیبل و ورودی عدد اول
# -------------------------------
lbl1 = tk.Label(root, text="عدد اول:")
lbl1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

# -------------------------------
# لِیبل و ورودی عدد دوم
# -------------------------------
lbl2 = tk.Label(root, text="عدد دوم:")
lbl2.grid(row=1, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# -------------------------------
# دکمه جمع
# -------------------------------
btn_calc = tk.Button(root, text="جمع کن", command=calculate_sum, bg="lightblue")
btn_calc.grid(row=2, column=0, columnspan=2, sticky="we", padx=10)

# -------------------------------
# دکمه تفریق
# -------------------------------
btn_calc = tk.Button(root, text="کم کن", command=calculate_sub, bg="lightblue")
btn_calc.grid(row=3, column=0, columnspan=2, sticky="we", padx=10)

# -------------------------------
# دکمه ضرب
# -------------------------------
btn_calc = tk.Button(root, text="ضرب کن", command=calculate_Multiplication, bg="lightblue")
btn_calc.grid(row=4, column=0, columnspan=2, sticky="we", padx=10)

# -------------------------------
# دکمه تقسیم
# -------------------------------
btn_calc = tk.Button(root, text="تقسيم کن", command=calculate_Division, bg="lightblue")
btn_calc.grid(row=5, column=0, columnspan=2, sticky="we", padx=10)

# -------------------------------
# لِیبل نمایش نتیجه
# -------------------------------
lbl_result = tk.Label(root, text="جواب: ---")
lbl_result.grid(row=6, column=0, columnspan=2, pady=20)

# -------------------------------
# اجرای برنامه
# -------------------------------
root.mainloop()
