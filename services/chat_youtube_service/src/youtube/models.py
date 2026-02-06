from typing import Any

from pydantic import BaseModel, Field


class PageInfo(BaseModel):
    totalResults: int = Field(..., alias="totalResults")
    resultsPerPage: int = Field(..., alias="resultsPerPage")


class VideoListResponse(BaseModel):
    kind: str
    etag: str
    items: list[dict[str, Any]]
    pageInfo: PageInfo


class Localized(BaseModel):
    title: str
    description: str


class Snippet(BaseModel):
    publishedAt: str
    channelId: str
    title: str
    description: str
    thumbnails: dict[str, Any]
    channelTitle: str
    categoryId: str
    liveBroadcastContent: str
    localized: Localized


class LiveStreamingDetails(BaseModel):
    actualStartTime: str | None = None
    concurrentViewers: str | None = None
    activeLiveChatId: str | None = None


class Video(BaseModel):
    kind: str
    etag: str
    id: str
    snippet: Snippet
    liveStreamingDetails: LiveStreamingDetails | None = None


class AuthorDetails(BaseModel):
    channelId: str
    channelUrl: str
    displayName: str
    profileImageUrl: str
    isVerified: bool
    isChatOwner: bool
    isChatSponsor: bool
    isChatModerator: bool


class LiveChatMessageSnippet(BaseModel):
    type: str
    liveChatId: str
    authorChannelId: str
    publishedAt: str
    hasDisplayContent: bool
    displayMessage: str
    textMessageDetails: dict[str, Any] | None = None


class LiveChatMessage(BaseModel):
    kind: str
    etag: str
    id: str
    snippet: LiveChatMessageSnippet
    authorDetails: AuthorDetails


class LiveChatMessageListResponse(BaseModel):
    kind: str
    etag: str
    pollingIntervalMillis: int
    pageInfo: PageInfo
    nextPageToken: str | None = None
    items: list[LiveChatMessage]  # Actual comments
