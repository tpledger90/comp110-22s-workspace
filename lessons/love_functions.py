def love(name: str) -> str:
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {name}"

    def spread_love(to: str, n: int) -> str:
        """Gnerates a string that repeats a loving message n times"""
        love_note: str = ""
        count: int = 0

        while count < n:
            love_note += love(to) + "\n"
            count += 1
        return love_note


"""def main() -> None:
    print(spread_love("Brooks", 5))

if __name__ == "__main__":
    main()"""
