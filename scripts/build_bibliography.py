# Import necessary libraries
import os
import markdownify
from pyzotero import zotero
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve Zotero credentials from environment variables
ZOTERO_API_KEY = os.getenv("ZOTERO_API_KEY")
ZOTERO_USER_ID = os.getenv("ZOTERO_USER_ID")
COLLECTION_KEY = os.getenv("ZOTERO_COLLECTION_KEY")

# Initialize Zotero client
zot = zotero.Zotero(ZOTERO_USER_ID, "user", ZOTERO_API_KEY)

# Fetch items from the specified collection
collection_items = zot.everything(zot.collection_items(collection=COLLECTION_KEY))

# Function to convert Zotero HTML italics to Markdown italics
def convert_to_markdown(content):
    return markdownify.markdownify(content)

# Format Zotero items into MLA-style citations with Markdown italics
def format_citations(items):
    citations = []
    for item in items:
        citation = f"*{item['title']}*"
        if 'creators' in item:
            citation += ", "
            citation += ", ".join([f"{creator['lastName']}, {creator['firstName']}" for creator in item['creators']])
        if 'date' in item:
            citation += f", {item['date']}"
        if 'publisher' in item:
            citation += f", {item['publisher']}"
        citations.append(citation)
    return "\n".join(citations)

# Generate the bibliography content
bibliography_content = format_citations(collection_items)

# Write the bibliography to a markdown file
file_path = os.path.join(os.getcwd(), "bibliography.md")
with open(file_path, "w", encoding="utf-8") as file:
    file.write(bibliography_content)

print(f"Bibliography successfully generated and saved to {file_path}")
