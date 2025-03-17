import streamlit as st
from io import StringIO
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LinearRegression
st.title("ML HUB")
uploaded_file = st.file_uploader("Upload a file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    dataset, train = st.tabs(["Dataset", "Train"])
    with dataset:
        st.write(data)
    with train:
        modeling,configs = st.columns(2)
        with configs:
            task = st.radio("select a task type", ["Classification", "Regression"],index=None)
            features = st.multiselect("Select features", data.columns)
            target = st.selectbox("Select target", data.drop(features, axis=1).columns, index=None)
        with modeling:
            st.write("Modeling")
            st.write("Task:", task if task else '')
            st.write("Features:", ", ".join(features))
            st.write("Target:", target if target else '')
            if st.button("Train"):
                if task == "Classification":
                    model = KNeighborsClassifier()
                else:
                    model = LinearRegression()
                model.fit(data[features], data[target])
                st.success("Model trained successfully")
                st.write("Model score:", model.score(data[features], data[target]))
else:
    st.write("Please upload a file")
