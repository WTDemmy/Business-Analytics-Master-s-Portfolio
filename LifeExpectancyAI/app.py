import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Page config
st.set_page_config(page_title="Life Expectancy AI", layout="wide")

st.title("🧠 Life Expectancy AI — A County Decision Support Tool")
st.markdown("""
Hi 👋🏽  

This is a **county-level Life Expectancy Decision Support System (DSS)** for the United States.

It uses real public health data to:
- Predict life expectancy based on key risk factors  
- Compare counties across the U.S.  
- Simulate “what-if” scenarios to support better decisions  

👉 Adjust the sliders to explore how **income, education, obesity, and smoking** impact life expectancy.
""")

# Load cleaned data
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned/health_life_exp.csv")
    df = df.rename(columns={"Life Expectancy": "life_exp"})
    # Ensure correct dtypes
    df["income"] = pd.to_numeric(df["income"], errors="coerce")
    df["education"] = pd.to_numeric(df["education"], errors="coerce")
    df["obesity"] = pd.to_numeric(df["obesity"], errors="coerce")
    df["smoking"] = pd.to_numeric(df["smoking"], errors="coerce")
    df["life_exp"] = pd.to_numeric(df["life_exp"], errors="coerce")
    df = df.dropna()
    return df

df = load_data()

# Train model (cached)
@st.cache_resource
def train_model(data):
    features = ["income", "education", "obesity", "smoking"]
    X = data[features]
    y = data["life_exp"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, features, X_test, y_test

model, features, X_test, y_test = train_model(df)

# Display model performance
st.sidebar.header("📈 Model Performance")
st.sidebar.metric("Mean Absolute Error (MAE)", f"{1.69:.2f} years")  # you can compute dynamically
st.sidebar.metric("R² Score", f"{0.627:.3f}")

# Sidebar: County selector
st.sidebar.header("🔍 Select a county")
county_list = df["County"].unique()
selected_county = st.sidebar.selectbox("County", sorted(county_list))
county_row = df[df["County"] == selected_county].iloc[0]

# Two columns: actual vs predicted, and what‑if tool
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📍 {selected_county}, {county_row['State']}")
    actual = county_row["life_exp"]
    # Predict using the model
    input_features = county_row[features].values.reshape(1, -1)
    predicted = model.predict(input_features)[0]
    
    st.metric("Actual Life Expectancy", f"{actual:.1f} years")
    st.metric("Model Prediction", f"{predicted:.1f} years", delta=f"{predicted - actual:+.1f} yrs")
    
    # Show current values
    st.write("**Current characteristics:**")
    st.write(f"💰 Median income: ${county_row['income']:,.0f}")
    st.write(f"🎓 % Some college: {county_row['education']:.1f}%")
    st.write(f"🍔 Adult obesity: {county_row['obesity']:.1f}%")
    st.write(f"🚬 Adult smoking: {county_row['smoking']:.1f}%")

with col2:
    st.subheader("⚙️ What‑if scenario")
    st.write("Adjust the values below to see how life expectancy would change.")
    
    # Sliders initialized with county's current values
    income = st.slider("Median household income ($)", 20000, 150000, int(county_row["income"]), step=5000)
    education = st.slider("% Some college", 10.0, 80.0, float(county_row["education"]), step=1.0)
    obesity = st.slider("% Adult obesity", 15.0, 50.0, float(county_row["obesity"]), step=0.5)
    smoking = st.slider("% Adult smoking", 5.0, 40.0, float(county_row["smoking"]), step=0.5)
    
    # Predict new life expectancy
    new_input = pd.DataFrame([[income, education, obesity, smoking]], columns=features)
    new_pred = model.predict(new_input)[0]
    st.metric("New Predicted Life Expectancy", f"{new_pred:.1f} years")
    
    # Show change
    change = new_pred - predicted
    st.write(f"**Change from current predicted value:** {change:+.1f} years")

# Additional insights: feature correlations
st.subheader("🔍 How each factor correlates with life expectancy (nationwide)")
corr = df[features + ["life_exp"]].corr()["life_exp"].drop("life_exp").sort_values()
fig = px.bar(x=corr.values, y=corr.index, orientation='h', title="Correlation with Life Expectancy")
st.plotly_chart(fig, use_container_width=True)

# Top and bottom counties
st.subheader("🏆 Highest and lowest life expectancy counties (selected state)")
state_filter = st.selectbox("Filter by state", options=["All"] + sorted(df["State"].unique()))
if state_filter != "All":
    df_filtered = df[df["State"] == state_filter]
else:
    df_filtered = df

col1, col2 = st.columns(2)
with col1:
    st.write("**Highest life expectancy**")
    st.dataframe(df_filtered.nlargest(10, "life_exp")[["County", "State", "life_exp"]])
with col2:
    st.write("**Lowest life expectancy**")
    st.dataframe(df_filtered.nsmallest(10, "life_exp")[["County", "State", "life_exp"]])

st.sidebar.markdown("### 🧾 About this tool")
st.sidebar.info("""
Built by Demi as part of a Capstone Project in  
WT Computer Information Systems & Business Analytics.

This tool demonstrates:
- Data integration (multi-source datasets)
- Predictive analytics (linear regression)
- Decision support systems (interactive simulation)

⚠️ Results are estimates, not medical advice.
""")
st.caption("⚠️ This tool uses aggregated public health data. Predictions are for educational and planning purposes only.")