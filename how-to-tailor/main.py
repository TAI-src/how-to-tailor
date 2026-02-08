from pathlib import Path
import yaml

def glob(pattern, hide=None, page_path=None, current_page=None):
    """
    Generate links relative to the folder of the current page.
    """
    hide = hide or []
    base = Path(__file__).parent / "docs"
    files = sorted(base.glob(pattern))
    pages = []

    # folder of the page, relative to docs
    if page_path:
        page_folder = Path(page_path).parent
    else:
        page_folder = Path("")

    for f in files:
        if f.name in hide:
            continue
        # Determine title
        title = f.stem.replace("_", " ").title()
        authors = []

        # Read YAML front-matter title if available
        try:
            text = f.read_text(encoding="utf-8")
            # YAML frontmatter is usually at the top
            if text.startswith("---"):
                end = text.find("---", 3)
                yaml_text = text[3:end].strip()
                data = yaml.safe_load(yaml_text)
                title = data.get("title", title)
                authors = ", ".join(data.get("authors", authors))
                title = data["title"]
        except Exception:
            pass
        
        # relative to the page folder
        rel_url = f.relative_to(base / page_folder).as_posix()
        pages.append({
            "title": title,
            "url": rel_url,
            "authors": authors
        })
        

    return pages

def define_env(env):
    env.macro(glob)

