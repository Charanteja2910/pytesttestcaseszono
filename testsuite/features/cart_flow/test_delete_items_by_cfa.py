from features.orders.items_delete_by_cfa import delete_items_by_cfa
from features.orders.get_pofile import get_pofile_data
from settings.conftest import checking_the_status_code_201


deleted_by_cfa_response = delete_items_by_cfa()

pofile_response =get_pofile_data().json()

ids_in_pofile = []
for i in pofile_response["files"]:
    if i["importSource"] == "manual":
        ids_in_pofile.append(i["lines"][0]["productVariantId"])


def test_deleted_by_cfa():
    assert checking_the_status_code_201(deleted_by_cfa_response)
    assert len(ids_in_pofile) == 0
