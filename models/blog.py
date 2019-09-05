from quart import Quart, render_template, request, redirect, url_for,session,jsonify
# for quart implementation
from pymongo import MongoClient
from pprint import pprint 
from bson import ObjectId
import asyncio
# For ObjectId to work


client = MongoClient('mongodb://localhost:27017/')
db = client.mongoblog 
blogs = db.blog

app = Quart(__name__)
app.secret_key = b'\xf9{\x16\xe8\x94\xd0\x97=\xb2wEVN\x8d\xcd\xb2'

@app.route('/', methods=['GET'])
async def posts():
    blogs_1 = blogs.find()

    return await render_template('post.html', blogs = blogs_1)

@app.route('/', methods=['POST'])
async def create():
    form = await request.form 
    
    
    blogs.insert_one()
    return redirect (url_for('posts'))


app.run(debug = True)