import fitz  # PyMuPDF
from PIL import Image
import io

def extract_image_info(pdf_path):
    doc = fitz.open(pdf_path)
    images_info = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        image_list = page.get_images(full=True)
        
        for image_index, img in enumerate(page.get_images(full=True)):
            # 画像の基本情報を取得
            base_image_info = doc.extract_image(img[0])
            image_bytes = base_image_info["image"]
            image_ext = base_image_info["ext"]
            image = Image.open(io.BytesIO(image_bytes))
            
            # 画像の詳細情報を取得
            dpi = image.info.get('dpi', (72, 72))  # PillowではデフォルトDPIは通常72とされる
            width, height = image.size
            compression_rate = len(image_bytes) / (width * height)
            
            images_info.append({
                'page': page_num + 1,
                'image_index': image_index + 1,
                'width': width,
                'height': height,
                'dpi': dpi,
                'extension': image_ext,
                'compression_rate': compression_rate,
            })
            
    doc.close()
    return images_info

# PDFファイルのパスを指定
pdf_path = r'O:\OneDrive - nagaokaut.ac.jp\01_Research\05_Papers\10_202310_JSCE_Factsheet\202310_JSCE_Factsheet_Turkey_Geotech_v0.93.pdf'
images_info = extract_image_info(pdf_path)

for info in images_info:
    print(info)
