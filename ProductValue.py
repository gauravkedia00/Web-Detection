import os

# Imports the Google Cloud client library
from google.cloud import vision_v1p3beta1 as vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Orane\YUPEI\visualSearch\visualTest.json"
def update_product_labels(
        project_id, location, product_id, key, value):
    """Update the product labels.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        key: The key of the label.
        value: The value of the label.
    """
    client = vision.ProductSearchClient()

    # Get the name of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Set product name, product label and product display name.
    # Multiple labels are also supported.
    key_value = vision.types.Product.KeyValue(key=key, value=value)
    product = vision.types.Product(
        name=product_path,
        product_labels=[key_value])

    # Updating only the product_labels field here.
    update_mask = vision.types.FieldMask(paths=['product_labels'])

    # This overwrites the product_labels.
    updated_product = client.update_product(
        product=product, update_mask=update_mask)

    # Display the updated product information.
    print('Product name: {}'.format(updated_product.name))
    print('Updated product labels: {}'.format(product.product_labels))

update_product_labels("visualsearch-223211", "europe-west1","Alice's Adventures in Wonderland", "Category", "Children")

#update_product_labels("visualsearch-223211", "europe-west1","Animal Farm", "Category", "Political")
#update_product_labels("visualsearch-223211", "europe-west1","Casino Royale", "Category", "Children")
#update_product_labels("visualsearch-223211", "europe-west1","Book of Thoth", "Category", "Children")
#update_product_labels("visualsearch-223211", "europe-west1","Castle Otranto", "Category", "Children")
#update_product_labels("visualsearch-223211", "europe-west1","Charles Darwin - Origin of Species 2nd Edition", "Category", "Children")
#update_product_labels("visualsearch-223211", "europe-west1","Charles Darwin - Origin of Species 2nd Edition", "Category", "Children")
#update_product_labels("visualsearch-223211", "europe-west1","Charlie and the Chocolate Factory", "Category", "Children")