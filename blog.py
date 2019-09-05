from quart import Quart, render_template, request, redirect, url_for
# for quart implementation
from pymongo import MongoClient
from pprint import pprint 
from bson import ObjectId
# For ObjectId to work


client = MongoClient('mongodb://localhost:27017/')
db = client.mongoblog 
posts = db.post 

app = Quart(__name__)

@app.route('/', methods=['GET'])
async def posts():
    posts_1 = posts.find()
    return await render_template('post.html', posts = posts_1)

@app.route('/', methods=['POST'])
async def create():
    form = await request.form 
    title = request.values.get('title')
    text = request.values.get('text')
    posts.insert_many({ "title": title, "text": text})
    return redirect url_for('posts')


app.run(debug = True)