from ..exceptions import OCRError
from ..classes import OCRBackendBase
from django.utils.translation import ugettext_lazy as _
import logging
from paddleocr import PaddleOCR

logger = logging.getLogger(name=__name__)


class PaddleOCRBackend(OCRBackendBase):
    def _execute(self, image_file_object):
        img_cpy = image_file_object
        try:
            img_cpy.seek(0)
            image_data = img_cpy.read()
        except Exception as exception:
            error_message_list = []
            error_message_list.append(
                'Exception opening image file object: {}; {}'.format(
                    img_cpy, exception
                )
            )
            error_message = '/n'.join(error_message_list)
            logger.error(error_message, exc_info=True)
            raise OCRError(error_message)

        try:
            ocr = PaddleOCR(use_angle_cls=True, lang="ar")
            result = ocr.ocr(image_data, cls=True)
        except Exception as exception:
            error_message_list = []
            error_message_list.append(
                'Exception calling PaddleOCR with language option: {}; {}'.format(
                    "arabic", exception
                )
            )
            error_message = '/n'.join(error_message_list)
            logger.error(error_message, exc_info=True)
            raise OCRError(error_message)

        concat_output = ""
        for pg in range(len(result)):
            concat_output = "\n".join(row[1][0] for row in result[pg])
        text = concat_output
        return text
