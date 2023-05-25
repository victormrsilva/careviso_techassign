# Technical Assignment (Senior DBA)

I present three files to this technical assignment
* npi_model.mwb = EER diagram for the MySQL Workbench
* npi_model.sql = SQL file to create the database and the tables
* connect_api.py = A python file with an example of request to the NPPES NPI API

In this EER, we have six tables, based on the  “CSV to JSON conversion field map” (https://npiregistry.cms.hhs.gov/help-api/json-conversion) and “NPPES Read API Output JSON Document (https://npiregistry.cms.hhs.gov/api-page)” pages:
* Provider: main entity. Store the basic information and NPI number for the provider
* Taxonomy: store the taxonomy data. If I'm not mistaken, the taxonomy code is government-defined. So we can just prepare a full coded taxonomy and create a n:m relationship between provider and taxonomy
* Endpoint: store the endpoint data. I could see that it have some address information, which could be used as a relationship between the Address and Endpoint tables.
* Address: store the address data
* Identifier: store the identifier data
* Other Name: store other names that the provider can have

I tried to guess the datatype for the fields, but I decided to keep the VARCHAR(45) by default for most of the fields.

As always, I'm open to suggestions on how to improve this first model
