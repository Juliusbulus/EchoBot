import os
import sys
import time

from utils.utils import update_current_scene

# --- Add the parent directory to the Python path ---
# This allows us to import from the 'utils' directory that is one level up
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


def main():
    """
    Example of how to use the update_current_scene function.
    """
    print("--- Scene Changer Example ---")

    # --- Path to your schedule file ---
    # The script is in 'main/src', so schedule.json is two levels up.
    schedule_file_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "schedule.json")
    )
    print(f"Targeting schedule file: {schedule_file_path}")

    # --- Example 1: Change scene to 'greeting' ---
    print("\nAttempting to change scene to 'greeting'...")
    success = update_current_scene("greeting", schedule_path=schedule_file_path)
    if success:
        print("✓ Scene change to 'greeting' was successful.")
        print("  Your 'run_stream.py' should now be playing the greeting scene.")
    else:
        print("✗ Scene change to 'greeting' failed. Check the error messages above.")

    # Wait for a bit before changing to the next scene
    print("\nWaiting for 10 seconds before the next change...")
    time.sleep(10)

    # --- Example 2: Change scene to 'dj_visual_only' ---
    print("\nAttempting to change scene to 'dj_visual_only'...")
    success = update_current_scene("dj_visual_only", schedule_path=schedule_file_path)
    if success:
        print("✓ Scene change to 'dj_visual_only' was successful.")
        print("  Background music should now be at normal volume.")
    else:
        print("✗ Scene change to 'dj_visual_only' failed.")

    # --- Example 3: Try to change to a scene that doesn't exist ---
    print("\nAttempting to change to a non-existent scene...")
    success = update_current_scene(
        "invalid_scene_name", schedule_path=schedule_file_path
    )
    if not success:
        print(
            "\n✓ As expected, the function handled the invalid scene name gracefully."
        )

    # --- Example 4: Change scene and OVERRIDE the audio path ---
    print("\nWaiting for 10 seconds before the next change...")
    time.sleep(10)

    # Let's assume you have a newly generated audio file you want to use with
    # the 'talking' scene
    new_audio_file = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "cartesia_audio",
            "generated_audio",
            "audio_20250717_101941.wav",
        )
    )

    print("\nAttempting to switch to 'talking' scene with a new audio file...")
    print(f"  New audio: {os.path.basename(new_audio_file)}")

    success = update_current_scene(
        "talking",
        schedule_path=schedule_file_path,
        audio_path=new_audio_file,  # <-- This is the new optional argument
    )

    if success:
        print("✓ Scene 'talking' is now active with the new custom audio.")
    else:
        print("✗ Failed to switch scene with custom audio.")


if __name__ == "__main__":
    main()
