from importlib.metadata import version, PackageNotFoundError

def main():
    try:
        ver = version("myapp")
    except PackageNotFoundError:
        ver = "0.0.0"
    print(f"MyApp running (version: {ver})")
    try:
        from rich import print as rprint
        rprint("[bold green]It works![/] This is a demo packaged with a portable Python runtime.")
    except Exception as e:
        print("Optional: rich not available or failed to import:", e)

if __name__ == "__main__":
    main()
