from flask import Flask, render_template, request, redirect, url_for, session,flash

from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"

# LOCAL
engine = create_engine('sqlite:///database.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()


@app.route('/', methods=['GET','POST'])
def home():
	if request.method=='GET':
		return render_template('index.html')
	else:
		g = (request.form['gender'])
		a = (request.form['age'])
		go = (request.form['goal'])
		act = (request.form['activity'])
		en = (request.form['env'])
		i = (request.form['intensity'])
		p = (request.form['preference'])
		Answers = Questions(
			gender = g,
			age = a,
			goal = go,
			activity = act,
			env = en,
			intensity = i,
			preference = p)
		session.add(Answers)
		print('added')
		session.commit()
		print('commited')

		if(Cal(Answers)=='p1'):
			return render_template('page1.html')
		elif(Cal(Answers)=='p2'):
			return render_template('page2.html')
		else:
			return render_template('page3.html')


@app.route('/page1')
def page1():
	return render_template('page1.html')

@app.route('/page2')
def page2():
	return render_template('page2.html')

@app.route('/page3')
def page3():
	return render_template('page3.html')

def Cal(q1):
	p1=0
	p2=0
	p3=0
	if(q1.goal == 'Lose weight'):
		p3+=1
	if(q1.goal == 'Gain weight'):
		p1+=1
	if(q1.goal == 'Stay the same weight'):
		p2+=1
	if(q1.activity == '3 days a week'):
		p1+=1
	if(q1.activity == '4 days a week'):
		p2+=1
	if(q1.activity == '5 days a week'):
		p3+=1
	if(q1.env == 'Inside'):
		p1+=1
	if(q1.env == 'Outside'):
		p2+=1
		p3+=1
	if(q1.intensity == 'Intense'):
		p2+=1
	if(q1.intensity == 'Moderete'):
		p1+=1
	if(q1.intensity == 'Easy'):
		p3+=1
	if(q1.preference == 'Weight lifting'):
		p1+=1
	if(q1.preference == 'Calisthenics'):
		p2+=1
	if(q1.preference == 'Cardio'):
		p3+=1

	highest_p = max(p1,p2,p3)
	if(p1 == highest_p):
		return "p1"
	elif(p2 == highest_p):
		return "p2"
	else:
		return "p3"


if __name__=='__main__':
	app.run(debug=True)