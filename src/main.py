from gui import run_app

def main():
    print("My first personal program")
    print("Trying to run a function from another file\n")
    try:
        result = run_app()
        print(result)
    except AttributeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()