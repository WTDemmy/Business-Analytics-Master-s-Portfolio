from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "cleaned" / "health_life_exp.csv"
MODEL_DIR = BASE_DIR / "model"
MODEL_DIR.mkdir(exist_ok=True)

# ------------------------------------------------------------
# 1. Load Data
# ------------------------------------------------------------
df = pd.read_csv(DATA_FILE)

print(f"Dataset loaded: {df.shape[0]} rows")

# ------------------------------------------------------------
# 2. Define Features & Target
# ------------------------------------------------------------
X = df[["income", "education", "obesity", "smoking"]]
y = df["Life Expectancy"]

# ------------------------------------------------------------
# 3. Train/Test Split
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------------------------------------------
# 4. Train Model
# ------------------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------------------------------------
# 5. Evaluate Model
# ------------------------------------------------------------
y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n📊 Model Performance")
print(f"MAE (Average Error): {mae:.2f} years")
print(f"R² Score: {r2:.3f}")

# ------------------------------------------------------------
# 6. Show Feature Impact (VERY IMPORTANT FOR PRESENTATION)
# ------------------------------------------------------------
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
}).sort_values(by="Coefficient", ascending=False)

print("\n📈 Feature Importance (Impact on Life Expectancy):")
print(coefficients)

# ------------------------------------------------------------
# 7. Save Model
# ------------------------------------------------------------
model_file = MODEL_DIR / "life_exp_model.pkl"
joblib.dump(model, model_file)

print(f"\nModel saved to {model_file}")