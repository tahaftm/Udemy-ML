import streamlit as st
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("data/breast cancer.csv").drop(['id','Unnamed: 32'], axis = 1)
data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
data_without_target_df = data.drop('diagnosis', axis=1)
impute = SimpleImputer(strategy='mean')
impute.fit_transform(data_without_target_df)
scaler = MinMaxScaler().fit(data_without_target_df)
data[data_without_target_df.columns.tolist()] = scaler.transform(data_without_target_df)
input_train, input_test, target_train, target_test = train_test_split(data_without_target_df, data['diagnosis'], test_size=0.2, random_state=42)
model = LogisticRegression(solver='liblinear').fit(data_without_target_df, data['diagnosis'])

st.title("Breast Cancer Prediction – Input Form")

st.subheader("Enter Feature Values")

# ========== MEAN ==========
radius_mean = st.number_input("Radius Mean", value=13.54)
texture_mean = st.number_input("Texture Mean", value=14.36)
perimeter_mean = st.number_input("Perimeter Mean", value=87.46)
area_mean = st.number_input("Area Mean", value=566.3)
smoothness_mean = st.number_input("Smoothness Mean", value=0.09779)
compactness_mean = st.number_input("Compactness Mean", value=0.08129)
concavity_mean = st.number_input("Concavity Mean", value=0.06664)
concave_points_mean = st.number_input("Concave Points Mean", value=0.04781)
symmetry_mean = st.number_input("Symmetry Mean", value=0.1885)
fractal_dimension_mean = st.number_input("Fractal Dimension Mean", value=0.05766)

# ========== SE ==========
radius_se = st.number_input("Radius SE", value=0.2699)
texture_se = st.number_input("Texture SE", value=0.7886)
perimeter_se = st.number_input("Perimeter SE", value=2.058)
area_se = st.number_input("Area SE", value=23.56)
smoothness_se = st.number_input("Smoothness SE", value=0.008468)
compactness_se = st.number_input("Compactness SE", value=0.01773)
concavity_se = st.number_input("Concavity SE", value=0.03001)
concave_points_se = st.number_input("Concave Points SE", value=0.01198)
symmetry_se = st.number_input("Symmetry SE", value=0.02105)
fractal_dimension_se = st.number_input("Fractal Dimension SE", value=0.002932)

# ========== WORST ==========
radius_worst = st.number_input("Radius Worst", value=15.11)
texture_worst = st.number_input("Texture Worst", value=19.26)
perimeter_worst = st.number_input("Perimeter Worst", value=99.7)
area_worst = st.number_input("Area Worst", value=711.2)
smoothness_worst = st.number_input("Smoothness Worst", value=0.144)
compactness_worst = st.number_input("Compactness Worst", value=0.1773)
concavity_worst = st.number_input("Concavity Worst", value=0.239)
concave_points_worst = st.number_input("Concave Points Worst", value=0.1288)
symmetry_worst = st.number_input("Symmetry Worst", value=0.2977)
fractal_dimension_worst = st.number_input("Fractal Dimension Worst", value=0.07259)

# ========== DICTIONARY ==========
input_data = {
    "radius_mean": radius_mean,
    "texture_mean": texture_mean,
    "perimeter_mean": perimeter_mean,
    "area_mean": area_mean,
    "smoothness_mean": smoothness_mean,
    "compactness_mean": compactness_mean,
    "concavity_mean": concavity_mean,
    "concave_points_mean": concave_points_mean,
    "symmetry_mean": symmetry_mean,
    "fractal_dimension_mean": fractal_dimension_mean,

    "radius_se": radius_se,
    "texture_se": texture_se,
    "perimeter_se": perimeter_se,
    "area_se": area_se,
    "smoothness_se": smoothness_se,
    "compactness_se": compactness_se,
    "concavity_se": concavity_se,
    "concave_points_se": concave_points_se,
    "symmetry_se": symmetry_se,
    "fractal_dimension_se": fractal_dimension_se,

    "radius_worst": radius_worst,
    "texture_worst": texture_worst,
    "perimeter_worst": perimeter_worst,
    "area_worst": area_worst,
    "smoothness_worst": smoothness_worst,
    "compactness_worst": compactness_worst,
    "concavity_worst": concavity_worst,
    "concave_points_worst": concave_points_worst,
    "symmetry_worst": symmetry_worst,
    "fractal_dimension_worst": fractal_dimension_worst
}

pred = int(model.predict(pd.DataFrame([input_data]))[0])
if pred == 1:
    st.write("The model predicted that the breast cancer is Malignant")
else:
    st.write("The model predicted that the breast cancer is Benign")