# Import classes from your brand new package
from main import Bmw
from api import Audi
from scraper import Nissan
   
# Create an object of Bmw class & call its method
ModBMW = Bmw()
ModBMW.outModels()
   
# Create an object of Audi class & call its method
ModAudi = Audi()
ModAudi.outModels()
  
# Create an object of Nissan class & call its method
ModNissan = Nissan()
ModNissan.outModels()