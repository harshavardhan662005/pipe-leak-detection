import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. App Header
st.set_page_config(page_title="PipeGuard AI", page_icon="💧")
st.title("💧 PipeGuard: Real-Time Leak Detection")
st.markdown("Monitoring underground water infrastructure using acoustic and pressure sensors.")

# 2. Sidebar - Controls
st.sidebar.header("Dashboard Controls")
if st.sidebar.button('Refresh Sensor Data'):
    st.sidebar.success("Syncing with Virtual Sensors...")

# 3. Load Data
df = pd.read_csv('sensor_data.csv')

# 4. High-Level Metrics (The "Status Cards")
latest_pressure = df['Water_Pressure'].iloc[-1]
avg_pressure = df['Water_Pressure'].mean()

col1, col2 = st.columns(2)
col1.metric("Current Pressure", f"{latest_pressure:.2f} PSI", delta_color="inverse")
col2.metric("System Health", "CRITICAL" if latest_pressure < 20 else "HEALTHY")

# 5. The Visual Graph
st.subheader("Live Sensor Feeds")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df.index, df['Water_Pressure'], label="Pressure", color="#1f77b4")
ax.plot(df.index, df['Acoustic_Vibration']*10, label="Vibration (x10)", color="#ff7f0e")
ax.axhline(y=20, color='r', linestyle='--', label="Danger Zone")
ax.legend()
st.pyplot(fig)

# 6. Automated Alerts
if latest_pressure < 20:
    st.error(f"🚨 ALERT: Burst detected at index {df.index[-1]}! Immediate action required.")
else:
    st.success("✅ System stable. No leaks detected.")

# 7. Data Table
with st.expander("See Raw Sensor Logs"):
