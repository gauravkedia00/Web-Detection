import os

# Imports the Google Cloud client library

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\Orane\YUPEI\visualSearch\visualTest.json"

from booksearch.referenceImageManagement import list_reference_images

#create_product("visualsearch-223211", "europe-west1", "Charles Darwin - Origin of Species 2nd Edition", "Charles Darwin - Origin of Species 2nd Edition", "homegoods")
#add_product_to_product_set("visualsearch-223211", "europe-west1","Charles Darwin - Origin of Species 2nd Edition","visualtestproduct-201811")
#create_reference_image("visualsearch-223211", "europe-west1", "Charles Darwin - Origin of Species 2nd Edition","Charles Darwin - Origin of Species 2nd Edition","gs://visualsearch-223211-vcm/bobbybook/Charles Darwin - Origin of Species 2nd Edition.jpg")

#create_product("visualsearch-223211", "europe-west1", "Charles Dickens Christmas Carol (1st Edition)", "Charles Dickens Christmas Carol (1st Edition)", "homegoods")
#add_product_to_product_set("visualsearch-223211", "europe-west1","Charles Dickens Christmas Carol (1st Edition)","visualtestproduct-201811")
#create_reference_image("visualsearch-223211", "europe-west1", "Charles Dickens Christmas Carol (1st Edition)","Charles Dickens Christmas Carol (1st Edition)","gs://visualsearch-223211-vcm/bobbybook/Charles Dickens Christmas Carol (1st Edition).jpg")


#create_product("visualsearch-223211", "europe-west1", "Charlie and the Chocolate Factory", "Charlie and the Chocolate Factory", "homegoods")
#add_product_to_product_set("visualsearch-223211", "europe-west1","Charlie and the Chocolate Factory","visualtestproduct-201811")
#create_reference_image("visualsearch-223211", "europe-west1", "Charlie and the Chocolate Factory","Charlie and the Chocolate Factory","gs://visualsearch-223211-vcm/bobbybook/Charlie and the Chocolate Factory.jpg")


list_reference_images("visualsearch-223211", "europe-west1", "Alice's Adventures in Wonderland")