from requests import Response


class ErrorResponse(BaseException):
    def __init__(self, response: Response) -> None:
        error = response.json()["error"]["message"]
        status_code = response.status_code
        message = f"[{status_code}] {error}"
        super().__init__(message)
