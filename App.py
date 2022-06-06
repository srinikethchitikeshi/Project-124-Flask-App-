from flask import Flask,jsonify,requests

App = Flask(__name__) 
@app.route("/")
def chs():
    return "Welcome"

contacts = [
    {
        "Contact":97******17
        "Name":luke
        "done":False
        "id":1
    }
    {
        "Contact":82******18
        "Name":rhodes
        "done":False
        "id":2
    }
]

@app.route("/Add-Data",methods = ["POST"])
def Addtask():
    if not request.json:
        return jsonify({
            "status":"Error",
            "message":"Please provide the data"
        },400)
    task = {
        'id':tasks[-1]['id']+1
        'Title':request.json['Title'],
        'Description':request.josn.get('Description',""),
        "done":False
    }

    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":'Contact added successfully'    
    })    

@app.route("/Get-Data")
def Gettask():    
    return jsonify({
        "data":tasks
    })

if(__name__ == "__main__"):
    app.run