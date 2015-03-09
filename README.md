
SearchYourFood
=====================

Search Your Food is Web service created using Python web service and REST Interface

Service searches for the food item in given location and gets all the restaurants information.

## Do you want to search your favourite food item in your favourite location?

* Url: `/scrape?fi=<"FOODITEM">&gl=<"SEARCH LOCATION">&p=<"NO OF PAGES"> `
* Returns: JSON list of restaurant name, Website, address, contact ,location

Example usage:
```
$ curl http://localhost:8080/scrape?fi=icecream&gl=cincinnati&p=1
{"Website": ["http://www.pinogelato.com",....],
 "Ratings": [ 4,....],
 "Contact": ["(614) 792-7876", ....],
 "Locality": ["OH",....],
 "Business_Name": ["Pino Gelato Bistro", .... ], 
 "Street_Address": ["4435 W Dublin Granville Rd", .... ]} 
```

## Docker Notes

Docker container contains all the software (OS,CODE,SERVER, DEPENDENT PACKAGES installed) required to start the webservice and then directly accesing the application from your local with out installing all necessary software again.

### Information and installation:
Information about docker and istallation can be found in https://docs.docker.com/installation/ .

After installing the docker successfully..

Download this continer here: https://www.dropbox.com/s/nz7qqirhga6vrbh/findfood.tar.gz?dl=0

```
gzip -d findfood.tar.tz
docker import findfood.tar
or try
docker load -i findfood.tar
```

Run `/startme.sh` in the docker container to start the web server.

Example starting this container:
```
docker run -d -p 8080:80 findfood /startme.sh
```
This will start the container, the webserver, and forward traffic on your port 8080 into the container.
when container is started it will generate image with image id like  "c2926b4sdfksdfsbksdkfsbk.........". This image id will be helpful to stop the container

Now, open the browser and try with the link as in example .
Example 

```
http://localhost:8080/scrape?fi=icecream&gl=dubai&p=1
```
After testing the sever . you can stop the container which will automatically closes the server.

```
stop container c29
```
Here c29 is the first 3 letters of the image id generated when the container started


## Future Work 
* Additional functionality that can be added in future
* provide the features to get first 5 entires
* provide the features to get top 10 restaurants for the given food category and location.




