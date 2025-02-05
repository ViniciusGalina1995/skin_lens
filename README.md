# Skin Disease Detection and Classification

This project aims to develop a skin scanner tool that can classify skin conditions into one of nine diseases using Convolutional Neural Networks (CNNs) and state-of-the-art Transfer Learning Models. The application will provide a user-friendly interface, enabling easy access to accurate skin condition classification.

## Dataset

The dataset used for this project is sourced from Kaggle and can be accessed [here](https://www.kaggle.com/datasets/pritpal2873/multiple-skin-disease-detection-and-classification). It contains images categorized into the following nine classes:

1. Actinic Keratosis (500 files)
2. Basal Cell Carcinoma (500 files)
3. Dermatofibroma (400 files)
4. Melanoma (505 files)
5. Nevus (500 files)
6. Pigmented Benign Keratosis (500 files)
7. Seborrheic Keratosis (500 files)
8. Squamous Cell Carcinoma (414 files)
9. Vascular Lesion (290 files)

## Project Workflow

### 1. Data Preparation

- **Loading Data**: The dataset will be loaded and organized into a structured format.
- **Splitting Data**: The dataset will be split into three folders:
  - **Train**: For training the model.
  - **Validation**: For evaluating the model during training.
  - **Test**: For final performance evaluation.

### 2. Data Preprocessing and Augmentation

- **Preprocessing**: Steps include resizing images, normalizing pixel values, and encoding labels.
- **Augmentation**: Techniques such as rotation, flipping, zooming, and brightness adjustment will be applied to double the size of the training set.

### 3. Modeling

- **Convolutional Neural Networks**: A CNN SOTA will be implemented as the core model.
- **Transfer Learning**: Pre-trained models such as ResNet, ConvNeXtLarge will be fine-tuned for this classification task.
- **Iteration**: Multiple experiments will be conducted to optimize hyperparameters, architecture, and preprocessing steps to achieve the best performance.

### 4. API Development

- **Creating the API**: An API will be developed to allow online skin condition classification. Users can upload an image, and the API will return the predicted class along with confidence scores.

### 5. Dockerization

- **Containerization**: The application, including the model and API, will be containerized using Docker to ensure consistent performance and easy deployment on the cloud.

### 6. Front-End Development

- **User Interface**: A basic web interface will be created for end-users. This interface will allow:
  - Uploading skin images.
  - Displaying the classification results in a clear and user-friendly manner.

## Deployment

The final application will be deployed on a cloud platform, ensuring accessibility and scalability. Docker containers will be used for seamless deployment.

Link of the web application: https://skinlensweb-35zsxjyv5xmpcefkqtzgu5.streamlit.app/

## Reproducibility

**After cloning the repo the model file has to be downloaded and pasted on the models folder!**
[Link for the model](https://drive.google.com/file/d/1fo6d-z-mXrReLqQfjX5P7Q3UmCl44Tup/view?usp=sharing)

## Future Improvements

- Incorporating additional datasets for broader disease coverage.
- Enhancing model performance through advanced techniques like ensemble learning.
- Improving the front-end with interactive features and better design.

## Contributors

Angelo Malacarne
Bhagyalakshmi Ushakumari
Diego Siguelnitzky
Vinicius Lacorte Galina

## License

[MIT]

---

This README provides an overview of the project structure and objectives. Detailed implementation steps will be documented within the codebase and supporting files.
