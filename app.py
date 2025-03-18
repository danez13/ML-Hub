import streamlit as st
import server

backend = server.connection_handler()


if __name__ == "__main__":
    st.title("ML HUB")

    uploaded_file = st.file_uploader("Upload a file", type=["csv"])
    if not uploaded_file:
        st.warning("please upload a dataset file to access more features")
    elif not backend.load_data(uploaded_file):
        if backend.data_isempty():
            st.error("you have uploaded an empty file, please upload again")
        st.stop()
    else:
        file_upload_success = st.success("file upload was successful")
    
    dataset_tab, model_tab, train_tab = st.tabs(["Dataset", "Model", "Train"])
    with dataset_tab:
        st.subheader("Dataset processing")

        if uploaded_file is None:
            st.stop()

        with st.expander("Dataset Configuration"):
            tab1, tab2, transformation_preview_column = st.columns(3)

            with transformation_preview_column:
                st.write("###### Preview Management")
                if st.button("apply changes"):
                    backend.data_apply_preview()

                
        current_tab, preview_tab = st.tabs(["Current", "Preview"])
        with current_tab:
            st.write(backend.get_current_data())
        with preview_tab:
            st.write(backend.get_preview_data())


    with model_tab:
        st.subheader("Model configuration")
        if uploaded_file is None:
            pass
        else:
            task = st.radio("select a task type", ["Classification", "Regression"],index=None)
            features = st.multiselect("Select features", backend.get_columns())
            target = st.selectbox("Select target", [x for x in backend.get_columns() if x not in features], index=None)
            backend.set_user_config(task, features, target)

    with train_tab:
        st.subheader("Model training")
        
        config = backend.get_user_config()
        st.write("Task:",config["task"]if config["task"] else '')
        st.write("Features:", ",".join(config["features"]))
        st.write("Target:", config["target"] if config["target"] else '')
        st.write("Model:", backend.get_model() if backend.get_model() else '')
        
        if not config["task"] and not config["target"] and len(config["features"])==0:
            st.warning("please set model configuration")
            st.stop()
        
        if st.button("Train model"):
            st.divider()
            if backend.init_model_training():
                st.success("model training was a success")
                st.write("Accuracy score:",backend.get_model_score())

