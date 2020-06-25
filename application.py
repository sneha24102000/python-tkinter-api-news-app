from tkinter import *
import requests
#pip install requests

class News:
	def __init__(self):
		self.root =Tk()

		self.root.title("News Application")
		self.root.minsize(1000, 600)
		self.root.maxsize(1000, 600)

		self.root.configure(background="cyan")

		self.label = Label(self.root, text="Apnanewz 24*7", bg="cyan")
		self.label.configure(font=("Times", 30, "bold"))
		self.label.pack(pady=(30, 30))

		self.label1 = Label(self.root, text="Enter the topic", bg="cyan")
		self.label1.configure(font=("Times", 15, "italic"))
		self.label1.pack(pady=(10, 20))


		self.topic = Entry(self.root)
		self.topic.pack(pady=(5, 10), ipadx=30, ipady=3)

		self.click = Button(self.root, text="Search", bg="#000", fg="#fff",command=lambda: self.fetch())
		self.click.pack(pady=(5, 10))

		self.root.mainloop()

	def fetch(self):
		# fetch the search
		term = self.topic.get()
		url = "https://newsapi.org/v2/everything?q={}&apiKey=1cdb329f317c4c2ab304ceda59bac177".format(term)
		# hit the api
		response = requests.get(url)
		self.response = response.json()
		#print(self.response)
		self.data=self.response['articles']
		self.extract()


	def extract(self, index=0):
		news=[]
		news.append(self.data[index]['title'])
		news.append(self.data[index]['source']['name'])
		news.append(self.data[index]['description'])

		self.clear()
		self.display(news, index=index)


	def display(self,news,index):
		title = Label(self.root,text=news[0],fg="#9B59B6",bg="cyan")
		title.pack(pady=(5,5),padx=(2, 2))

		source = Label(self.root, text=news[1], fg="#000", bg="cyan")
		source.pack(pady=(5,5),padx=(2, 2))


		desc = Label(self.root, text=news[2], fg="#000", bg="cyan")
		desc.pack(pady=(5,5),padx=(2, 2))


		frame=Frame(self.root)
		frame.pack()


		if index!=0:

			previous=Button(frame, text="Previous",command=lambda: self.extract(index=index-1))
			previous.pack(side="left")
		if index!=19:
			next=Button(frame, text="Next",command=lambda: self.extract(index=index+1))
			next.pack(side="right")





	def clear(self):
		for i in self.root.pack_slaves():
			i.destroy()



obj=News()