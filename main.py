from flask import Flask,request,jsonify
import Scrape_flight

app=Flask(__name__)

@app.route('/Search',methods = ['POST'])
#mailing process
def find():
        try:
            dict_file = request.get_json()
            F_no = dict_file["flight_no"]
            data=Scrape_flight.search(F_no)
            return data
                 
        except Exception as e:
             return jsonify({'message' :'Error - Unable to search flight'})

if __name__=='__main__':
    app.run(debug=True)