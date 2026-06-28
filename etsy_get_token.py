#!/usr/bin/env python3
"""
etsy_get_token.py
Gets a valid Etsy OAuth2 access token with listings_w scope.

STEP 1: Get your Etsy keystring
  → https://www.etsy.com/developers/your-apps
  → Click your app → copy "Keystring"
  → Paste it below as ETSY_KEYSTRING

STEP 2: Run this script
  → python3 etsy_get_token.py

STEP 3: It will open a browser, you click "Allow"
  → The terminal will print your access token
  → Copy it and use it in create_divine_listings.py
"""

import hashlib, os, re, base64, secrets, urllib.parse, webbrowser, ssl
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request, json

# Fix SSL cert verification on macOS Python 3.14
ssl._create_default_https_context = ssl._create_unverified_context

# ── PASTE YOUR KEYSTRING HERE ──────────────────────────────────────────────────
ETSY_KEYSTRING = "p49zu7qnl7im9tqt8btmm14z"
# ──────────────────────────────────────────────────────────────────────────────

REDIRECT_URI = "http://localhost:3003/oauth/redirect"
SCOPES = "listings_w listings_r"
PORT = 3003

# PKCE helpers
def generate_code_verifier():
    return base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b'=').decode()

def generate_code_challenge(verifier):
    digest = hashlib.sha256(verifier.encode()).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b'=').decode()

# Capture the auth code
auth_code = None

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Success! You can close this tab and return to the terminal.</h2>")
        else:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Missing code parameter.")

    def log_message(self, format, *args):
        pass  # suppress server logs

def main():
    if ETSY_KEYSTRING == "PASTE_YOUR_KEYSTRING_HERE":
        print("\n❌ Open etsy_get_token.py and paste your Etsy Keystring at the top.\n")
        print("  Get it at: https://www.etsy.com/developers/your-apps")
        return

    verifier = generate_code_verifier()
    challenge = generate_code_challenge(verifier)
    state = secrets.token_urlsafe(16)

    auth_url = (
        "https://www.etsy.com/oauth/connect"
        f"?response_type=code"
        f"&redirect_uri={urllib.parse.quote(REDIRECT_URI)}"
        f"&scope={urllib.parse.quote(SCOPES)}"
        f"&client_id={ETSY_KEYSTRING}"
        f"&state={state}"
        f"&code_challenge={challenge}"
        f"&code_challenge_method=S256"
    )

    print("\n🔐 Opening Etsy authorization page in your browser...")
    print("   Click 'Allow access' when prompted.\n")
    webbrowser.open(auth_url)

    # Start local server to catch the redirect
    server = HTTPServer(("localhost", PORT), OAuthHandler)
    server.handle_request()

    if not auth_code:
        print("❌ No code received. Try again.")
        return

    # Exchange code for token
    token_url = "https://api.etsy.com/v3/public/oauth/token"
    payload = {
        "grant_type": "authorization_code",
        "client_id": ETSY_KEYSTRING,
        "redirect_uri": REDIRECT_URI,
        "code": auth_code,
        "code_verifier": verifier,
    }

    req = urllib.request.Request(
        token_url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(req) as resp:
        token_data = json.loads(resp.read())

    access_token = token_data.get("access_token", "")
    refresh_token = token_data.get("refresh_token", "")

    print("\n✅ SUCCESS! Here are your tokens:\n")
    print(f"Access Token (use this now):")
    print(f"  {access_token}\n")
    print(f"Refresh Token (save this to get a new access token later):")
    print(f"  {refresh_token}\n")
    print("─" * 60)
    print("Now run:\n")
    print(f'  export ETSY_API_KEY="{ETSY_KEYSTRING}"')
    print(f'  export ETSY_ACCESS_TOKEN="{access_token}"')
    print(f'  python3 create_divine_listings.py')
    print("─" * 60)

    # Save to a local file for convenience
    creds = {"api_key": ETSY_KEYSTRING, "access_token": access_token, "refresh_token": refresh_token}
    with open("etsy_creds.json", "w") as f:
        json.dump(creds, f, indent=2)
    print("\n💾 Saved to etsy_creds.json (keep this private, don't commit to git)\n")

if __name__ == "__main__":
    main()
