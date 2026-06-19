import re
from pathlib import Path

from hermes_agent import read_source_file



def test_sidecar_session_create_requests_close_on_disconnect():
    """The sidecar must opt its session into close_on_disconnect so the gateway
    reaps the slash_worker on WS disconnect (the #21370/#21467 leak)."""
    source = read_source_file("web/src/components/ChatSidebar.tsx")
    call = re.search(r'"session\.create",\s*\{(.*?)\}', source, re.DOTALL)
    assert call, "sidecar session.create call not found"
    assert re.search(r"close_on_disconnect:\s*true", call.group(1))


def test_sidecar_session_create_scopes_profile():
    """The sidecar must pass the dashboard's selected profile so model/credential
    info matches the PTY child under profile-scoped chat."""
    source = read_source_file("web/src/components/ChatSidebar.tsx")
    assert '"session.create"' in source
    assert re.search(
        r"close_on_disconnect:\s*true,\s*\.\.\.\(profile\s*\?\s*\{\s*profile\s*\}\s*:\s*\{\}\)",
        source,
        re.DOTALL,
    )
