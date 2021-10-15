import vm


def main() -> None:
    cred = vm.get_credentials("sample-secrets.json")
    print(cred)
    return


if __name__ == "__main__":
    main()
