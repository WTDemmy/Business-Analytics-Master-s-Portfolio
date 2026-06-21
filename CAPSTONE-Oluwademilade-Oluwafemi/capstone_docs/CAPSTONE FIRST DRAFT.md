Capstone Project Proposal First Draft
===============================================

Title:
--------------

## A Predictive Life Expectancy Decision System Using U.S. Government Data 

* * * * *

1\. Project Overview and Problem Statement
==========================================

Life expectancy varies significantly across regions in the United States due to a combination of socioeconomic, demographic, and public health factors. Despite the availability of large-scale government datasets, there is no simple, integrated system that allows users to easily analyze and predict life expectancy outcomes based on these variables.

This project aims to address that gap by developing a *data-driven decision intelligence system* that integrates multiple public datasets to predict life expectancy and identify key contributing factors.

The system will leverage publicly available data from sources such as the Centers for Disease Control and Prevention and the United States Census Bureau to provide a simplified but functional predictive model and user-facing interface.

* * * * *

2\. Purpose and Objectives
==========================

The purpose of this capstone project is to demonstrate the synthesis of key CISBA curricular areas through the development of a working prototype system.

### Objectives:

-   Build a predictive model for life expectancy using public datasets

-   Integrate multiple data sources into a unified dataset

-   Develop a functional web-based prototype (dashboard)

-   Identify key drivers influencing life expectancy

-   Translate analytical outputs into a user-friendly decision-support system

* * * * *

3\. Synthesis Prototype Project Demo (Artifact)
===============================================

The primary artifact will be a **working web-based application** built using Python and Streamlit.

### Core Features:

-   User selects a state or region

-   System outputs:

    -   Predicted life expectancy

    -   Risk classification (Low / Medium / High)

    -   Key contributing factors (e.g., income, education, population density)

### Technical Components:

-   Data ingestion and preprocessing

-   Predictive modeling (Linear Regression and/or Random Forest)

-   Interactive user interface

The system will be hosted and maintained in the WTAMU GitHub repository and will include all datasets, scripts, and documentation required to run the application.

* * * * *

4\. Curricular Area Synthesis
=============================

This project demonstrates the integration of at least three (and ultimately all four) CISBA curricular areas:

### Software Systems (SS)

-   Development of a functional application using Python and Streamlit

-   Implementation of user interaction and system logic

### Business Analytics (BA)

-   Application of predictive modeling techniques

-   Analysis of relationships between socioeconomic variables and life expectancy

-   Interpretation of model outputs and insights

### Data Management (DM)

-   Collection and integration of datasets from multiple public sources

-   Data cleaning, transformation, and structuring

-   Management of datasets within the system pipeline

### Cybersecurity and Networking (CN)

-   Consideration of data privacy and ethical use of public health data

-   Identification of potential risks in data interpretation and system misuse

-   Discussion of secure handling of datasets within the application

* * * * *

5\. Data Sources and Feasibility
================================

The project will utilize publicly available datasets from:

-   Centers for Disease Control and Prevention (life expectancy, mortality data)

-   United States Census Bureau (demographic and socioeconomic data)

-   Data.gov (aggregated public datasets)

These datasets are:
-   Large-scale and reliable
-   Freely accessible
-   Structured for analytical use
  The project will use a subset of variables from each dataset to ensure manageable scope and clean integration, focusing on county-level analysis where possible.

Data Sources (Sample)
---------------------

The project will utilize publicly available datasets including:

-   Life expectancy data from the Centers for Disease Control and Prevention USALEEP project:\
    <https://www.cdc.gov/nchs/nvss/usaleep/usaleep.html>
-   Socioeconomic data from the United States Census Bureau American Community Survey:\
    <https://data.census.gov/>
-   Health indicator data from the Centers for Disease Control and Prevention BRFSS system:\
    <https://www.cdc.gov/brfss/index.html>
-   Optional economic indicators from the Federal Reserve Economic Data:\
    <https://fred.stlouisfed.org/>
* * * * *

6\. Methodology
===============

The project will follow a structured analytical and system development process:

1.  Data Collection
    -   Acquire datasets from government sources 

2.  Data Preparation
    -   Clean missing values
    -   Merge datasets by geographic identifiers (state/county)

3.  Exploratory Data Analysis (EDA)
    -   Identify trends and relationships

4.  Model Development
    -   Build predictive models (Linear Regression, Random Forest)
    -   Evaluate model performance

5.  System Development
    -   Build Streamlit-based dashboard
    -   Integrate model outputs into UI

6.  Testing and Validation
    -   Ensure system functionality
    -   Validate outputs for consistency

* * * * *

7\. Synthesis Paper Plan (≤ 5 Pages)
====================================
The accompanying paper will:

-   Define the foundational concepts of:
    -   Software Systems (SS)
    -   Business Analytics (BA)
    -   Data Management (DM)
    -   Cybersecurity and Networking (CN)

-   Explain how these areas are integrated within the project
-   Reference prior coursework and portfolio projects (e.g., security audits, C# systems, analytics work)
-   Justify the feasibility and relevance of the prototype

* * * * *

8\. Presentation Plan
=====================

The presentation will include:
-   Overview of the problem and motivation
-   Demonstration of the working prototype
-   Explanation of system architecture
-   Discussion of how the project reflects curricular synthesis
-   Future expansion possibilities

* * * * *

9\. Portfolio Integration (GitHub)
==================================
The project will be fully integrated into the existing portfolio repository with the following structure:
-   Main README (overview of student and portfolio)
-   Separate folders for:
    -   Software Systems (SS)
    -   Business Analytics (BA)
    -   Data Management (DM)
    -   Cybersecurity and Networking (CN)

-   Synthesis Project folder containing:

    -   Source code
    -   Datasets
    -   README documentation
    -   Final report
    -   Presentation slides
    -   Video recording

* * * * *

10\. Feasibility and Scope
==========================

This project is designed to be:
-   Buildable within the semester timeframe
-   Technically achievable with available tools (Python, Streamlit)
-   Scalable for future expansion

The prototype will prioritize:
-   Simplicity
-   Functionality
-   Clear demonstration of synthesis

* * * * *

11\. Future Vision
==================

A fully realized version of this system could:

-   Incorporate real-time data updates
-   Expand to additional health and economic indicators
-   Support policy analysis and decision-making
-   Integrate more advanced machine learning models and explainability tools

* * * * *

