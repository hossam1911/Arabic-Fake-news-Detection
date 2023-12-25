from transformers import pipeline
def test(x):
    pipe = pipeline("text-classification", model=r"E:\My Data\Graduation project work\.ipynb_checkpoints\Arabert_model", device=0, return_all_scores=True)
    score= pipe(x)
    return score
