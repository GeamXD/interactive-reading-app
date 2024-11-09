import re

def remove_markdown_formatting(markdown_text):
    # Remove links
    markdown_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', markdown_text)  
    # Remove bold and italic text (asterisks and underscores)
    markdown_text = re.sub(r'(\*\*|\*|__|_)(.*?)\1', r'\2', markdown_text)
    # Remove headers
    markdown_text = re.sub(r'^#+\s*', '', markdown_text, flags=re.MULTILINE)
    # Remove blockquotes
    markdown_text = re.sub(r'^\s*>\s*', '', markdown_text, flags=re.MULTILINE)
    # Remove code blocks
    markdown_text = re.sub(r'```[\s\S]*?```', '', markdown_text)
    # Remove inline code
    markdown_text = re.sub(r'`([^`]+)`', r'\1', markdown_text)
    return markdown_text.strip()

