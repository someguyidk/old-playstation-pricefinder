from flask import Flask, render_template, request, session
from bs4 import BeautifulSoup
import requests
import socket

app = Flask(__name__)

@app.route('/')
def index():
	price_limit = request.form.get("price_limit")
	prices = []
	games = []
	dictionary = {"prices":prices,"games":games}
	for i in ['1','2']:
		url = requests.get(f"https://store.playstation.com/es-mx/browse/{i} ").text
		soup = BeautifulSoup(url,'lxml')
		#prices = soup.find_all(class_='price-display__price').text
		#print('\n' + 'Amount ofGames under 15$: '+ str(len(prices)))
		for cell in soup.find_all(class_='grid-cell grid-cell--game'):
			try:
				price = cell.find(class_='price-display__price').text
				game = cell.find(class_='grid-cell__title').text
			except Exception:
				price = 'free'
		
			if price == 'free' or float(price.split('$')[1]) < float(below):
				prices.append(price)
				games.append(game)
		

		return render_template('extended_index.html',dict=dictionary,prices=prices,games=games)


if __name__ == "__main__":

	 app.run(debug=True)