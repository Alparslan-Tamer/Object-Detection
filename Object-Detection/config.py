import albumentations as A
import cv2
import torch

from albumentations.pytorch import ToTensorV2

DATASET = 'Custom_Dataset'
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
NUM_WORKERS = 4
NUM_CLASSES = 19

# Degiştirebileceğiniz parametreler
# -----------------------------
NUM_EPOCHS = 100
BATCH_SIZE = 4
IMAGE_SIZE = 608
LEARNING_RATE = 3e-4
WEIGHT_DECAY = 0
CONF_THRESHOLD = 0.4
MAP_IOU_THRESH = 0.5
NMS_IOU_THRESH = 0.45
# ----------------------------

S = [IMAGE_SIZE // 32, IMAGE_SIZE // 16, IMAGE_SIZE // 8]
PIN_MEMORY = True
LOAD_MODEL = False # prediction yapacaksanız bunu True yapın (Eğer modeliniz var ise)
SAVE_MODEL = True # eğitim yapacaksanız bunu True yapın
CHECKPOINT_FILE = "checkpoint.pth.tar"
IMG_DIR = DATASET + "/images/"
LABEL_DIR = DATASET + "/labels/"

ANCHORS = [
    [(0.28, 0.22), (0.38, 0.48), (0.9, 0.78)],
    [(0.07, 0.15), (0.15, 0.11), (0.14, 0.29)],
    [(0.02, 0.03), (0.04, 0.07), (0.08, 0.06)],
]  # Note these have been rescaled to be between [0, 1]


scale = 1.1
train_transforms = A.Compose(
    [
        A.LongestMaxSize(max_size=int(IMAGE_SIZE * scale)),
        A.PadIfNeeded(
            min_height=int(IMAGE_SIZE * scale),
            min_width=int(IMAGE_SIZE * scale),
            border_mode=cv2.BORDER_CONSTANT,
        ),
        A.RandomCrop(width=IMAGE_SIZE, height=IMAGE_SIZE),
        A.ColorJitter(brightness=0.3, contrast=0.3, saturation=0.3, hue=0.3, p=0.2),
        A.Blur(p=0.1),
        A.CLAHE(p=0.1),
        A.Posterize(p=0.1),
        A.ToGray(p=0.1),
        A.ChannelShuffle(p=0.05),
        A.Normalize(mean=[0, 0, 0], std=[1, 1, 1], max_pixel_value=255,),
        ToTensorV2(),
    ],
    bbox_params=A.BboxParams(format="yolo", min_visibility=0.4, label_fields=[],),
)
test_transforms = A.Compose(
    [
        A.LongestMaxSize(max_size=IMAGE_SIZE),
        A.PadIfNeeded(
            min_height=IMAGE_SIZE, min_width=IMAGE_SIZE, border_mode=cv2.BORDER_CONSTANT
        ),
        A.Normalize(mean=[0, 0, 0], std=[1, 1, 1], max_pixel_value=255,),
        ToTensorV2(),
    ],
    bbox_params=A.BboxParams(format="yolo", min_visibility=0.4, label_fields=[]),
)

pred_transforms = A.Compose(
    [
        A.LongestMaxSize(max_size=IMAGE_SIZE),
        A.PadIfNeeded(
            min_height=IMAGE_SIZE, min_width=IMAGE_SIZE, border_mode=cv2.BORDER_CONSTANT
        ),
        A.Normalize(mean=[0, 0, 0], std=[1, 1, 1], max_pixel_value=255,),
        ToTensorV2(),
    ]
)

CUSTOM_CLASSES = [
    "Kirmizi_Isik",
    "Sari_Isik",
    "Yesil_Isik",
    "Park_Yapilabilir",
    "Durak_Isareti",
    "Saga_Donulemez",
    "Sola_Donulemez",
    "Ileri_ve_Sola_Donus",
    "Sola_Mecburi_Donus",
    "Saga_Mecburi_Donus",
    "Girilemez",
    "Dur",
    "Azami_Hiz_20",
    "Hiz_Sinirlamasi_Sonu_20",
    "Azami_Hiz_30",
    "Hiz_Sinirlamasi_Sonu_30",
    "Azami_Hiz_50",
    "Hiz_Sinirlamasi_Sonu_50",
    "Ileri_ve_Saga_Donus",
]

