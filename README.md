# Snow Cover Analysis (SCA) Mapping

This project aims to use advanced machine learning techniques to predict and analyze snow cover using satellite images. Whether you're a researcher, a nature enthusiast, or simply curious about how technology can help us understand our environment, this project provides a fascinating insight into snow cover analysis.

## Project Overview

### What is Snow Cover Analysis?

Snow cover analysis involves studying the extent and distribution of snow on the ground. This information is crucial for understanding climate patterns, managing water resources, and assessing environmental changes. Satellite images provide a powerful tool for observing snow cover over large areas.

### Project Goals

1. **Predict Snow Cover**: Use satellite images to predict areas covered by snow.
2. **Evaluate Model Performance**: Assess the accuracy and reliability of the predictions.
3. **Visualize Snow Cover**: Create visual representations of snow cover for easy understanding and analysis.

## How It Works

### Step 1: Data Preparation

We start by gathering and preparing the necessary data. This involves:

- **Collecting Satellite Images**: High-resolution images from Planet satellites.
- **Preprocessing**: Cleaning and formatting the data for analysis.

### Step 2: Model Training

Using advanced machine learning techniques, we train a model to predict snow cover. The model learns to recognize patterns in the satellite images that indicate the presence of snow.

### Step 3: Snow Cover Prediction

Once the model is trained, it can predict snow cover on new satellite images. This helps in real-time monitoring of snow-covered areas.

### Step 4: Model Evaluation

To ensure our predictions are accurate, we evaluate the model using various metrics. This step is crucial for understanding the reliability of our predictions and making necessary improvements.

### Step 5: Visualization

Finally, we create visual representations of the snow cover predictions. These visuals make it easy to see the distribution and extent of snow-covered areas.

## Key Features

- **Automated Snow Cover Detection**: Efficient and accurate detection of snow cover using machine learning.
- **High-Resolution Satellite Imagery**: Utilizes detailed images for precise analysis.
- **Model Evaluation**: Comprehensive evaluation to ensure high accuracy.
- **Visualization Tools**: Easy-to-understand visuals for quick insights.

## How You Can Benefit

- **Researchers**: Gain insights into snow cover patterns and their environmental impacts.
- **Policy Makers**: Make informed decisions about water resource management and climate action.
- **Nature Enthusiasts**: Understand and visualize snow cover in various regions.

## ML-based High Resolution Snow Cover Mapping

Geoweaver workflow for high resolution snow cover area mapping task. The input data includes satellite imagery from Planet Cubesat.

For more details, please refer to the [Geo-SMART Jupyter Book](https://geo-smart.github.io/scm_geosmart_use_case/chapters/one.html).

## Getting Started: Using the Workflow
## Using the Workflow

This section provides detailed instructions on how to use the workflow for the Snow Cover Analysis project. Follow these steps to set up and execute the workflow using Geoweaver.

### Step-by-Step Instructions

1. **Download the Source Code**
    - Visit the release page of the `geo-smart/snow_cover_mapping` repository: [Geo-SMART SCA Mapping Releases](https://github.com/geo-smart/sca_mapping_geoweaver/releases).
    - Select the latest release available and download the zip file of the source code. For example, if the latest release is `0.0.4`, download `sca_mapping_geoweaver-0.0.4.zip`.

2. **Import the Workflow into Geoweaver**
    - Open Geoweaver running on your local machine. [video guidance](https://youtu.be/jUd1dzi18EQ)  
    - Click on "Weaver" in the top navigation bar. 
    - A workspace to add a workflow opens up. Select the "Import" icon in the top navigation bar.
    - Choose the downloaded zip file, for example, `sca_mapping_geoweaver-0.0.4.zip`.
    - Click on "Start" to upload the file. If the file is valid, a prompt will ask for your permission to upload. Click "OK".
    - Once the file is uploaded, Geoweaver will create a new workflow named `snow_cover_mapping`.

3. **Execute the Workflow**
    - Click on the execute icon in the top navigation bar to start the workflow execution process. [video guidance](https://youtu.be/PJcMNR00QoE) 
    - A wizard will open where you need to select the host [video guidance](https://youtu.be/KYiEHI0rn_o) and environment [video guidance](https://www.youtube.com/watch?v=H66AVoBBaHs). 
    - Click on "Execute" icon to initiate the workflow. Enter the required password when prompted and click "Confirm" to start executing the workflow. 
4. **Monitor Execution and View Results**
    - The workflow execution will begin.
    - **Note**: Green indicates the process is successful, Yellow indicates the process is running and Red indicates the process has failed.
    - Once the execution is complete, the results will be available immediately.

By following these steps, you will be able to set up and execute the snow cover mapping workflow using Geoweaver.


## Workflow Graph

![Workflow Graph](https://github.com/geo-smart/sca_mapping_geoweaver/blob/main/image.png)
