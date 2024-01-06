# Overview
AraNews is a comprehensive Arabic news dataset created to investigate misinformation and disinformation in Arabic news articles. The dataset includes diverse news sources from 15 Arab countries, the United States, and the United Kingdom, offering a broad perspective on the linguistic landscape.

### Project Description

This project centers on Arabic fake news detection, leveraging cutting-edge techniques such as Arabert pre-trained models from Hugging Face. The implementation also features the deployment of the model using Flask, complete with a user-friendly interface.

### Dataset Statistics

- Number of Newspapers: 50
- Countries Covered: 15 Arab countries, USA, UK
- Total News Articles: 5,187,957
Data Collection
The dataset was meticulously compiled by manually selecting 50 newspapers and subsequently scraping news articles from these sources.


### Code Structure

- `preprocessing.ipynb`: Houses the latest Arabic preprocessing techniques.
- `model_training.ipynb`: Code for training the fake news detection model.
- `Fakely website`: Flask application for model deployment.
## Results

The trained model achieved notable results:

- Training Loss (Epoch 2): 0.203500
- Validation Loss (Epoch 2): 0.228960
- Macro F1 (Epoch 2): 0.908546
- Accuracy (Epoch 2): 0.908658
### Model Save

The final model is saved in the `output_dir` directory, and the tokenizer used for preprocessing is also preserved for future use.

### Web Page
![Input](Fakely%20website/screen2.png)
![Result](Fakely%20website/Screen1.png)




## Acknowledgments

Special appreciation to the authors of the AraNews dataset for providing a valuable resource for research in Arabic misinformation detection.

**Dataset Citation:**
- **Title:** Machine Generation and Detection of Arabic Manipulated and Fake News
- **Authors:** El Moatez Billah Nagoudi, AbdelRahim Elmadany, Muhammad Abdul-Mageed, Tariq Alhindi, Hasan Cavusoglu
- **Year:** 2020
- **Book Title:** Proceedings of the Fourth Arabic Natural Language Processing Workshop
- **Address:** Barcelona, Spain

# Download the dataset 
  https://github.com/UBC-NLP/wanlp2020_arabic_fake_news_detection?tab=readme-ov-file#donwload-aranews
