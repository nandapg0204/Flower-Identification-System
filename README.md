<h1>Flower identification using Transfer Learning</h1>
<p>This repository contains code and data for the Flower Identification Using Transfer Learning project, which employs deep learning techniques to classify flower species efficiently</p>
<h2> Motivation </h2>

<p>Identifying flower species is often slow and relies on expert knowledge, making it challenging for researchers and enthusiasts. This project automates flower classification using deep learning, which speeds up the process and increases accuracy</p>
<h2>Project overview :</h2>


<p> This project implements a Flower Identification System using Transfer Learning with Convolutional Neural Networks (CNNs).The goal is to classify images of flowers into their respective categories by leveraging pre-trained models, specifically the EfficientNetB7 architecture.</p>
<h2>Experimentation</h2>


<p>    In this, I explored the effectiveness of different convolutional neural network architectures for my classification task. Initially, I developed a custom-built model from scratch to establish a baseline understanding of the dataset and initial performance benchmarks.</p>
<p>    Following the custom model, I implemented the ResNet architecture, known for its deep layer structure and skip connections that facilitate training of deep networks. This allowed me to assess whether the inherent features of ResNet could improve upon the baseline performance achieved by the custom model.</p>
<p>    Subsequently, I integrated the EfficientNetB7 architecture into my experimentation. EfficientNet models are recognized for their superior performance-to-parameter ratio, making them efficient choices for various computer vision tasks. By adopting EfficientNetB7, specifically optimized for high-resolution image classifications, I aimed to achieve further enhancements in both accuracy and computational efficiency.</p>
<h2>Model architecture</h2>


![Flower](https://github.com/nandapg0204/Flower-Identification-Using-Transfer-Learning/blob/main/images/model_architecture.PNG?raw=true)
<h2> Training Approach Description</h2>


<p>This neural network training process involved two key phases: feature engineering and fine-tuning, with adaptive learning rates tailored to each phase to optimize model performance.</p>
<p><strong>Feature Engineering Phase :</strong>During this phase all layers of the pre-trained model were frozen while new feature representations were generated. This phase focused on training the added layers to adapt to the specific task using a higher learning rate.</p>
<p><strong>Fine-Tuning Phase:</strong>This phase involved selectively unfreezing some of the top layers of the model. Then the model was trained on a smaller learning rate. This approach allowed the model to refine its learned representations, particularly in areas critical to the task, without destabilizing the already learned features.</p>
<h2>Loss and Accuracy plots </h2>
![lossandaccuracy](https://github.com/nandapg0204/Flower-Identification-Using-Transfer-Learning/blob/main/images/Loss_Accuracy_Curves.PNG?raw=true)
