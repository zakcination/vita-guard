# inference.py

from easy_ViTPose.easy_ViTPose.inference import VitInference
from download_model import model_path, yolo_path
from config import MODEL_SIZE, DATASET

# Initialize the model
model = VitInference(model_path, yolo_path, MODEL_SIZE, dataset=DATASET, yolo_size=320, is_video=True)

# Add your inference code here
# e.g., model.run_inference(input_data)
