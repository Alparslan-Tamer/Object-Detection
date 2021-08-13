"""
Prediction fonksiyonu
"""

import utils
import config
import torch.optim as optim
import torch
from PIL import Image
import numpy as np
import cv2

def prediction(x, model):
    scaled_anchors = (
            torch.tensor(config.ANCHORS)
            * torch.tensor(config.S).unsqueeze(1).unsqueeze(1).repeat(1, 3, 2)
    ).to(config.DEVICE)

    x = x.unsqueeze(0)
    x = x.to("cuda" if config.DEVICE == "cuda" else "cpu")

    with torch.no_grad():
        out = model(x)
        bboxes = [[] for _ in range(x.shape[0])]
        for i in range(3):
            batch_size, A, S, _, _ = out[i].shape
            anchor = scaled_anchors[i]
            boxes_scale_i = utils.cells_to_bboxes(
                out[i], anchor, S=S, is_preds=True
            )
            for idx, (box) in enumerate(boxes_scale_i):
                bboxes[idx] += box

    for i in range(batch_size):
        nms_boxes = utils.non_max_suppression(
            bboxes[i], iou_threshold=0.4, threshold=0.8, box_format="midpoint", # iyi bir tespit için bunun ayarlanması gerekiyor. iou_threshold ve threshold
        )

        utils.plot_w_cv2(x[i].permute(1, 2, 0).detach().cpu(), nms_boxes) # Görselleştirme amaçlı, görselleştirme istemiyorsan bunu kapat.
        print(nms_boxes)
        classes = [box[0] for box in nms_boxes]
    return classes


if __name__ == "__main__":
    model = utils.model_load() # modelimizi import ediyoruz.
    image_file = "data3_586.jpg"
    image = np.array(Image.open(image_file).convert("RGB"))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    transform = config.pred_transforms(image=image)
    image = transform["image"]
    class_pred = prediction(image, model) # sahnede tespit ettiği nesnelerin değerlerini dönüyor.

    while True:
        if cv2.waitKey(1) == 27: # esc basarsanız görsel kapanır.
            break

    print(class_pred)
