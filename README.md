# Object-Detection

## Dataset Hazırlama
'dataset_csv.py' kullanmadan önce https://drive.google.com/file/d/1iDoZSM1I0CMY1Fms4iBzwRmAoz9Qz4IF/view bu dataseti indirip tek klasör içinde bulunan .jpg (images) ve .txt (labels) uzantılı dosyaları iki ayrı klasör olacak şekilde ayırın bu ayırma işlemini direkt klasörler üzerinden yapabilirsiniz, koda gerek yok.Sonrasında ise images, labels klasörlerini dataset_csv.py ile aynı klasör içine atınız, bu klasörü ise Custom_Dataset olarak isimlendiriniz. Ardından dataset_csv.py çalıştırın.

## Eğitim vs Prediction
Eğitim için config.py dosyasında SAVE_MODEL flagını True, LOAD_MODEL flagını ise False yapınız. Prediction için ise eğitimi bitirdikten sonra elinizde kullanıma hazır bir model olduğuna emin olduktan sonra LOAD_MODEL flagını True, SAVE_MODEL flagını ise False yapınız. 