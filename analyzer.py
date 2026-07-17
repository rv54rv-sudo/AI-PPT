from PIL import Image


def analyze(image_path):

    img = Image.open(image_path)

    print("=" * 40)
    print("AI 海報分析")
    print("=" * 40)

    print("圖片大小：", img.size)
    print("圖片模式：", img.mode)

    print("\n分析完成")