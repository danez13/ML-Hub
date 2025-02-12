# ML-Hub
## Scope
### Overview
---
* __Project name:__ ML Hub
* __Objective:__ The platform will enable data scientists and machine learning practitioners to store and process datasets. as well as train, and evaluate machine learning models all in one place.

* __Target Audience:__ Data scientists, machine learning engineers, researchers, and developers.
### Core Features and Functionalities
---
1. user authentication & Profiles
    * __Login/Signup:__ Users can create an account using email and password, or third-party authentication _(OAuth via Google, GitHub, etc.)_.
    
    * __User Profile:__ A profile page where users can manage account settings, view stored datasets and models, and track their progress.
1. Database Management
    * __upload datasets:__ Users can upload various types of datasets _(CSV, JSON, Excel, etc.)_.
    * __Data Exploration:__ Basic data visualization and preview capabilities for users to inspect their datasets _(e.g., first few rows, column types, summary stats)_.
    * __Data Processing:__ Users can preprocess datasets _(e.g., clean data, normalize, handle missing values, etc.)_ using a set of pre-built functions or custom scripts.
  
    * __Dataset Versioning:__ Keep track of different versions of datasets, allowing users to roll back to earlier versions if needed.
2. Model Management
    * __Create Models:__ Users can define, create, and configure machine learning models _(e.g., choose algorithms, set hyperparameters)_.
    * __Training:__ Train models on the datasets uploaded by users. The platform should allow users to define the training process _(epochs, batch size, learning rate, etc.)_.
    * __Model Evaluation:__ Evaluate the models using standard metrics _(accuracy, precision, recall, confusion matrix, etc.)_ and visualize results _(e.g., ROC curves, loss plots)_.
    
    * __Model Versioning:__ Keep track of model versions so users can compare performance over time and rollback to previous iterations if necessary.
   
3. Experiment Tracking
    * __Track Experiments:__ Users can log and track experiments _(datasets used, hyperparameters, model configurations, performance metrics)_.
    
    * __Compare Experiments:__ Compare different models or training runs side by side to identify the best-performing approach.
4. Sharing
    * __Share Datasets and Models:__ Users can share their datasets and models with others _(public/private access)_.
    
    * __Collaborative Projects:__ Allow users to work together on datasets or models by adding collaborators with different permission levels _(e.g., read-only, edit, manage)_.

### Technical Requirements
---
#### Front End (React)
1. __Dashboard:__ Display datasets, models, experiment logs, and performance statistics in an organized way.
1. __Data Management Interface:__ Create a user-friendly interface to upload, preview, and explore datasets.
1. __Model Training Interface:__ Allow users to configure model parameters and track the training process in real-time.

1. __Results Visualization:__ Provide charts, graphs, and other visual components to display model evaluation results, like confusion matrices, ROC curves, and accuracy graphs.

#### Back End (springboot/ flask)
1. __User Authentication:__ Implement OAuth2/JWT-based authentication for secure login.
2. __File Storage:__ Use cloud storage like AWS S3 or a local file system to store datasets and models.
3. __Model Training:__
    * Run model training processes, either on the server or offload to external computation environments _(e.g., AWS EC2 or a GPU-enabled machine)_.
    * Use libraries like TensorFlow, PyTorch, or Scikit-learn for machine learning.

4. __Experimental Tracking:__ Store logs and metrics of various model training experiments in a database (PostgreSQL or MongoDB).

#### Database
1. __Relational Database (MySQL):__ For storing user data, experiment results, and model metadata.

2. __Document Database (MongoDB):__ Can be used for storing unstructured data like model weights, hyperparameters, or data logs.

### Non-Functional Features
---
* __Performance:__ Ensure that datasets can be processed efficiently, and model training doesn’t cause long delays. Implement caching or parallel processing where possible.
* __Security:__ Ensure that datasets and models are securely stored, and user data is protected.
* __Scalability:__ The platform should scale efficiently to handle large datasets and high computational loads, especially when model training is involved.
