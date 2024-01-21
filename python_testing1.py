# Necessary Imports
from fastapi import FastAPI                 # The main FastAPI import
from fastapi.responses import Response      # Used for returning responses
import uvicorn                              # Used for running the app

# Configuration
app = FastAPI()               # Specify the "app" that will run the routing

# Example route: return a simple static webpage
@app.get("/", response_class=Response)
def get_hello() -> Response:
  return Response(content="Hello, World!", media_type="text/html")

# Running the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6543, --reload = True)


#check for valid inputs
#how do I do dict
    def average(a_list):
        sum = 0
        counter = 1
        if len(a_list) == 0:
            return None
        else:
            for x in a_list:
                if (type(x)!=int) or (type(x) != float): 
                    return None
                else:
                    sum = sum+x
                    counter= counter +1
            return sum/counter
      
    // adict= { }
   // adict['word'] =  20


    //syntax of variable length?
//