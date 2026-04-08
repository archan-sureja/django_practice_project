import os 
from django.core.files.uploadhandler import FileUploadHandler, SkipFile, StopUpload

class ValidationUploadHandler(FileUploadHandler):
    ALLOWED_EXTENSIONS = {".pdf", ".doc", ".docx"}
    MAX_SIZE = 5 * 1024 * 1024  # 5MB

    def __init__(self, request=None):
        super().__init__(request)
        self.bytes_received = 0
        print("[HANDLER] __init__ called")

    def new_file(self, field_name, file_name, content_type, content_length, charset=None, content_type_extra=None):
        print(f"[HANDLER] new_file called: {file_name}, type: {content_type}, size: {content_length}")
        super().new_file(field_name, file_name, content_type, content_length, charset, content_type_extra)
        ext = os.path.splitext(file_name)[1].lower()
        print(f"[HANDLER] File extension: {ext}, Allowed: {self.ALLOWED_EXTENSIONS}")

        if ext not in self.ALLOWED_EXTENSIONS:
            print(f"[HANDLER] Rejecting file: {ext} not allowed")
            raise SkipFile(f"File type {ext} not allowed")

        self.bytes_received = 0
        # print("[HANDLER] File accepted")
    
    def receive_data_chunk(self, raw_data, start):
        self.bytes_received += len(raw_data)
        print(f"[HANDLER] receive_data_chunk: {self.bytes_received} bytes")
        if self.bytes_received > self.MAX_SIZE:
            raise StopUpload(connection_reset=True)
        return raw_data

    def file_complete(self, file_size):
        print(f"[HANDLER] file_complete called, size: {file_size}")
        return None