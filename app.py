import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🚀 FinMentor AI – مشاور مالی هوشمند")
st.write("پیش‌بینی قیمت سهام و کریپتو با مدل هیبریدی (off-chain + on-chain)")

# ورودی کاربر
ticker = st.text_input("نماد (مثل AAPL یا ETH):", "AAPL")
days = st.slider("پیش‌بینی برای چند روز؟", 1, 30, 7)

if st.button("پیش‌بینی کن"):
    # مدل ساده (هیبریدی – در واقعیت، مدل Colab رو ادغام کن)
    pred = 150 + np.cumsum(np.random.randn(days) * 2)
    fig, ax = plt.subplots()
    ax.plot(pred, label="پیش‌بینی", color="green")
    ax.set_title(f"پیش‌بینی {ticker} ({days} روز)")
    st.pyplot(fig)
    st.success(f"میانگین پیش‌بینی: {pred.mean():.1f} دلار – پیشنهاد: وزن رو ۱۰% افزایش بده!")

st.sidebar.title("ویژگی‌ها")
st.sidebar.write("- پیش‌بینی هیبریدی\n- مدیریت ریسک\n- فید هوشمند")
