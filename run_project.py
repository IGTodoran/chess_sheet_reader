from matplotlib import pyplot as plt
from image_loader import ImageLoader

if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--sheet_path", type=str, help="Path to the chess sheet",
                        default="./chess_sheets/chess_sheet_1.jpg", required=False)

    args = parser.parse_args()

    img_path = args.sheet_path
    img = ImageLoader(img_path)
    plt.imshow(img.img)
    plt.show()
