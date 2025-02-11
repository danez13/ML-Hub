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
    * Login/Signup
      * Users can create an account using email and password, or third-party authentication (OAuth via Google, GitHub, etc.).
    * User Profile
      * A profile page where users can manage account settings, view stored datasets and models, and track their progress.
2. Database Management
    * upload datasets
      * Users can upload various types of datasets (CSV, JSON, Excel, etc.).
    * Data Exploration
      * Basic data visualization and preview capabilities for users to inspect their datasets (e.g., first few rows, column types, summary stats).
    * Data Processing
      * Users can preprocess datasets (e.g., clean data, normalize, handle missing values, etc.) using a set of pre-built functions or custom scripts.
    * Dataset Versioning
      * Keep track of different versions of datasets, allowing users to roll back to earlier versions if needed.
3. Model Management
    * Create Models
      * Users can define, create, and configure machine learning models (e.g., choose algorithms, set hyperparameters).
    * Training
      * Train models on the datasets uploaded by users. The platform should allow users to define the training process (epochs, batch size, learning rate, etc.).
    * Model Evaluation
      * Evaluate the models using standard metrics (accuracy, precision, recall, confusion matrix, etc.) and visualize results (e.g., ROC curves, loss plots).
    * Model Versioning
      * Keep track of model versions so users can compare performance over time and rollback to previous iterations if necessary.
   
4. Experiment Tracking
    * Track Experiments
      * Users can log and track experiments (datasets used, hyperparameters, model configurations, performance metrics).
    * Compare Experiments
      * Compare different models or training runs side by side to identify the best-performing approach.
5. Sharing
    * Share Datasets and Models
      * Users can share their datasets and models with others (public/private access).
    * Collaborative Projects
      * Allow users to work together on datasets or models by adding collaborators with different permission levels (e.g., read-only, edit, manage).

### Technical Requirements
---
#### Front End (React)
1. Dashboard
    * Display datasets, models, experiment logs, and performance statistics in an organized way.
2. Data Management Interface
    * Create a user-friendly interface to upload, preview, and explore datasets.
3. Model Training Interface
    * Allow users to configure model parameters and track the training process in real-time.
4. Results Visualization
    * Provide charts, graphs, and other visual components to display model evaluation results, like confusion matrices, ROC curves, and accuracy graphs.
#### Back End (springboot/ flask)
1. User Authentication
    * Implement OAuth2/JWT-based authentication for secure login.
2. File Storage
    * Use cloud storage like AWS S3 or a local file system to store datasets and models.
3. Model Training
    * Run model training processes, either on the server or offload to external computation environments (e.g., AWS EC2 or a GPU-enabled machine).
    * Use libraries like TensorFlow, PyTorch, or Scikit-learn for machine learning.
4. Experimental Tracking
    * Store logs and metrics of various model training experiments in a database (PostgreSQL or MongoDB).
#### Database
1. Relational Database (MySQL)
    * For storing user data, experiment results, and model metadata.
2. Document Database (MongoDB)
    * Can be used for storing unstructured data like model weights, hyperparameters, or data logs.

### Non-Functional Features
---
* Performance
  * Ensure that datasets can be processed efficiently, and model training doesn’t cause long delays. Implement caching or parallel processing where possible.
* Security:
  * Ensure that datasets and models are securely stored, and user data is protected.
* Scalability
  * The platform should scale efficiently to handle large datasets and high computational loads, especially when model training is involved.


## Road map 
Phase 1: Setup & Architecture Planning 🏗️
🔹 Define project structure, select tools, and set up repositories.
🔹 Tasks:
✅ Set up GitHub/GitLab repository.
✅ Define backend architecture (FastAPI + Spring Boot).
✅ Define database schema (PostgreSQL, MinIO for storage).
✅ Set up Docker for local development.

💡 Why?
Getting a structured foundation prevents rework later.

2️⃣ Phase 2: Backend Development (Spring Boot & FastAPI) ⚙️
🔹 Start with Spring Boot as the API gateway & user management system.
🔹 Develop FastAPI for dataset processing and ML workflows.

Tasks:
✅ Spring Boot (Java) Development

Implement JWT-based authentication (/auth/register, /auth/login).
Develop user management APIs (/users/profile).
Create dataset metadata storage APIs (/datasets/upload, /datasets/list).
Implement task orchestration for training jobs (/tasks/start-training).
✅ FastAPI (Python) Development

Set up ML pipeline (dataset preprocessing, training, evaluation).
Implement model training APIs (/ml/train, /ml/evaluate).
Integrate MinIO/AWS S3 storage for dataset handling.
💡 Why?
The backend is the foundation; the frontend will consume its APIs.

3️⃣ Phase 3: Database & Storage Setup 🗄️
🔹 Implement the PostgreSQL database schema & configure MinIO for object storage.

Tasks:
✅ Write SQL migration scripts (using Liquibase/Flyway for Spring Boot).
✅ Implement database models for Users, Datasets, Models, Experiments.
✅ Connect MinIO/AWS S3 for dataset & model storage.

💡 Why?
You need structured data storage before building frontend interactions.

4️⃣ Phase 4: Frontend Development (React + API Integration) 🎨
🔹 Build the React UI, integrating backend APIs for user authentication, dataset uploads, and ML model training.

Tasks:
✅ Set up a React project (Next.js or Vite for faster performance).
✅ Implement user authentication (JWT-based login/register UI).
✅ Develop dataset management UI (upload, view, delete datasets).
✅ Implement ML model training UI (select dataset, configure model, track progress).
✅ Show real-time training updates using WebSockets or polling.

💡 Why?
A working frontend allows users to interact with the system!

5️⃣ Phase 5: Deployment & Scaling 🌍
🔹 Deploy backend services on AWS/GCP/Azure, containerized with Docker & Kubernetes.

Tasks:
✅ Deploy Spring Boot & FastAPI backend to a cloud service.
✅ Set up PostgreSQL & MinIO in the cloud.
✅ Deploy the React frontend to Vercel/Netlify.
✅ Implement CI/CD pipelines for automated testing & deployment.

💡 Why?
Deployment ensures your app is live and accessible to users.

6️⃣ Phase 6: Testing & Optimization 🛠️
🔹 Ensure the system runs smoothly, is scalable, and performs well.

Tasks:
✅ Implement unit & integration tests for APIs.
✅ Optimize database queries for performance.
✅ Implement API rate limiting & security best practices.
✅ Set up monitoring (Grafana, Prometheus, ELK Stack).

💡 Why?
Testing ensures reliability, security, and scalability.
