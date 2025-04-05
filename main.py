from PIL import Image

# Список путей к изображениям
image_files = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg"]

# Открытие первого изображения
images = [Image.open(file) for file in image_files]

# Сохранение в PDF
images[0].save(
    "output.pdf", "PDF", resolution=100.0, save_all=True, append_images=images[1:]
)
