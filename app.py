import streamlit as st
import server

backend = server.connection_handler()


if __name__ == "__main__":
    st.title("ML HUB")

    uploaded_file = st.file_uploader("Upload a file", type=["csv"])

    if uploaded_file is None:
        st.stop()
    elif not backend.load_data(uploaded_file):
        if backend.data_isempty():
            st.error("you have uploaded an empty file, please upload again")
        st.stop()
    else:
        st.success("file upload was successful")
    
    dataset, train = st.tabs(["Dataset", "Train"])
    with dataset:
        st.write(backend.get_data())

    with train:
        train, config = st.columns(2)
        with config:
            st.subheader("model configuration")
            task = st.radio("select a task type", ["Classification", "Regression"],index=None)
            features = st.multiselect("Select features", backend.get_columns())
            target = st.selectbox("Select target", [x for x in backend.get_columns() if x not in features], index=None)
            backend.set_user_config(task, features, target)
        
        with train:
            st.subheader("model training")
            config = backend.get_user_config()
            st.write("Task:",config["task"]if config["task"] else '')
            st.write("Features:", ",".join(config["features"]))
            st.write("Target:", config["target"] if config["target"] else '')
            st.write("model:", backend.get_model() if backend.get_model() else '')

            if st.button("Train model"):
                st.divider()
                if backend.init_model_training():
                    st.success("model training was a success")
                    st.write(backend.get_model_score())
