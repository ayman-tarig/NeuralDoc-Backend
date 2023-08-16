from mayan.apps.converter.layers import layer_saved_transformations
from mayan.apps.converter.permissions import (
    permission_transformation_delete, permission_transformation_edit
)
from mayan.apps.converter.tests.mixins import LayerTestMixin
from mayan.apps.documents.tests.literals import TEST_FILE_MULTI_PAGE_TIFF_FILENAME
from mayan.apps.file_caching.events import event_cache_partition_purged
from mayan.apps.file_caching.models import CachePartitionFile
from mayan.apps.file_caching.permissions import permission_cache_partition_purge
from mayan.apps.file_caching.tests.mixins import CachePartitionViewTestMixin

from ..events import (
    event_document_file_deleted, event_document_file_edited
)
from ..permissions import (
    permission_document_file_delete, permission_document_file_edit,
    permission_document_file_print, permission_document_file_view
)

from .base import GenericDocumentViewTestCase
from .mixins.document_file_mixins import (
    DocumentFileTestMixin, DocumentFileTransformationTestMixin,
    DocumentFileTransformationViewTestMixin, DocumentFileViewTestMixin
)


class DocumentFileViewTestCase(
    DocumentFileTestMixin, DocumentFileViewTestMixin,
    GenericDocumentViewTestCase
):
    def test_document_file_delete_no_permission(self):
        first_file = self._test_document.file_latest
        self._upload_test_document_file()

        test_document_file_count = self._test_document.files.count()

        self._clear_events()

        response = self._request_test_document_file_delete_view(
            document_file=first_file
        )
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            self._test_document.files.count(), test_document_file_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_delete_with_access(self):
        first_file = self._test_document.file_latest
        self._upload_test_document_file()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_delete
        )

        test_document_file_count = self._test_document.files.count()

        self._clear_events()

        response = self._request_test_document_file_delete_view(
            document_file=first_file
        )
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            self._test_document.files.count(), test_document_file_count - 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, None)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self._test_document)
        self.assertEqual(events[0].verb, event_document_file_deleted.id)

    def test_trashed_document_file_delete_with_access(self):
        first_file = self._test_document.file_latest
        self._upload_test_document_file()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_delete
        )

        test_document_file_count = self._test_document.files.count()

        self._test_document.delete()

        self._clear_events()

        response = self._request_test_document_file_delete_view(
            document_file=first_file
        )
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            self._test_document.files.count(), test_document_file_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_multiple_delete_no_permission(self):
        self._upload_test_document_file()

        test_document_file_count = self._test_document.files.count()

        self._clear_events()

        response = self._request_test_document_file_multiple_delete_view()

        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            self._test_document.files.count(), test_document_file_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_multiple_delete_with_access(self):
        self._upload_test_document_file()

        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_delete
        )

        test_document_file_count = self._test_document.files.count()

        self._clear_events()

        response = self._request_test_document_file_multiple_delete_view()

        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            self._test_document.files.count(), test_document_file_count - 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, None)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self._test_document)
        self.assertEqual(events[0].verb, event_document_file_deleted.id)

    def test_document_file_edit_view_no_permission(self):
        document_file_comment = self._test_document_file.comment

        self._clear_events()

        response = self._request_test_document_file_edit_view()
        self.assertEqual(response.status_code, 404)

        self._test_document_file.refresh_from_db()
        self.assertEqual(
            self._test_document_file.comment,
            document_file_comment
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_edit_view_with_access(self):
        self.grant_access(
            obj=self._test_document_file,
            permission=permission_document_file_edit
        )

        document_file_comment = self._test_document_file.comment
        document_file_filename = self._test_document_file.filename

        self._clear_events()

        response = self._request_test_document_file_edit_view()
        self.assertEqual(response.status_code, 302)

        self._test_document_file.refresh_from_db()
        self.assertNotEqual(
            self._test_document_file.comment,
            document_file_comment
        )
        self.assertNotEqual(
            self._test_document_file.filename,
            document_file_filename
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 1)

        self.assertEqual(events[0].action_object, self._test_document)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, self._test_document_file)
        self.assertEqual(events[0].verb, event_document_file_edited.id)

    def test_trashed_document_file_edit_view_with_access(self):
        self.grant_access(
            obj=self._test_document_file,
            permission=permission_document_file_edit
        )

        document_file_comment = self._test_document_file.comment
        document_file_filename = self._test_document_file.filename

        self._test_document.delete()

        self._clear_events()

        response = self._request_test_document_file_edit_view()
        self.assertEqual(response.status_code, 404)

        self._test_document_file.refresh_from_db()
        self.assertEqual(
            self._test_document_file.comment,
            document_file_comment
        )
        self.assertEqual(
            self._test_document_file.filename,
            document_file_filename
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_list_no_permission(self):
        self._clear_events()

        response = self._request_test_document_file_list_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_list_with_access(self):
        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_view
        )

        self._clear_events()

        response = self._request_test_document_file_list_view()
        self.assertContains(
            response=response, status_code=200,
            text=str(self._test_document_file)
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_trashed_document_file_list_with_access(self):
        self.grant_access(
            obj=self._test_document,
            permission=permission_document_file_view
        )

        self._test_document.delete()

        self._clear_events()

        response = self._request_test_document_file_list_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_print_form_view_no_permission(self):
        self._clear_events()

        response = self._request_test_document_file_print_form_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_print_form_view_with_access(self):
        self.grant_access(
            obj=self._test_document_file,
            permission=permission_document_file_print
        )

        self._clear_events()

        response = self._request_test_document_file_print_form_view()
        self.assertEqual(response.status_code, 200)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_trashed_document_file_print_form_view_with_access(self):
        self.grant_access(
            obj=self._test_document_file,
            permission=permission_document_file_print
        )

        self._test_document.delete()

        self._clear_events()

        response = self._request_test_document_file_print_form_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_print_view_no_permission(self):
        self._clear_events()

        response = self._request_test_document_file_print_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_print_view_with_access(self):
        self.grant_access(
            obj=self._test_document_file,
            permission=permission_document_file_print
        )

        self._clear_events()

        response = self._request_test_document_file_print_view()
        self.assertEqual(response.status_code, 200)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_trashed_document_file_print_view_with_access(self):
        self.grant_access(
            obj=self._test_document_file,
            permission=permission_document_file_print
        )

        self._test_document.delete()
        self._clear_events()

        response = self._request_test_document_file_print_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_properties_view_no_permission(self):
        self._clear_events()

        response = self._request_test_document_file_properties_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_properties_view_with_access(self):
        self.grant_access(
            obj=self._test_document_file,
            permission=permission_document_file_view
        )

        self._clear_events()

        response = self._request_test_document_file_properties_view()
        self.assertContains(
            response=response, text=self._test_document_file.filename,
            status_code=200
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_trashed_document_file_properties_view_with_access(self):
        self.grant_access(
            obj=self._test_document_file,
            permission=permission_document_file_view
        )

        self._test_document.delete()
        self._clear_events()

        response = self._request_test_document_file_properties_view()
        self.assertEqual(response.status_code, 404)

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)


class DocumentFileTransformationViewTestCase(
    LayerTestMixin, DocumentFileTransformationTestMixin,
    DocumentFileTransformationViewTestMixin, GenericDocumentViewTestCase
):
    _test_document_filename = TEST_FILE_MULTI_PAGE_TIFF_FILENAME

    def test_document_file_transformations_clear_view_no_permission(self):
        self._create_document_file_transformation()

        transformation_count = layer_saved_transformations.get_transformations_for(
            obj=self._test_document_file.pages.first()
        ).count()

        self._clear_events()

        response = self._request_test_document_file_transformations_clear_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            layer_saved_transformations.get_transformations_for(
                obj=self._test_document_file.pages.first()
            ).count(), transformation_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_transformations_clear_view_with_access(self):
        self._create_document_file_transformation()

        transformation_count = layer_saved_transformations.get_transformations_for(
            obj=self._test_document_file.pages.first()
        ).count()

        self.grant_access(
            obj=self._test_document_file,
            permission=permission_transformation_delete
        )

        self._clear_events()

        response = self._request_test_document_file_transformations_clear_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            layer_saved_transformations.get_transformations_for(
                obj=self._test_document_file.pages.first()
            ).count(), transformation_count - 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_trashed_document_file_transformations_clear_view_with_access(self):
        self._create_document_file_transformation()

        transformation_count = layer_saved_transformations.get_transformations_for(
            obj=self._test_document_file.pages.first()
        ).count()

        self.grant_access(
            obj=self._test_document_file,
            permission=permission_transformation_delete
        )

        self._test_document.delete()

        self._clear_events()

        response = self._request_test_document_file_transformations_clear_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            layer_saved_transformations.get_transformations_for(
                obj=self._test_document_file.pages.first()
            ).count(), transformation_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_multiple_transformations_clear_view_no_permission(self):
        self._create_document_file_transformation()

        transformation_count = layer_saved_transformations.get_transformations_for(
            obj=self._test_document_file.pages.first()
        ).count()

        self._clear_events()

        response = self._request_test_document_file_multiple_transformations_clear_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            layer_saved_transformations.get_transformations_for(
                obj=self._test_document_file.pages.first()
            ).count(), transformation_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_multiple_transformations_clear_view_with_access(self):
        self._create_document_file_transformation()

        transformation_count = layer_saved_transformations.get_transformations_for(
            obj=self._test_document_file.pages.first()
        ).count()

        self.grant_access(
            obj=self._test_document_file,
            permission=permission_document_file_view
        )
        self.grant_access(
            obj=self._test_document_file,
            permission=permission_transformation_delete
        )

        self._clear_events()

        response = self._request_test_document_file_multiple_transformations_clear_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            layer_saved_transformations.get_transformations_for(
                obj=self._test_document_file.pages.first()
            ).count(), transformation_count - 1,
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_transformations_clone_view_no_permission(self):
        self._create_document_file_transformation()

        page_first_transformation_count = layer_saved_transformations.get_transformations_for(
            obj=self._test_document_file.pages.first()
        ).count()
        page_last_transformation_count = layer_saved_transformations.get_transformations_for(
            obj=self._test_document_file.pages.last()
        ).count()

        self._clear_events()

        response = self._request_test_document_file_transformations_clone_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            layer_saved_transformations.get_transformations_for(
                obj=self._test_document_file.pages.first()
            ).count(), page_first_transformation_count
        )
        self.assertEqual(
            layer_saved_transformations.get_transformations_for(
                obj=self._test_document_file.pages.last()
            ).count(), page_last_transformation_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_transformations_clone_view_with_access(self):
        self._create_document_file_transformation()

        page_first_transformation_count = layer_saved_transformations.get_transformations_for(
            obj=self._test_document_file.pages.first()
        ).count()
        page_last_transformation_count = layer_saved_transformations.get_transformations_for(
            obj=self._test_document_file.pages.last()
        ).count()

        self.grant_access(
            obj=self._test_document_file,
            permission=permission_transformation_edit
        )

        self._clear_events()

        response = self._request_test_document_file_transformations_clone_view()
        self.assertEqual(response.status_code, 302)

        self.assertEqual(
            layer_saved_transformations.get_transformations_for(
                obj=self._test_document_file.pages.first()
            ).count(), page_first_transformation_count
        )
        self.assertEqual(
            layer_saved_transformations.get_transformations_for(
                obj=self._test_document_file.pages.last()
            ).count(), page_last_transformation_count + 1
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)


class DocumentFileCachePurgeViewTestCase(
    CachePartitionViewTestMixin, GenericDocumentViewTestCase
):
    def test_document_file_cache_purge_no_permission(self):
        self._test_object = self._test_document_file
        self._inject_test_object_content_type()

        self._test_document_file.file_pages.first().generate_image()

        test_document_file_cache_partitions = self._test_document_file.get_cache_partitions()

        cache_partition_file_count = CachePartitionFile.objects.filter(
            partition__in=test_document_file_cache_partitions
        ).count()

        self._clear_events()

        response = self._request_test_object_file_cache_partition_purge_view()
        self.assertEqual(response.status_code, 404)

        self.assertEqual(
            CachePartitionFile.objects.filter(
                partition__in=test_document_file_cache_partitions
            ).count(), cache_partition_file_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 0)

    def test_document_file_cache_purge_with_access(self):
        self._test_object = self._test_document_file
        self._inject_test_object_content_type()

        self.grant_access(
            obj=self._test_document_file,
            permission=permission_cache_partition_purge
        )

        self._test_document_file.file_pages.first().generate_image()

        test_document_file_cache_partitions = self._test_document_file.get_cache_partitions()

        cache_partition_file_count = CachePartitionFile.objects.filter(
            partition__in=test_document_file_cache_partitions
        ).count()

        self._clear_events()

        cache_partitions = self._test_document_file.get_cache_partitions()

        response = self._request_test_object_file_cache_partition_purge_view()
        self.assertEqual(response.status_code, 302)

        self.assertNotEqual(
            CachePartitionFile.objects.filter(
                partition__in=test_document_file_cache_partitions
            ).count(), cache_partition_file_count
        )

        events = self._get_test_events()
        self.assertEqual(events.count(), 2)

        self.assertEqual(events[0].action_object, self._test_document_file)
        self.assertEqual(events[0].actor, self._test_case_user)
        self.assertEqual(events[0].target, cache_partitions[0])
        self.assertEqual(events[0].verb, event_cache_partition_purged.id)

        self.assertEqual(events[1].action_object, self._test_document_file)
        self.assertEqual(events[1].actor, self._test_case_user)
        self.assertEqual(events[1].target, cache_partitions[1])
        self.assertEqual(events[1].verb, event_cache_partition_purged.id)
