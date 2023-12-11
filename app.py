import os
from turtle import title
import flask
from flask import send_from_directory, request
from googleapiclient.discovery import build
from newsdataapi import NewsDataApiClient
import random
from firebase_admin import credentials
from firebase_admin import firestore


# try:
#     cred = credentials.Certificate("firebase_key.json")
#     firebase_admin.initialize_app(cred)
    
#     print("No problems")
# except:
#     print("Something went wrong with database initialization")



app = flask.Flask(__name__)


#integration of the firebase
# def datapush(data):                 # pushing data to the firebase
#     db= firestore.client()
#     db.collection("test").add({"Hello":"There"})

# required for news api
def news_res():
    api = NewsDataApiClient(apikey="##")
    response = api.news_api(q="exams", country="in")
    
    arr=[]
    for j in range(0,3):
        i= random.randint(0,19)
        title = response['results'][i]['title']
        link = response['results'][i]['link']
        if j==2:
            arr.append(title +" "+link+" "+"Click Links to know more about it")
            break
        arr.append(title +" "+link+" ")

    if response['status'] == "success":
        i = 0
        return str(arr[0])+"\n"+str(arr[1])+"\n"+str(arr[2])
    else:
        return "Sorry failed to load. We are working on it."

# required for notes
def url_call_notes(dat) :
    if dat=='class 10' or dat=='10' or dat=="10th class":
        return str("This ought to help \n https://www.hsslive.in/2021/03/class-10-sslc-study-materials.html")
    elif dat=='class 11' or dat=='11' or dat=='11th class':
        return str("I hope this helps \n https://www.hsslive.in/p/higher-secondary-plus-oneclass-11-study.html")
    elif dat== 'class 12' or dat=='12' or '12th class':
        return str("Lets hope this works out well for you \n https://www.hsslive.in/p/academics.html")
    return "Sorry I have nothing for you"

# required for search query execution
def search_query(query):
    api_key ="##" # api key for google custom search api
    resource = build('customsearch','v1',developerKey=api_key).cse()
    result=""
    i=0
    res = resource.list(q=query,cx='d7e934f9ad8464e41').execute()
    for item in res['items']:
        i+=1
        result +=  item['title']+"\n"+item['snippet']+"\n"+item['link']+"\n"
        if i==5:
            break
    
    return str(result)

# required for the cost detail
def cost_college_state(search):
    import pandas as pd
    df = pd.DataFrame(pd.read_csv(r"sample_data - Universities.csv",encoding= 'unicode_escape'))
    df_dict= df.to_dict('records')
    ans= "Sl no."+"\t\t\t"+'Name of the University'+"\t\t\t"+'State'+"\t\t\t"+"Grade"
    i=0
    for row in df_dict:
        
        if str(search).casefold()==str(row['State']).casefold() :
            i+=1
            k=i
            ans+= "\n\n\n"+str(k)+".\t\t\t"+row['Name of the University']+"\t\t\t|"+row['State']+"\t\t\t|"+row['Grade']
            
    return ans


# required for proper webhook call
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/favicon.png')



# index page
@app.route('/')
# home page
@app.route('/home')
def home():
    return "This is your database"

# /webhook where all our requests and interactions take place


@app.route('/webhook', methods=['POST'])
def webhook():
 
    # loading the necessary json from dialogflow to the server
    data = request.get_json(force=True)
    # the required response from the server to the dialogflow
    if (data['queryResult']['intent']['displayName'] == 'Exam_news'):                   # condition for execution of intent 1
        news = news_res()

        return {
                "fulfillmentText": news
            }
        
    elif data['queryResult']['intent']['displayName']== 'Notes_hs' :                    # condition for execution of intent 2
        urls= url_call_notes(str(data['queryResult']["parameters"]["class"]))
        return {
            "fulfillmentText":  urls
                }

    elif data['queryResult']['intent']['displayName']== 'search_query' :                # condition for execution of intent 3
        top =  data['queryResult']['parameters']['Topic']
        top = top[1::]
        ser_res= search_query(top)
        #datapush(ser_res)
        print("Hello i am running")
        return {
                "fulfillmentText" : ser_res
               }
        
    elif data['queryResult']['intent']['displayName']== '' :       # condition for execution of intent 4
        reply= {
                'fulfillmentText' : "Hello"
                                                }
        return reply
    
    elif data['queryResult']['intent']['displayName']== 'College_fees' : 
        state =  data['queryResult']['parameters']['Inquiry']
        file_res= cost_college_state(state[1::])
        return {
            'fulfillmentText' : str(file_res)
        }
# main method
if __name__ == "__main__":
    app.secret_key = "ItsaSecret"
    app.run(debug=True, port=8000)
