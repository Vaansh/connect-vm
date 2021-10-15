import vm


def main() -> None:
    cred = vm.get_credentials("sample-secrets.json")
    vm.open_vm()


if __name__ == "__main__":
    main()
