"""Package specific constants.

Meta API Constants:
    __**META_GRAPH_API_ENDPOINT**__: A f-string value of meta graph url endpoint.
    __**META_GRAPH_API_VERSION**__: Package specific Meta Graph API version.

Request Constants:
    __**REQUEST_HEADERS**__: Common request headers for all requests made from the wrapper.

Media Constants:
    __**CAPTION_ALLOWED_MEDIA_TYPES**__: Media types in which captions are allowed.
    __**FILENAME_ALLOWED_MEDIA_TYPES**__: Media types in which custom filenames are allowed.

"""
# META API CONSTANTS
META_GRAPH_API_ENDPOINT = (
    "https://graph.facebook.com/v{version}/{phone_number_id}/messages"
)
META_GRAPH_API_VERSION = "13.0"

# REQUEST CONSTANTS
REQUEST_HEADERS = {"Content-Type": "application/json"}

# MEDIA CONSTANTS

CAPTION_ALLOWED_MEDIA_TYPES = ["document", "image"]
FILENAME_ALLOWED_MEDIA_TYPES = ["document"]
