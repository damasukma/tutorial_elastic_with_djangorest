from django_elasticsearch_dsl import Document, Index
# from django_elasticsearch_dsl.registries import registry

from .models import ProjectApplication

file_log_type = Index('log_file_search')

file_log_type.settings(
    number_of_shards=1,
    number_of_replicas=0
)

# @registry.register_document
@file_log_type.doc_type
class ProjectApplicationDocument(Document):
    class Django:
        model = ProjectApplication
        fields = [
            'project_name',
            'path_file',
            'status_log'
        ]
