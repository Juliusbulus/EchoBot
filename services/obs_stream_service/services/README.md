# Services

This directory contains various services used in the EchoBot application. Each service is responsible for a specific set of functionalities.

## `bgm_service.py`

The `BGMService` manages the background music for the radio stream. It is responsible for:

- Initializing the background music from a schedule.
- Ducking the background music when a scene with its own audio is playing.
- Restoring the background music to its normal volume when the scene is over.
- Initializing voice audio for scenes that have it.

## `chat_service.py`

The `ChatService` handles the interaction with the YouTube live chat. Its main responsibilities are:

- Fetching relevant chat messages from the live stream.
- Generating responses to chat messages using an LLM.
- Posting responses to the chat.
- Storing a history of answered messages to avoid duplicates.

## `log_pusher.py`

The `log_pusher` service is a simple utility for pushing log messages to a central server. It sends log messages to a specified URL in a separate thread.

## `obs_service.py`

The `OBSService` is a wrapper around the `obs-websocket-py` client. It provides a high-level interface for controlling OBS (Open Broadcaster Software). Its main functionalities are:

- Connecting to OBS and ensuring that the connection is active.
- Setting the stream key for the live stream.
- Playing scenes with or without audio.
- Switching between scenes with smooth transitions.
- Starting and stopping the stream.

## `schedule_service.py`

The `ScheduleService` is responsible for loading and saving the `schedule.json` file. This file contains the configuration for the radio stream, including the scenes, background music, and other settings. The service also provides a method for switching scenes by updating the `schedule.json` file.

## `subscene_cycler.py`

The `SubsceneCyclerService` is responsible for cycling through a list of subscenes in the background. This is useful for creating dynamic scenes with multiple video sources. The service can be started and stopped, and it can be configured to use different transitions between subscenes.
