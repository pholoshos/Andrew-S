from chatterbot.trainers import ListTrainer
from chatterbot.trainers import UbuntuCorpusTrainer
from chatterbot import ChatBot
from flask import Flask
from flask import request,render_template
app = Flask(__name__)

chatbot = ChatBot('Example Bot')
message = "he"
response = "hello"
climateChange = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6'
]


def start():
    return "welcome"

trainer = ListTrainer(chatbot)

trainer.train([
    'what is your name?',
    'my name is andrew',
    'who are you?',
    'i am an AI chatbot made by pholosho seloane'
    'hello',
     start(),
    'hi',
    'hello'
    'How are you?',
    'I am good, how are you?.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
    'do you know pholosho?',
    'yes i do',
    'do you know any jokes?',
    'yes i do know a few jokes',
    'what is climate change?',
    climateChange[0],
    'Name a human activity that contributes to climate change.',
    climateChange[1],
    'Name three effects of climate change',
    climateChange[2],
    'How many people in the world are vulnerable to the effects of climate change?',
    climateChange[3],
    'If the global temperature rises by over 1.5°C what percentage of species will beat risk of extinction?',
    climateChange[4],
    'Which is the name of the gas that is responsible for 75 percent of the warming effectfrom greenhouse gases?',
    climateChange[5],
    




    
])

@app.route("/")
def hello_world():
  
  return render_template('index.html',message=message, response=response)

@app.route('/talk',methods=['POST','GET'])
def talk():
    if(request.method == 'POST'):
        question = request.form['message']
        response = chatbot.get_response(question)
        return render_template('index.html',message=question, response=response)



debug = True
host = '127.0.0.1'
port = 5000


app.run(host, port, debug)
#talk()