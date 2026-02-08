# Example Index

{% for p in glob("examples/*.md", hide=["example_template.md", "index.md"], page_path=page.file.src_path) %}
- [{{ p.title }}]({{ p.url }}) ({{ p.authors }})
{% endfor %}


