# WHY THIS FILE EXISTS:
# We isolate all database logic here. If we ever switch from Supabase to
# PostgreSQL directly or another DB, we only change THIS file — nothing else
# needs to know how data is stored.
#
# This pattern is called the "Repository Pattern" — the database is a
# black box to the rest of the app. You call save_message() and don't
# care how it's stored.
# ─────────────────────────────────────────────────────────────────────────────
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from datetime import datetime, timezone
from models import HistoryItem

# SETUP
# Load the .env file so os.getenv() can read our secrets
# Without this, SUPABASE_URL and SUPABASE_KEY would be None
load_dotenv()

# Read credentials from environment variables
# NEVER hardcode secrets like: url = "https://abc.supabase.co"
# That would be a security disaster if committed to git
SUPABASE_URL: str = os.getenv("SUPABASE_URL")
SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

# Validate that we actually have the credentials
# Fail loudly at startup rather than mysteriously later
if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(
        "Missing SUPABASE_URL or SUPABASE_KEY in environment variables. "
        "Check your .env file."
    )
