import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        html = file.read()

    clean_text = re.sub(r'<[^>]*>', '', html)

    lines = clean_text.splitlines()
    cleaned_lines = [line.strip() for line in lines if line.strip()]

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_lines))


delete_html_tags('draft.html', 'cleaned.txt')