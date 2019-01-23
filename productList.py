import os

# Imports the Google Cloud client library
from google.cloud import vision_v1p3beta1 as vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Orane\YUPEI\visualSearch\visualTest.json"

def list_products(project_id, location):
    """List all products.
    Args:
        project_id: Id of the project.
        location: A compute region name.
    """
    client = vision.ProductSearchClient()

    # A resource that represents Google Cloud Platform location.
    location_path = client.location_path(project=project_id, location=location)

    # List all the products available in the region.
    products = client.list_products(parent=location_path)

    # Display the product information.
    for product in products:
        print('Product name: {}'.format(product.name))
        print('Product id: {}'.format(product.name.split('/')[-1]))
        print('Product display name: {}'.format(product.display_name))
        print('Product description: {}'.format(product.description))
        print('Product category: {}'.format(product.product_category))
        print('Product labels: {}\n'.format(product.product_labels))

