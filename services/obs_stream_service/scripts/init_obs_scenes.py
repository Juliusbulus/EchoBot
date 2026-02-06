import logging
import os

# Explicitly load .env from the project root before any other imports
try:
    from dotenv import load_dotenv

    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    dotenv_path = os.path.join(project_root, ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path=dotenv_path)
        # Using print here for immediate feedback before logging is configured
        print(f"INFO: Successfully loaded .env file from {dotenv_path}")
    else:
        print(f"WARNING: .env file not found at {dotenv_path}")
except ImportError:
    print("WARNING: python-dotenv not installed, .env file will not be loaded.")


from radio.obs import (
    create_or_update_audio_source,
    create_or_update_video_source_centered,
    create_scene,
    scene_exists,
    start_background_music,
)
from radio.services.schedule_service import ScheduleService


def setup_obs_environment():
    """
    Automatically creates all scenes and default sources in OBS so that the
    live setup exactly matches the schedule.json file.
    """
    logging.info("=== OBS auto‑setup started ===")
    schedule_service = ScheduleService()
    schedule = schedule_service.load()
    if not schedule:
        logging.error("Could not load schedule.json. Aborting setup.")
        return

    available_scenes = schedule.get("_available_scenes", {})
    bg_music_config = schedule.get("background_music", {})

    all_scene_names = [
        scene["scene_name"]
        for scene in available_scenes.values()
        if isinstance(scene, dict)
    ]
    if bg_music_config.get("enabled"):
        all_scene_names.append("Background-Music")

    for scene_name in set(all_scene_names):
        if not scene_exists(scene_name):
            create_scene(scene_name)

    for scene_name, scene_data in available_scenes.items():
        if scene_name.startswith("_"):
            continue

        if scene_data.get("video_path") and os.path.exists(scene_data["video_path"]):
            create_or_update_video_source_centered(
                scene_name=scene_data["scene_name"],
                source_name=scene_data["video_source_name"],
                file_path=scene_data["video_path"],
                loop_video=scene_data["loop_video"],
            )

        if scene_data.get("audio_path") and os.path.exists(scene_data["audio_path"]):
            create_or_update_audio_source(
                scene_name=scene_data["scene_name"],
                source_name=scene_data["audio_source_name"],
                file_path=scene_data["audio_path"],
            )

    if bg_music_config.get("enabled"):
        bg_music_path = bg_music_config.get("file_path")
        if bg_music_path and os.path.exists(bg_music_path):
            logging.info(f"Setting up background music with: {bg_music_path}")
            start_background_music(
                music_file_path=bg_music_path,
                has_initial_audio=False,
                normal_volume=bg_music_config.get("volume_normal", 0.3),
                ducked_volume=bg_music_config.get("volume_ducked", 0.1),
            )
        else:
            logging.warning(
                f"Background music is enabled, but file not found: {bg_music_path}"
            )

    logging.info("✓ OBS auto‑setup finished")


if __name__ == "__main__":
    setup_obs_environment()
