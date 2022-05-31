from requests import Response


class ErrorResponse(BaseException):
    """Custom Exception to create tracebacks of api response errors.

    Invoked when the response status code is not 200.

    Args:
        response: The response with status code other than 200.
    """

    def __init__(self, response: Response) -> None:
        error = response.json()["error"]["message"]
        status_code = response.status_code
        message = f"[{status_code}] {error}"
        super().__init__(message)
