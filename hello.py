import typer

def main(
    name: str = typer.Argument(..., help="Имя пользователя"),
    lastname: str = typer.Option("", "--lastname", "-l", help="Фамилия пользователя"),
):
    """
    Автоматическое приветствие:
    - если указана только имя → "Привет, {name}!"
    - если указаны имя и фамилия → "Добрый день, {name} {lastname}!"
    """
    lastname = (lastname or "").strip()

    if lastname:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
