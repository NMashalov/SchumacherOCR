import vtracer
import io
from PIL.Image import Image
import base64 
import tempfile 
import typing as tp

class ImgProcessor:

    @classmethod
    def img_stream_to_base64_stream(cls,image_stream :tp.Iterable ):
        for img in image_stream:  
            yield cls.to_base64()
    @staticmethod
    def to_base64(image: Image) :
        image.save(buffered:= io.BytesIO(), format="PNG")
        return base64.b64encode(buffered.getvalue())

    @staticmethod
    def png_to_svg(image: Image):
        with tempfile.NamedTemporaryFile() as f:
            vtracer.convert_image_to_svg_py()