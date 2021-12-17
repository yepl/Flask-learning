from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return u'Welcome to My Watchlist!<br>欢迎来到我的 Watchlist！'+'<br><h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
    # u指以unicode方式输出，加<br>标签换行

from flask import escape,url_for
@app.route('/user/<name>')
def user_page(name):
    return 'User: %s' % escape(name)

#修改视图函数名url_for,生成访问链接，见终端输出结果
@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('user_page', name='greyli'))  # 输出：/user/greyli
    print(url_for('user_page', name='peter'))  # 输出：/user/peter
    print(url_for('test_url_for'))  # 输出：/test
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test?num=2
    #return 'Test page'
    #return str(url_for('test_url_for', num=2))
    return url_for('test_url_for', num=2)

@app.route('/list/')
def list():
    return url_for('user_page',name='tom',vid=7)