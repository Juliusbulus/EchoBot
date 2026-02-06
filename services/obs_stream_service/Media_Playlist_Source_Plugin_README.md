# Media Playlist Source Plugin for OBS - Installation and Usage Guide

This guide provides a comprehensive step-by-step process to download, install, and utilize the Media Playlist Source plugin for OBS Studio. This plugin offers an easy and powerful way to integrate background music playlists into your streams.

## System Requirements

*   OBS Studio 31 or higher (latest version recommended)
*   Windows, macOS, or Linux operating system
*   Administrative privileges for installation

## Step 1: Download the Plugin

Visit the [GitHub releases page](https://github.com/CodeYan01/media-playlist-source/releases/download/0.1.3/media-playlist-source-0.1.3-x86_64-linux-gnu.deb) and download the latest version (0.1.3 as of September 2025).

Choose the appropriate file for your operating system:

*   **Windows Users**
    *   **Regular Installation:** `media-playlist-source-0.1.3-windows-x64-Installer.exe` (1.82 MB)
    *   **Portable OBS:** `media-playlist-source-0.1.3-windows-x64-Portable.zip` (142 KB)
*   **macOS Users**
    *   **Universal (Intel + Apple Silicon):** `media-playlist-source-0.1.3-macos-universal.pkg` (508 KB)
*   **Linux Users**
    *   **Ubuntu/Debian:** `media-playlist-source-0.1.3-x86_64-linux-gnu.deb` (19.5 KB)

## Step 2: Install the Plugin

### Windows Installation (Recommended)

1.  **Close OBS Studio completely.** This is crucial to prevent file corruption.
2.  Download the installer: `media-playlist-source-0.1.3-windows-x64-Installer.exe`
3.  **Run the installer:**
    *   Right-click and select "Run as Administrator".
    *   If Windows displays a security warning, click "More info" then "Run anyway".
    *   Follow the installation wizard. The installer will automatically detect your OBS installation directory.

### Windows Portable Installation

If you are using a portable OBS installation:

1.  Download `media-playlist-source-0.1.3-windows-x64-Portable.zip`.
2.  Extract the ZIP file.
3.  Copy the `data` and `obs-plugins` folders to your portable OBS directory.
4.  Merge them with existing folders.

### macOS Installation

1.  Close OBS Studio.
2.  Download and run: `media-playlist-source-0.1.3-macos-universal.pkg`.
3.  Follow the installer. It will automatically install to the correct location.

### Linux Installation (Ubuntu/Debian)

```bash
# Download the .deb package
wget https://github.com/CodeYan01/media-playlist-source/releases/download/0.1.3/media-playlist-source-0.1.3-x86_64-linux-gnu.deb

# Install the package
sudo dpkg -i media-playlist-source-0.1.3-x86_64-linux-gnu.deb

# If there are dependency issues, fix them
sudo apt-get install -f
```

## Step 3: Verify Installation

1.  Open OBS Studio.
2.  **Check for the plugin:** Go to the `Sources` area and click the `+` button.
3.  Look for "Media Playlist Source" in the list. It should appear alongside other source options.

## Step 4: Set Up Your Music Playlist

### Create the Media Playlist Source

1.  **Add the source:**
    *   Click `+` in the `Sources` panel.
    *   Select "Media Playlist Source".
    *   Name it (e.g., "Background Music").
    *   Click "OK".
2.  **Configure playlist settings:**
    *   **Loop Playlist:** Enable to repeat the entire playlist.
    *   **Shuffle Playlist:** Enable to randomize playback order.
    *   **Visibility Behavior:** Choose how the playlist behaves when the source is hidden:
        *   "Stop when not visible, restart when visible" (recommended)
        *   "Pause when not visible, unpause when visible"
        *   "Always play even when not visible"

### Add Music Files

1.  Click the `+` button in the playlist area.
2.  **Choose your method:**
    *   **Add Files:** Select individual music files.
    *   **Add Directory:** Point to a folder containing music files.
    *   **Add Path or URL:** Add streaming URLs or network paths.
3.  **Organize your playlist:**
    *   Drag and drop to reorder songs.
    *   Use the up/down arrows to rearrange.
    *   Remove tracks with the `-` button.

## Step 5: Adjust Audio Settings

1.  Find your source in the `Audio Mixer` (bottom of OBS).
2.  Adjust volume using the slider.
3.  **Apply audio filters if needed:**
    *   Right-click the source in the `Audio Mixer`.
    *   Select "Filters".
    *   Add effects like Noise Gate, Compressor, or EQ.

## Key Features and Benefits

### Advanced Playlist Management

*   Edit playlists without restarting playback.
*   Shuffle support based on VLC 4's implementation.
*   Saves currently playing file for OBS restart continuity.
*   Manual file selection from playlist.
*   Automatic reshuffling when playlist ends.

### File Format Support

*   MP3, WAV, OGG, M4A, AAC, FLAC
*   Both audio and video files
*   Network streams and URLs

### Smart Playback Control

*   Hardware decoding option for better performance.
*   Speed control (though this restarts the source).
*   Close file when inactive to save resources.

## Alternative Methods

### Method 2: VLC Video Source (Built-in)

If you prefer using the built-in OBS functionality:

1.  Install VLC Media Player (same bit version as OBS - 64-bit recommended).
2.  Add `VLC Video Source` in OBS.
3.  Configure playlist in the VLC source properties.
4.  Add files or directories to create your playlist.

### Method 3: Simple Media Source (Built-in)

For basic needs:

1.  Add `Media Source`.
2.  Select a single audio file.
3.  Enable "Loop" for continuous playback.
4.  Use multiple `Media Sources` for different tracks.

## Troubleshooting Common Issues

### Plugin doesn't appear in sources:

*   Verify OBS is version 31 or higher.
*   Ensure proper installation (try reinstalling).
*   Check if OBS was running during installation (restart OBS).

### Playback doesn't continue to next track:

*   This was fixed in version 0.1.3.
*   Make sure you're using the latest version.

### Windows installation issues:

*   Run installer as Administrator.
*   Uninstall previous versions first (versions 0.1.0 and below).
*   Use the portable version if installer fails.

## Conclusion

The Media Playlist Source plugin is the most user-friendly solution for background music in OBS, offering professional playlist management without requiring Python scripting or FFmpeg knowledge.
