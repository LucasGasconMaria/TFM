# Development of a Web App for Skin Alteration Classification Using Machine Learning

## Overview

This repository contains the code and docs for my Master's Thesis (TFM) focused on machine learning for classifying skin alteration images. The project aims to develop and deploy a robust classification model capable of identifying various skin conditions from images using a web-app.

## Key Features

- **Machine Learning Models:** Implementation of state-of-the-art machine learning CNN, DenseNet121 and ResNet50 models for image classification.
- **Dataset:** Details about the dataset used, preprocessing steps, and data augmentation techniques applied.
- **Training and Evaluation:** Code for training the models, evaluating their performance, and fine-tuning.
- **Deployment:** Details about the deployment of the trained model for real-world applications, including web-app.
- **Documentation:** In-depth documentation covering the project's architecture, methodologies, and findings.

## Repository Structure

- **`/code`:** Contains all the code files, including Python scripts.
- **`/docs`:** Detailed project documentation, including research papers, thesis, or any relevant reports.
- **`/results`:** Stores model evaluation metrics, visualizations, and any other relevant output.
- **`/web`:** Contains all the code files and assets regarding the webtool.

## Web App

[WebTool](https://skinai.bioedu.one/)

## Deployment

To deploy via Docker, clone this repository and execute the following command on the server terminal:

```
git clone git@github.com:HummusDeArialux/TFM.git
sudo docker build -t skinai .
sudo docker run -p 8000:8000 skinai
```

After deploying, navigate to http://127.0.0.1:8000

## Documentation

For detailed information about the project, including methodologies, findings, and the web app architecture, please refer to the `/docs` directory.

## Dataset

BCN20000, avaiable at: https://api.isic-archive.com/collections/249/

- Imagenes_256 can be obtain by resizing images to 256x256.
- Imagenes_256_reduced can be obtain by executing the code in reducing_dataset.py.
- Imagenes_test can be obtain by executing the code in create_test_images.py.

## Models

Models can't be uploaded due to size, but can be obtained by executing the following code: CNN.py, DenseNet.py and ResNet.py.

Fully trained DenseNet121 model can be found within web/tensored-django folder.

## Acknowledgments

Special thanks to:

- **Romina, My Exceptional Tutor:** I want to express my heartfelt gratitude to Romina for her unwavering support and invaluable guidance throughout this project. Her expertise and encouragement played a crucial role in shaping the success of this work.
