#!/usr/bin/python

"""
Webserver - Python - REST - Search Your Food 

Run Instructions: Run the following command in the command line to start the server on port:8080

python <path>/searchurfood.py

Inputs :http://localhost:8080/scrap?st="Food Item you would like to Search"&gl="Location of Search"%27&p="No of pages"
Ex     : http://localhost:8080/scrap?st=chicken&gl=cincinnati%27&p=2

Output : you will get the data in Json format on your web browser 
"""
#Import packages 
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import json
import urlparse
import sys
import urllib2 as url 
import bs4
import re
import requests


PORT_NUMBER = 8080

#build the urls for individual selection and page numbers
def get_url_build(base_url,limit):

   """ 
   cols = {'Business_Name'  : [],
           'Street_Address' : [],
           'Locality'       : [],
           'Region'         : [],
           'Zipcode'        : [],
           'Contact'        : [],
           'Website'        : [],
           'Ratings'        : []
           }
   """            

   #initialisation() 
   for i in range(1,limit + 1): 
   		url1 = base_url + '&page=' + str(i) 
   		print 'processing:', url1  
   		soup = get_url_parsed(url1)
   		data = get_url_data(soup)
   		

   return data
 
# Parsing the URL using beautiful soup   		
def get_url_parsed(url1):   
#This is the dacomment in ipython
   buty = url.urlopen(url1).read()
   soup = ''
   soup = bs4.BeautifulSoup(buty) 
   return soup

# get the data from URL
def get_url_data(soup):   
   g_data = soup.find_all("div",{"class":"info"})
   
   
   for item in g_data:
      i = 0
      try :
         cols['Business_Name'].append(item.contents[0].find_all("a",{"class":"business-name"})[0].text.encode('ascii', 'ignore') )    #Business Name
      except :
            cols['Business_Name'].append(' ') 
      pass
      
      try :  
         cols['Street_Address'].append(item.contents[1].find_all("span",{"itemprop":"streetAddress"})[0].text.encode('ascii', 'ignore') )  #street Address 
      except :
            cols['Street_Address'].append(' ') 
      pass
      
      try :
         cols['Locality'].append(item.contents[1].find_all("span")[2].text.replace(',','').encode('ascii', 'ignore') )  #locality 
      except :
         cols['Locality'].append(' ')
      pass
          
      try :
         cols['Region'].append(item.contents[1].find_all("span")[3].text.encode('ascii', 'ignore') )  #AddressRegion
      except :
         cols['Region'].append(' ')
      pass
          
      try :
         cols['Zipcode'].append(item.contents[1].find_all("span")[4].text.encode('ascii', 'ignore') )  #PostalCode zipcode
      except :
         cols['Zipcode'].append(' ')
      pass
      
      try :
         cols['Contact'].append(item.contents[1].find_all("div",{"itemprop":"telephone"})[0].text.encode('ascii', 'ignore')) #phones number
         #cols['Contact'].append(item.contents[1].find_all("div",{"itemprop":"telephone"})[0].text.encode('ascii', 'ignore'))
      except :
         cols['Contact'].append(' ') 
      pass
          
      try :
         cols['Website'].append(item.contents[2].find('a', attrs={'href': re.compile("^http://")}).get('href').encode('ascii', 'ignore') )#store website links
      except :
         cols['Website'].append(' ') 
      pass
      
      #print cols
         
      try : 
         classes = item.contents[1].find('div', {'class':"result-rating"})
         rating  = (classes.get('class')[1] + ' ' + classes.get('class')[2]).strip()
         for key, value in number.items():
            if  key == rating :
             cols['Ratings'].append(value)
                  
      except :
          cols['Ratings'].append(' ')
      pass
  	  
   return cols   

  
#This class will handles any incoming request from the browser
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
  def do_GET(self):
   
   if self.path.startswith("/scrap"):
      o = urlparse.urlparse(self.path)
      getvars = urlparse.parse_qs(o.query)
      try:
      	self.send_response(200)
      	self.send_header('Content-type','application/json')
        self.end_headers()
      
        #Inputs
        search_term  = str( getvars['fi'][0]) # input Food item to search 
        geo_location = str( getvars['gl'][0]) # input loaction to search
        num_pages    = int( getvars['p'][0])  # input number of pages to scrap
      
      	base_url = 'http://www.yellowpages.com/search?search_terms='#pizza&geo_location_terms=los'
        base_url = base_url + search_term + '&geo_location_terms=' + geo_location 
        print base_url
      
        data1 = get_url_build(base_url,num_pages)
        self.wfile.write( json.dumps( data1 ) )
    	return
      except:
        e = sys.exc_info()[0]
        self.send_error(404,'Error, provide a and b parameters' + str(e) + str(getvars.keys()))
        return
                  
                    
if __name__ == "__main__":
  try:
	  #Create a web server and define the handler to manage the
	  #incoming request
	  server = HTTPServer(('', PORT_NUMBER), myHandler)
	  print 'Started httpserver on port ' , PORT_NUMBER
	  
    #Wait forever for incoming http requests
	  # Intitialisation of python dictionaries
    number = {'one':1,
                'one half':1.5, 
                'two':2,
                'two half':2.5,
                'three':3,
                'three half':3.5,
                'four':4,
                'four half':4.5,
                'five':5,
                'five half':5.5} 


	  cols = {'Business_Name'  : [],
              'Street_Address' : [],
              'Locality'       : [],
              'Region'         : [],
              'Zipcode'        : [],
              'Contact'        : [],
              'Website'        : [],
              'Ratings'        : []
             }
      #print cols

	  server.serve_forever()

  except KeyboardInterrupt:
	  print '^C received, shutting down the web server'
	  server.socket.close()
