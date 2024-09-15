import os
from bs4 import BeautifulSoup
from markdownify import markdownify as md

def strip_html_comments(html_content, start_comment, end_comment):
    start_index = html_content.find(start_comment)
    end_index = html_content.find(end_comment)
    
    if start_index != -1 and end_index != -1:
        html_content = html_content[start_index + len(start_comment):end_index]
    
    return html_content

def convert_html_to_markdown(stripped_html):
    markdown_content = ""
    markdown_content = md(stripped_html)
    return markdown_content



def process_html_files(input_folder, output_folder, start_comment, end_comment):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.html'):
                input_file_path = os.path.join(root, file)
                with open(input_file_path, 'r') as f:
                    html_content = f.read()

                # Strip content between comments
                stripped_html = strip_html_comments(html_content, start_comment, end_comment)
                stripped_html = strip_html_comments(stripped_html, start_comment2, end_comment2)
                # Convert stripped HTML to Markdown
                markdown_content = convert_html_to_markdown(stripped_html)
                subfolder_name = os.path.basename(root)
                output_file_name = f"{file.replace('.html', '.md')}"
                # Create the sub folder if it doesn't exist
                os.makedirs(output_folder + '\\' + subfolder_name, exist_ok=True)
                output_file_path = os.path.join(output_folder +'\\'+ subfolder_name, output_file_name)

                with open(output_file_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)

# Define your input and output folders and comments
input_folder = 'input_files'
output_folder = 'Results'
start_comment = '<!-- Results start here -->'
end_comment = '<!-- Results end here -->'
start_comment2 = '<div class="container">'
end_comment2 = '<!-- container -->'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process the HTML files
process_html_files(input_folder, output_folder, start_comment, end_comment)