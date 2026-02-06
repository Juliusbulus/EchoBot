class YoutubeClientError(Exception):
    """Base exception for YouTube client errors."""


class YoutubeVideoNotFoundError(YoutubeClientError):
    """Raised when a video is not found or has no items."""


class YoutubeLiveChatNotFoundError(YoutubeClientError):
    """Raised when a live chat is not found for a video."""


class YoutubeAPIError(YoutubeClientError):
    """Raised for general YouTube API errors."""
