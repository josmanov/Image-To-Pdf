from gui import run_app

def main():
    try:
        result = run_app()
        print(result)
    except AttributeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()