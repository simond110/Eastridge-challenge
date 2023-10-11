## Run the project on the local machine
-run script
```
sudo docker-compose up -d
```
- Navgiate http://127.0.0.1:8000/swagger-ui/
## Postman Collection
postman_collection.json file exists in the source directory.
You can import it into the Postman Software and experiment the rest api after you run the project succesfully
## API DETAIL
1. Invoices API
   - `GET` `/api/invoices/?format=json` <br/>
   List the Invoices with pangiation. <br/>
   format query params are optional and by default it renders the data in JSON format.
   if you specify `?format=xml` api response in XML format.
   - `POST` `/api/invoices/` <br/>
   Create the Invoice
   - `GET` `/api/invoices/{invoice_id}/` <br/>
     List the Invoice data of given invoice_id
   - `PUT` `/api/invoices/{invoice_id}/` <br/>
     Update or Replace the Existing Invoice data
   - `Delete` `/api/invoices/{invoice_id}/`
     Delete the Invoice
   - `GET` `/api/invoices/{invoice_id/items/?format=json` <br/>
     List the Invoice Items of given invoice_id
     Pagination features are present.
   - `POST` `/api/invoices/{invoice_id/items/` <br/> 
     Add the Invoice Item to the given invoice_id
   - `GET|PUT|DELETE` `/api/invoices/{invoice_id}/items/{invoice_item_id}/` <br/>
     List|Update|Delete the Invoice Item of given id of given invoice id
2. Invoice Items API 
   - `GET` `/api/invoice-items/?format=json` <br/>
      List the invoice items with pagination. support both json and xml.
   - `POST` `/api/invoice-items/` <br/>
      Create the invoice item.
   - `GET` `/api/invoice-items/{invoice_item_id}/` <br/>
      Retrieve the Invoice Item with invoice_item_id   
   - `PUT` `/api/invoice-items/?format=json` <br/>
      Update the Invoice Item with invoice_item_id
   - `DELETE` `/api/invoice-items/?format=json` <br/>
      Delete the Invoice Item with invoice_item_id

## Swagger UI 
- You can browse API with swagger UI on http://<domain_name>/swagger-ui/