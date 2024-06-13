import os
from huggingface_hub import hf_hub_download
from config import MODEL_SIZE, YOLO_SIZE, DATASET, EXT, EXT_YOLO

MODEL_TYPE = "torch"
YOLO_TYPE = "torch"
REPO_ID = 'JunkyByte/easy_ViTPose'
FILENAME = os.path.join(MODEL_TYPE, f'{DATASET}/vitpose-' + MODEL_SIZE + f'-{DATASET}') + EXT
FILENAME_YOLO = 'yolov8/yolov8' + YOLO_SIZE + EXT_YOLO

print(f'Downloading model {REPO_ID}/{FILENAME}')
model_path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
yolo_path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME_YOLO)
