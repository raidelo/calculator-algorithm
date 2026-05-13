PROMPT = ">> "


def main() -> None:
    while True:
        inp = input(PROMPT)

        if inp.lower() in ["q", "quit", "exit"]:
            break

    print("\nExitting ...")
