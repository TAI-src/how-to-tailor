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
            lines = text.splitlines()
            if lines and lines[0].strip() == "---":
                # Find closing '---' on its own line
                end_index = None
                for i, line in enumerate(lines[1:], start=1):
                    if line.strip() == "---":
                        end_index = i
                        break
                if end_index is not None:
                    yaml_text = "\n".join(lines[1:end_index]).strip()
                    if yaml_text:
                        data = yaml.safe_load(yaml_text)
                        if isinstance(data, dict):
                            title = data.get("title", title)
                            authors = ", ".join(data.get("authors", authors))
                            # If 'title' is present, prefer it explicitly
                            if "title" in data:
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

