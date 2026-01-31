import time, datetime


def main():
    # Your code goes here
    print("Hello, world!")


if __name__ == "__main__":
    # Remove the debug statements marked as "DEBUG" before publishing your project!

    start_time = time.time()  # DEBUG
    print(f"\n[ + ] Started...\n")  # DEBUG
    main()
    end_time = time.time()  # DEBUG
    td = str(datetime.timedelta(seconds=end_time - start_time)).split(":")  # DEBUG
    print(f"\n[ + ] Finished after: {td[0]}h:{td[1]}m:{td[2].split('.')[0]}s\n")  # DEBUG
