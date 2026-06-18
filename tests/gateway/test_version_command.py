"""Tests for gateway /version command."""

import asyncio

from hermes_agent.hermes_cli.banner import format_banner_version_label


def test_gateway_version_command_returns_release_line():
    from hermes_agent.gateway.run import GatewayRunner

    result = asyncio.run(GatewayRunner._handle_version_command(None, None))  # type: ignore[arg-type]
    assert result == format_banner_version_label()
