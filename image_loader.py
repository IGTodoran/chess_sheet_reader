from PIL import Image
from PIL import ExifTags
from PIL import ImageOps


class ImageLoader:
    def __init__(self, img_path):
        """
        Class that allows extracting useful information from a segmented image.
        :param img_path: Path of the original image
        :param preprocess: If True, the segmented image will be processed before usage
        """
        self.img_path = img_path
        self.img = Image.open(self.img_path)
        self.exif = dict((ExifTags.TAGS[k], v) for k, v in self.img._getexif().items() if k in ExifTags.TAGS)
        self.img = ImageOps.exif_transpose(self.img)
