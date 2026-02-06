"""
!!! IMPORTANT !!!
Please put your client_secret.json in the same directory as this script!


Token Generator for Headless Deployment
This script generates OAuth tokens that can be used in headless environments like k8s.
"""

import json
from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def generate_token():
    """Generate OAuth token using browser authentication."""
    # Check if client_secret.json exists
    client_secret_file = Path("client_secret.json")
    if not client_secret_file.exists():
        print("❌ Error: client_secret.json not found!")
        print(
            "📥 Download it from Google Cloud Console and place it in this directory."
        )
        return

    print("🚀 Starting OAuth flow...")
    print("📋 A browser window will open for you to authorize the application.")

    # Run OAuth flow
    flow = InstalledAppFlow.from_client_secrets_file(str(client_secret_file), SCOPES)

    creds = flow.run_local_server(port=8080, access_type="offline", prompt="consent")

    # Save token.json
    token_file = Path("token.json")
    with open(token_file, "w") as f:
        f.write(creds.to_json())

    # Parse and display environment variables
    token_data = json.loads(creds.to_json())

    print("\n✅ Success! Token generated.")
    print(f"📁 Saved to: {token_file.absolute()}")

    print("\n🔧 Environment variables for your k8s deployment:")
    print("=" * 60)
    print(f"OAUTH_CLIENT_ID={token_data['client_id']}")
    print(f"OAUTH_CLIENT_SECRET={token_data['client_secret']}")
    print(f"OAUTH_REFRESH_TOKEN={token_data['refresh_token']}")
    print("=" * 60)

    print("\n📝 Copy these values to your .env file or k8s secrets.")
    print("🚀 Your app can now run headless without browser interaction!")


if __name__ == "__main__":
    generate_token()
