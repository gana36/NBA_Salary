
---

# NBA Player Salary Prediction Pipeline 🏀💸

This project implements an **end-to-end pipeline** designed to predict NBA player salaries. The pipeline consists of several stages: data exploration and cleaning, feature engineering, statistical testing, and multiple modeling techniques ranging from **linear regression** to **tree-based ensemble methods**.

## 1. Data Loading and Preprocessing 📂🔄

### Data Import and Cleaning:
The pipeline begins by loading NBA statistics from a **CSV file**, followed by **filling missing values** (e.g., replacing NA values with zeros for calculated metrics) to ensure that missing data does not disrupt further analysis.

### Exploratory Data Analysis (EDA) 🔍📊:
Visualizations are created using **Plotly** and **Seaborn** to explore the salary distribution, including **histograms**, **box plots**, and **scatter plots**. These visualizations help to understand the spread of the target variable and the relationships between categorical features (e.g., **team** and **position**) and numerical variables.

### Outlier Removal 🚫📉:
To mitigate the impact of extreme values on the model, the **interquartile range (IQR)** method is used to remove outliers from the salary data. By calculating the first (Q1) and third quartiles (Q3), salaries outside 1.5 times the IQR are clipped.

## 2. Feature Engineering and Transformation 🛠️🔧

### Derived Features:
New features are created to capture deeper relationships in the data, such as **per-game statistics** (e.g., points per minute), **efficiency metrics**, and **interaction features** (e.g., AST-to-TOV ratio).

### Handling Skewness and Collinearity 🔄📊:
Several transformations are applied to address skewness and collinearity in the data:
- **Log transformations** for right-skewed variables (e.g., 3-pointers, free throws).
- **Square root transformations** for moderately skewed features (e.g., steals, turnovers).
- **Cubic transformations** for left-skewed variables.

**Heatmaps** and **pairplots** to identify collinear features, which are either removed or transformed to reduce multicollinearity.

### Scaling ⚖️📐:
After encoding categorical features (using **TargetEncoder** and **LabelEncoder**), features are standardized using **StandardScaler** to ensure uniform treatment across attributes.

## 3. Modeling Approach 🎯💡

### 1. Linear Regression with Statistical Testing 🧮📊

#### Standard Model Building:
A **linear regression** model is first trained on the scaled features. The pipeline includes a custom-adjusted **R² calculation**, residual analysis, and evaluation using **RMSE**.

#### Diagnostic Tests 🔬✅:
To validate the model's assumptions, several statistical tests are applied:
- **Linearity Check**: Residual vs. fitted plots and the **Harvey-Collier test**.
- **Normality Check**: **Q-Q plots** and the **Shapiro-Wilk test**.
- **Homoscedasticity Check**: **Scale-location plots** and the **Breusch-Pagan test**.

#### Influence Measurement ⚖️👀:
**Cook’s Distance** is calculated and visualized to identify influential data points, which are removed to improve model robustness.

#### Polynomial Features 🧩:
When linearity assumptions are violated, **polynomial feature transformations** are explored to capture non-linear relationships.

### 2. Tree-Based Ensemble Approach 🌳🔮


#### Random Forest Ensemble 🌲🔧:
A **RandomForestRegressor** is used as the primary model, with key features including:
- Hyperparameter tuning via **GridSearchCV** (e.g., adjusting the number of estimators, max depth, min samples).
- **Feature selection** using **SelectFromModel** based on Random Forest importance scores.

#### Model Evaluation and Cross-Validation 📊🔄:
The model's performance is evaluated using **R² scores** and **RMSE** on both training and testing datasets. **K-fold cross-validation** is performed to ensure robustness, and adjusted **R²** is calculated to account for the number of predictors.

#### Visualization of Results 📉✨:
In addition to performance metrics, visualizations are provided, such as:
- **Actual vs. predicted plots**.
- **Residual plots** to assess error distribution.
- **Feature importance plots** highlighting the top 10 features driving predictions.

## 4. Next Steps and Extensions ⏭️🚀

Based on feature importance insights from the **Random Forests** model, further optimization using **XGBoost** or **XGBoost** on the top 10 most important features. This advanced ensemble method could enhance the predictive accuracy of the model.

## 5. Limitations and Considerations ⚠️🔍

While the pipeline provides a thorough approach to predicting NBA player salaries, there are a few limitations:
- The **dataset size** may not be large enough to capture all potential influences on salary.
- Factors such as **player experience**, **past performance**, and **external market conditions**, which are important determinants of salary, may not be fully accounted for in the current model. This could explain why certain salary predictions are less accurate.



