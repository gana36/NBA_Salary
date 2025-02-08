<img src="https://github.com/user-attachments/assets/3d29b1ac-5870-43d3-bfb7-969ff68cc8ec" width="500"/>


---

# NBA Player Salary Prediction Pipeline 🏀💸

**End-to-end pipeline** to predict NBA player salaries. Includes the following stages: data exploration and cleaning, feature engineering, statistical testing, finally **linear regression** and **tree-based ensemble methods**.

## 1. Data Loading and Preprocessing 📂🔄

### Data Import and Cleaning:
**Filling missing** values (e.g., replacing NA values with zeros for certain columns based on the attribute description).

### Exploratory Data Analysis (EDA) 🔍📊:
Used **Plotly** and **Seaborn** to explore the salary distribution, including **histograms**, **box plots**, and **scatter plots**. These visualizations are useful in understanding the spread of the target variable and the relationships between categorical features (e.g **team** and **position**) and numerical variables.

### Outlier Removal 🚫📉:
To reduce the impact of extreme values on the model, the **interquartile range (IQR)** method is used to remove outliers from the salary data. Salaries outside 1.5 times the IQR are removed.

## 2. Feature Engineering and Transformation 🛠️🔧

### Derived Features:
New features are created to capture deeper relationships in the data, such as **per-game statistics** (e.g., points per minute), **efficiency metrics**, and **interaction features** (e.g., AST-to-TOV ratio).

### Handling Skewness and Collinearity 🔄📊:
Several transformations are applied to address skewness and collinearity in the data:
- **Log transformations** for right-skewed variables (e.g., 3-pointers, free throws).
- **Square root transformations** for moderately skewed features (e.g., steals, turnovers).
- **Cubic transformations** for left-skewed variables.

**Heatmaps** and **pairplots** are used to identify collinear features, which are either removed or transformed to reduce multicollinearity.

### Scaling ⚖️📐:
After encoding categorical features (using **TargetEncoder** and **LabelEncoder**), features are standardized using **StandardScaler** to ensure uniform treatment across attributes.

## 3. Modeling Approach 🎯💡

### 1. Linear Regression with Statistical Testing 🧮📊

#### Standard Model Building:
A **linear regression** model is first trained on the scaled features. adjusted **R²**, residual analysis, and evaluation using **RMSE**.

#### Diagnostic Tests 🔬✅:
To validate the model's assumptions, several statistical tests are applied:
- **Linearity Assumption**: Residual vs. fitted plots and the **Harvey-Collier test**.
- **Normality Assumption**: **Q-Q plots** and the **Shapiro-Wilk test**.
- **Homoscedasticity Assumption**: **Residual vs. fitted plots** and the **Breusch-Pagan test**.

#### Influence Measurement ⚖️👀:
**Cook’s Distance** is used to identify influential data points, which are removed to improve model robustness.

#### Polynomial Features 🧩:
When linearity assumptions are violated, **polynomial feature transformations** are explored to capture non-linear relationships. But they couldn’t improve the models prediction ability. 

### 2. Tree-Based Ensemble Approach 🌳🔮


#### Random Forest Ensemble 🌲🔧:
A **RandomForestRegressor** is used with the following adjustments:
- Hyperparameter tuning via **GridSearchCV** (e.g., adjusting the number of estimators, max depth, min samples).
- **Feature selection** using **SelectFromModel** based on Random Forest importance scores.

#### Model Evaluation and Cross-Validation 📊🔄:
The model's performance is evaluated using **Adjusted R² scores** and **RMSE** on both training and testing datasets. To ensure robustness **K-fold cross-validation** is performed.

#### Visualization of Results 📉✨:
In addition to performance metrics, visualizations are plotted for Random Forest, such as:
- **Actual vs. predicted plots**.
- **Residual plots** to assess error distribution.
- **Feature importance plots** highlighting the top 10 features driving predictions.


## 4. Limitations and Considerations ⚠️🔍

While the pipeline provides a thorough approach to predicting NBA player salaries, there are a few limitations:
- The **dataset size** is not be large enough to capture all potential influences on salary.
- Factors such as **player experience**, **past performance**, and **external market conditions**, which are important determinants of salary, are not fully accounted in the dataset. This could explain why the models failed to generalize and predict the salary.
