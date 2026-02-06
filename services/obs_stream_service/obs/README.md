# OBS Control Functions (`radio/obs/__init__.py`)

This file contains a comprehensive set of functions for controlling OBS (Open Broadcaster Software) via the `obsws-python` library. The functions are organized by category to manage scenes, sources, audio, video, and the overall flow of a radio show-style stream.

*The following is an auto-generated summary of the functions in this module.*

## Table of Contents
- [OBS Connection & State](#obs-connection--state)
- [Scene & Source Management](#scene--source-management)
- [Source Manipulation](#source-manipulation)
- [Transitions & Scene Switching](#transitions--scene-switching)
- [Audio Control](#audio-control)
- [Video Control](#video-control)
- [Media Utilities](#media-utilities)
- [Radio Show Flow & Segments](#radio-show-flow--segments)
- [Source Visibility & Info](#source-visibility--info)
- [Setup & Initialization](#setup--initialization)
- [Streaming Control](#streaming-control)

## OBS Connection & State

Functions for checking the state of OBS, like whether scenes or sources exist.

| Function | Description |
| --- | --- |
| `source_exists(scene_name, source_name)` | Checks if a source with a given name exists. |
| `scene_exists(scene_name)` | Checks if a scene with a given name exists in OBS. |
| `get_canvas_size()` | Gets the canvas size (width, height) from OBS video settings. |

## Scene & Source Management

Functions for creating, updating, and deleting scenes and sources.

| Function | Description |
| --- | --- |
| `create_scene(scene_name)` | Creates a new scene in OBS. |
| `create_or_update_video_source(...)` | Creates or updates a video source with specified file and transform properties. |
| `create_or_update_audio_source_v2(...)` | (V2) Creates or updates an audio source with more detailed options. |
| `create_or_update_audio_source(...)` | Creates or updates an audio source with a specified file. |
| `add_global_source_to_scene(scene_name, source_name)` | Adds an existing global source to a scene. |
| `add_scene_as_source(target_scene, source_scene_name)` | Adds an existing scene as a source to another scene (nesting). |
| `delete_source_from_scene(scene_name, source_name)` | Deletes a source from a specific scene. |
| `cleanup_temporary_sources(scene_name, source_names)` | Deletes multiple temporary sources from a scene. |
| `create_global_audio_source(source_name, file_path)` | Creates a global audio source, independent of any scene. |

## Source Manipulation

Functions for controlling the properties of sources, such as their position, media file, and playback state.

| Function | Description |
| --- | --- |
| `set_source_transform(...)` | Sets the transform (position, size, scale) of a source. |
| `update_audio_source_file(source_name, file_path)` | Dynamically changes the file used by an audio media source. |
| `update_video_source_file(...)` | Dynamically changes the file used by a video media source. |
| `set_video_repeat_count(source_name, repeat_count)` | Sets the number of times a video should repeat. |
| `restart_media_source(input_name)` | Restarts a media source to play from the beginning. |
| `restart_video_source(source_name)` | (Alias for `restart_media_source`) Restarts a video source. |
| `stop_media_source(source_name)` | Stops a media source's playback. |

## Transitions & Scene Switching

Functions for managing scene transitions and switching between scenes.

| Function | Description |
| --- | --- |
| `set_scene_transition(...)` | Sets the current scene transition type and duration. |
| `switch_to_scene(scene_name)` | Switches to a specific scene immediately. |
| `switch_to_scene_smooth(...)` | Switches to a scene with a specified smooth transition. |

## Audio Control

Functions specifically for managing audio, including volume, fading, and background music.

| Function | Description |
| --- | --- |
| `fade_audio_source(...)` | Fades an audio source in or out by controlling its volume. |
| `set_bgm_volume(volume)` | Sets the background music volume directly. |
| `smooth_duck_background_music(...)` | Smoothly lowers (ducks) the background music volume. |
| `smooth_restore_background_music(...)` | Smoothly restores the background music volume to normal. |
| `init_background_music(music_file_path, ...)` | Initializes the background music in its own scene. |
| `init_voice_audio(music_file_path, ...)` | Initializes the voice audio source. |
| `start_background_music(...)` | Initializes the background music system using scene nesting for global availability. |

## Video Control

Functions for controlling video-specific properties.

| Function | Description |
| --- | --- |
| `fade_video_source(...)` | Fades a video source in or out (simulated by changing visibility). |

## Media Utilities

Helper functions for getting information about media files, like duration, and for processing them.

| Function | Description |
| --- | --- |
| `get_audio_duration_seconds(file_path)` | Calculates the duration of an audio file in seconds. |
| `get_video_duration_seconds(file_path)` | Calculates the duration of a video file in seconds. |
| `calculate_video_audio_coefficient(...)` | Calculates how many times a video needs to loop to match an audio duration. |
| `match_video_duration_to_audio(...)` | Processes a video file (looping or trimming it) to match an audio duration. |

## Radio Show Flow & Segments

High-level functions that define the logic for different parts of the radio show.

| Function | Description |
| --- | --- |
| `run_audio_matched_video_segment(...)` | Runs a complete video segment, matching its duration to an audio file. This is a blocking function. |
| `cleanup_scene_resources(cleanup_info)` | Cleans up temporary resources from a scene after a segment is finished. |
| `run_music_segment()` | Switches to the music scene and sets up the music video. |
| `run_news_segment()` | Manages the entire news segment: generating content, updating OBS, and playing the segment. |
| `run_custom_video_segment(...)` | Runs a custom video segment with specific repeat counts and transforms. |

## Source Visibility & Info

Functions for getting information about sources within a scene and controlling their visibility.

| Function | Description |
| --- | --- |
| `list_scene_sources(scene_name)` | Lists all sources in a specific scene with their visibility status. |
| `hide_source_in_scene(scene_name, source_name)` | Hides a source in a scene. |
| `show_source_in_scene(scene_name, source_name)` | Shows a source in a scene. |
| `hide_music_banner_sources(...)` | Hides common music banner/overlay sources. |

## Setup & Initialization

Functions for setting up the OBS environment from scratch.

| Function | Description |
| --- | --- |
| `setup_obs_environment(...)` | Auto-setup helper that creates all required scenes and sources. |
| `calculate_center_position(...)` | Calculates the (x, y) coordinates to center a source on the canvas. |
| `create_or_update_video_source_centered(...)` | Creates or updates a video source and centers it. |

## Streaming Control

Functions to start and stop the OBS stream.

| Function | Description |
| --- | --- |
| `start_streaming()` | Starts the OBS stream output. |
| `stop_streaming()` | Stops the OBS stream output. |