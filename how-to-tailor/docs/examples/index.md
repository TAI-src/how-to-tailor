# Example Index

{% for page in glob("examples/*.md", hide=["example_template.md", "index.md"], page_path=page.file.src_path) %}
- [{{ page.title }}]({{ page.url }}) ({{ page.authors }})
{% endfor %}


