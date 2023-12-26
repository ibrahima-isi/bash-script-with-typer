import typer, typing

from pathlib import Path


MAIN_DIR = Path.cwd() / "data"
app = typer.Typer()

@app.command("run")
def main(ext: str=typer.Argument("txt", help="files type to search"),
         directory: Path=typer.Argument(MAIN_DIR, help="Directory to search in"),
         delete: bool=typer.Option(False, help="delete file if delete option called")
          ):
    """help search a type of extension files

    Args:
        ext (str, optional): the type of files to search. Defaults to typer.Argument("txt", help="files type to search").
        directory (patlib.Path, optional): the directory in which to search. Defaults to typer.Argument(MAIN_DIR, help="Directory to search in").
        delete (bool, optional): help delete the files if called. Defaults to typer.Option(False, help="delete file if delete option called").
    """
    typer.secho(f"recherches des fichier {ext}...", fg=typer.colors.BRIGHT_GREEN, blink=True)

    search_dir = directory
    contents = search_dir.glob(f"*.{ext}")
    content_list = []
    for content in contents:
        typer.secho(f"{content}", fg=typer.colors.BRIGHT_GREEN, blink=True)
        content_list.append(content)
    
    if delete and content_list:
        confirmation_question = typer.style(f"Voulez-vous supprimer ces fichiers avec l'extension .{ext} ?", fg=typer.colors.RED, bold=True)
        typer.confirm(confirmation_question, abort=True)
        for content in contents:
            typer.secho(f"Suppression de {content}", fg=typer.colors.RED)
            content.unlink(missing_ok=True)
    else:
        print("Aucune resulat")
        



@app.command()
def search(s_ext: str="txt"):
    """Search the specified extension file type"""
    main(ext=s_ext, directory=MAIN_DIR, delete=False)

@app.command()
def delete(d_ext: str="txt"):
    """delete the files"""
    main(ext=d_ext, directory=MAIN_DIR, delete=True)




if __name__ == "__main__":
    # typer.run(main)
    app()