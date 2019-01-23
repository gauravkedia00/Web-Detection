import io
import os

# Imports the Google Cloud client library
from google.cloud import vision_v1p3beta1 as vision


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Orane\YUPEI\visualSearch\visualTest.json"

def add_product_to_product_set(
        project_id, location, product_id, product_set_id):
    """Add a product to a product set.
    Args:
        project_id: Id of the project.
        location: A compute region name.
        product_id: Id of the product.
        product_set_id: Id of the product set.
    """
    client = vision.ProductSearchClient()

    # Get the full path of the product set.
    product_set_path = client.product_set_path(
        project=project_id, location=location,
        product_set=product_set_id)

    # Get the full path of the product.
    product_path = client.product_path(
        project=project_id, location=location, product=product_id)

    # Add the product to the product set.
    client.add_product_to_product_set(
        name=product_set_path, product=product_path)
    print('Product added to product set.')



#add_product_to_product_set("visualsearch-223211", "europe-west1","A Wrinkle in Time","visualtestproduct-201811")