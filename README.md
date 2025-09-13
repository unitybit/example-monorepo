# Example Monorepo (Windows self-contained packaging)

This is a minimal monorepo you can push to GitHub to test Windows-only packaging
with a **portable Python runtime** and **tag-triggered prerelease**.

## Layout

```
example-monorepo/
  apps/
    myapp/
      app/               # your package/module
      pyproject.toml     # declares deps (uses `rich` as a demo)
  .github/workflows/release-windows.yml
```

## How to test

1. **Create a new GitHub repo** and push this folder's contents.
2. Edit `.github/workflows/release-windows.yml` and set `PBS_URL` to a real Windows asset from
   [python-build-standalone Releases](https://github.com/astral-sh/python-build-standalone/releases).
   Choose an `x86_64-pc-windows-msvc` archive ending with `-pgo+lto-full.zip` for your desired Python version.
3. (Optional) In `apps/myapp`, run `uv lock` locally to write `uv.lock` so the workflow uses exact pins.
4. Create a **tag** to release just this app:
   ```bash
   git tag myapp-v1.0.0
   git push origin myapp-v1.0.0
   ```
5. The workflow will produce a **prerelease** named `MyApp 1.0.0` with an artifact like `MyApp-1.0.0-windows.zip`.
   Unzip and double-click `run.bat`. Works offline.

## Notes

- If no `uv.lock` is present, the workflow falls back to installing from `pyproject.toml`.
- The bundled runtime comes from python-build-standalone, which includes `pip` so we can install deps directly.
- You can add more apps by copying `apps/myapp` to another folder and updating the switch in the workflow to map tag prefix → subdir.
