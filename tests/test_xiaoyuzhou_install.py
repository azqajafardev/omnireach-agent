# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path
from unittest.mock import patch

import agent_reach.cli as cli

ROOT = Path(__file__).resolve().parents[1]
TRANSCRIBE_SCRIPT = ROOT / "agent_reach" / "scripts" / "transcribe_xiaoyuzhou.sh"


class _DummyConfig:
    def get(self, _key):
        return None


def test_install_xiaoyuzhou_deps_does_not_raise_when_no_groq_key(capsys):
    with patch("agent_reach.config.Config", return_value=_DummyConfig()), \
         patch("os.path.isfile", side_effect=lambda p: True if str(p).endswith("transcribe.sh") else False), \
         patch("shutil.which", return_value=None):
        cli._install_xiaoyuzhou_deps()

    out = capsys.readouterr().out
    assert "Xiaoyuzhou" in out
    assert "Groq API key not set" in out


def test_transcribe_script_is_cross_platform_shell_syntax():
    subprocess.run(["bash", "-n", str(TRANSCRIBE_SCRIPT)], check=True)


def test_transcribe_script_handles_git_bash_python_and_size_math():
    text = TRANSCRIBE_SCRIPT.read_text(encoding="utf-8")
    assert "command -v python3" in text
    assert "command -v python" in text
    assert "command -v py" in text
    assert "cygpath -w" in text
    assert "| bc" not in text
