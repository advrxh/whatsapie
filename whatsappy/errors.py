from requests import Response
import json


class ErrorResponse(BaseException):
    def __init__(self, response: Response) -> None:
        error = response.json()["error"]["message"]
        status_code = response.status_code
        message = f"[{status_code}] {error}"
        super().__init__(message)


class ErrorMediaResponse(ErrorResponse):
    pass


class UnsupportedMediaType(BaseException):
    def __init__(self, media: str, extension: str) -> None:
        message = f"{extension} is not a supported {media} type"
        super().__init__(message)


class MaximumMediaSizeExceeded(BaseException):
    def __init__(self, media: str, file_path: str) -> None:
        message = f"{file_path} exceeded maximum file size limit for {media} media"
        super().__init__(message)
