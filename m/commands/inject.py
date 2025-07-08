from pathlib import Path
from sysconfig import get_path


def inject():
    inject_path = Path(get_path("purelib")) / "moderate.pth"
    project_root = Path(__file__, "../../..").resolve()
    inject_path.write_text(str(project_root))

    print(f"\n Wrote {project_root} to {inject_path}", end="\n\n")


if __name__ == "__main__":
    inject()

else:
    from typer import Typer

    (app := Typer()).command()(inject)
