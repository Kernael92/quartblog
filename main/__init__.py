from quart import Quart 
from app.dsatabase import DB  

async def create_app(config):
    app = Quart(__name__)
    DB.init()
    register_blueprints(app)
    for title, text in ['post1', 'post2', 'post3']:
        new_post = Post(title=title, text=text)
        new_post.insert()
    return app 

async def register_blueprints(app):

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)