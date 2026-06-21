**Project Overview**
--------------------

**Life Expectancy AI** is a county‑level **Decision Support System (DSS)** designed to explore, predict, and simulate **life expectancy** across U.S. counties. It integrates data, modeling, and interactive visualization into a single coherent pipeline demonstrating true *synthetic understanding* rather than a collection of disconnected parts.

The system allows users to:

-   Examine how factors like **income, education, obesity, and smoking** relate to life expectancy.

-   Generate **predictions** for any U.S. county.

-   Run **what‑if simulations** by adjusting variables and instantly seeing the predicted impact.

**What's Inside the Folder**
----------------------------

`LifeExpectancyAI/` contains:

-   **app.py** --- the Streamlit dashboard (main interface)

-   **model + preprocessing scripts** --- data cleaning, feature engineering, and regression model

-   **data/** --- County Health Rankings dataset (or link to source)

-   **requirements.txt** --- Python dependencies

-   **README.md** --- documentation for running and understanding the prototype

**How to Run the Prototype**
-----------------------------------------

You only need Python installed.

1.  Navigate to the `LifeExpectancyAI/` folder.

2.  Install dependencies:

    Code

    ```
    pip install -r requirements.txt

    ```

3.  Launch the dashboard:

    Code

    ```
    streamlit run app.py

    ```

Browser will open automatically.

**Data Source**
---------------

Uses the **2025 County Health Rankings** dataset from the University of Wisconsin Population Health Institute.

**Future Expansion Possibilities**
----------------------------------

-   Real‑time data integration (e.g., CDC APIs)

-   Explainable AI (e.g., SHAP)

-   Secure cloud deployment with authentication and role‑based access

**Capstone Synthesis Focus**
----------------------------

This DSS is a **synthesis**---a unified pipeline that integrates:

-   Data acquisition

-   Data cleaning

-   Modeling

-   Interactive visualization

-   Decision‑support logic

This demonstrates a *feasible synthetic understanding* by showing how each component works together to support meaningful, interpretable decisions.