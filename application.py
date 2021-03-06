from flask import Flask,render_template,request,redirect
app = Flask(__name__)

app.vars={}

@app.route('/',methods=['GET','POST'])
def index():
    # this is a comment, just like in Python
    # note that the function name and the route argument
    # do not need to be the same.
    if request.method == 'GET':  
        return render_template('homepage.html')
    else:
        return redirect('/next')
    #return render_template('layout_lulu.html', num=1,question='How many eyes do you have?', ans1='1',ans2='2',ans3='3')




@app.route('/next',methods=['GET','POST'])
def next():
    if request.method == 'GET':
           return render_template('1st.html')
    else:
        return redirect('/next2')


@app.route('/next2',methods=['GET','POST'])
def next2():
    if request.method == 'GET':
        return render_template('2nd.html')
    else:
        return redirect('/next3')


@app.route('/next3',methods=['GET','POST'])
def next3():
    if request.method == 'GET':
        return render_template('3rd.html')
    else:
        return redirect('/next4')


@app.route('/next4',methods=['GET','POST'])
def next4():
    if request.method == 'GET':
        return render_template('4th.html')
    else:
        return redirect('/next5')

@app.route('/next5',methods=['GET','POST'])
def next5():
    if request.method == 'GET':
        return render_template('5th.html')
    else:
        return redirect('/next6')

@app.route('/next6',methods=['GET','POST'])
def next6():
    if request.method == 'GET':
        return render_template('6th.html')
    else:
        return redirect('/next7')

@app.route('/next7',methods=['GET'])
def next7():
    if request.method == 'GET':
        return render_template('end.html')

#################
## Important: I have separated /next_lulu into GET and POST
## you can also do this in one function with IF and Else
## the attribute that contains GET and POST is request.method
###################


#@app.route('/usefulfunction_lulu',methods=['GET','POST'])
#def usefulfunction_lulu():
#    return render_template('end_lulu.html')
#return render_template('layout_lulu.html',num=1,question='Which fruit do you like best?',ans1='banana',ans2='mango',ans3='pineapple')

if __name__ == '__main__':
    app.run()
