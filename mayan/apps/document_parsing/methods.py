from django.apps import apps
from django.utils.html import conditional_escape
import requests

from .events import event_parsing_document_file_submitted
from .tasks import task_parse_document_file

def method_document_content(self):
    file_latest = self.file_latest
    if file_latest:
        return file_latest.content()
    else:
        return []


def method_document_parsing_submit(self, user=None):
    latest_file = self.file_latest
    # Don't error out if document has no file.
    if latest_file:
        latest_file.submit_for_parsing(user=user)


def method_document_file_content(document_file):
    DocumentFilePageContent = apps.get_model(
        app_label='document_parsing', model_name='DocumentFilePageContent'
    )

    for page in document_file.pages.all():
        try:
            page_content = page.content.content
        except DocumentFilePageContent.DoesNotExist:
            """Page has no content, skip."""
        else:
            yield conditional_escape(
                text=str(page_content)
            )


def method_document_file_parsing_submit(self, user=None):
    if user:
        user_id = user.pk
    else:
        user_id = None

    event_parsing_document_file_submitted.commit(
        action_object=self.document, actor=user, target=self
    )

    file_ocr_content = task_parse_document_file(self.pk, user_id)
    
    document_data =  {
        "id": self.pk,
        "uuid": self.uuid,
        "title": self.filename,
        "content": file_ocr_content,
        "mime_type": self.mimetype,
        "size": self.size,
    }
    
    print("BEFORE SENDING TO AI ENGINE");
    method_document_send_to_ai_engine(document_data)


def method_document_send_to_ai_engine(document_data):
    """
    Send the document content + document id to the AI engine
    """
    # Steps
    # -> Make a text file that contains the document_content and document_id
    # -> Send the text file to the AI engine API
    
    # -> AI Engine API URL: http://212.227.189.196:8000/file-upload 
    # -> AI Query URL: http://212.227.189.196:8000/query 
    
    # Create file content
    file_content = f"content: {document_data['content']}\n"

    for key, value in document_data.items():
        if key != 'content':
            file_content += f"{key}: {value}\n"

    # Create a file-like object
    file_data = {'files': ('file.txt', file_content)}
    
    try:
        url = 'http://212.227.189.196:8000/file-upload'
        response = requests.post(url, files=file_data)

        # Check the response status
        if response.status_code == 200:
            print('File sent successfully!')
        else:
            print('Error sending file. Status code:', response.status_code)

    except requests.exceptions.RequestException as e:
        print('An error occurred:', str(e))
        