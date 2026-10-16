#!/usr/bin/env python3
"""patent-kit confidentiality guard (PreToolUse hook).

Inside a patent workspace (a folder containing a `.patent-kit` marker, or any folder below it), anything that could
send the invention out of the machine needs the inventor's explicit approval each time:
  - web searches and page fetches (a search query can reveal the idea),
  - git push, gist or repository creation, and uploads with curl or similar,
  - publishing tools (artifacts, documents, posts) from any connected service.
Outside a workspace the hook does nothing.
"""
import json, pathlib, re, sys

PUBLISHING = re.compile(r"(create|publish|upload|post|send|share|update|write|batch)", re.I)
RISKY_BASH = re.compile(
    r"\bgit\s+push\b|\bgh\s+(repo\s+create|gist|release)\b|\bcurl\b[^|;&]*\s(-F|--form|-T|--upload-file|-d|--data\S*)\s"
    r"|\b(scp|sftp)\b|\brsync\b[^|;&]*\s\S+:\S*", re.I)


def in_workspace(start):
    p = pathlib.Path(start or ".").resolve()
    for d in [p, *p.parents]:
        if (d / ".patent-kit").exists():
            return d
    return None


def ask(reason):
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "ask",
        "permissionDecisionReason": "patent-kit: " + reason}}))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    ws = in_workspace(data.get("cwd"))
    if not ws:
        sys.exit(0)
    tool, inp = data.get("tool_name", ""), data.get("tool_input") or {}
    if tool == "WebSearch":
        ask(f"web search from a patent workspace. Query: \"{inp.get('query', '')}\". "
            "Approve only if it uses generic terms and does not describe the new combination.")
    if tool == "WebFetch":
        ask(f"page fetch from a patent workspace: {inp.get('url', '')}. Check that the URL and prompt reveal nothing new.")
    if tool == "Bash" and RISKY_BASH.search(inp.get("command", "")):
        ask("this command may send files out of the machine. Nothing about the invention leaves before filing.")
    if tool == "Artifact" or (tool.startswith("mcp__") and PUBLISHING.search(tool)):
        ask(f"{tool} may publish or share content. Nothing about the invention is published before filing.")
    sys.exit(0)


if __name__ == "__main__":
    main()
