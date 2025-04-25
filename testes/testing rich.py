from rich import print
pergunta = input("Escolha uma cor: ").lower()
if pergunta == "azul":
    print("[#002aff]AZUL![/#002aff]")
if pergunta == "vermelho":
    print("[red]VERMELHO![/red]")
if pergunta == "amarelo":
    print("[yellow]AMARELO![/yellow]")
else:
    print("[bold]Ainda não adicionei essa cor[/bold] [italic]kkk[/italic]")