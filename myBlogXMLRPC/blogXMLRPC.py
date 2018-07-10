from xmlrpc.server import SimpleXMLRPCServer
import hashlib
from datetime import datetime
import MySQLdb

user_name = 'liupengfei'
user_password = '123456'
BLOG_URL = 'localhost'
PORT = 8001

def get_user_blogs(key, username, password):

    if username == user_name and password == user_password :

        return [{'url': BLOG_URL, 'blogid': '123456', 'blogName': '多个领域'}]

    else:

        return '账号或密码错误'


def new_post(blogid, username, password, struct, publish):

    success = True

    author = '多个领域'
    title = struct['title']
    md5Obj = hashlib.md5()
    md5Obj.update(title.encode(encoding='utf-8'))
    identify = md5Obj.hexdigest()
    body = struct['description']
    # digest = body[0:100]
    addTime = datetime.now()
    category = struct['mt_keywords']

    db_connection = MySQLdb.connect(host='xxxxxx', port=xxxx, user='xxxxxx', passwd='xxxxxxx', db='xxxxxxx')
    db_cursor = db_connection.cursor()
    db_connection.set_character_set('utf8')
    db_cursor.execute('SET NAMES utf8;')
    db_cursor.execute('SET CHARACTER SET utf8;')
    db_cursor.execute('SET character_set_connection=utf8;')
    sql = "INSERT INTO dglyblog_blogmodel(author,title,identify,digest,body,add_time,category) VALUES('%s','%s','%s','%s','%s','%s','%s') " % (author,title,identify,'',body,addTime,category)
    try:
        db_cursor.execute(sql)
    except:
        success = False

    db_cursor.close()
    db_connection.commit()
    db_connection.close()

    print(success)

    return identify if success == True else ''


def get_post(postid, username, password):

    return {}


def edit_post(postid, username, password, struct, publish):

    success = True

    body = struct['description']
    identify = postid

    print(struct)
    print(postid)

    db_connection = MySQLdb.connect(host='xxxxxx', port=xxxx, user='xxxxxxx', passwd='xxxxxxxxx', db='xxxxxx')
    db_cursor = db_connection.cursor()
    db_connection.set_character_set('utf8')
    db_cursor.execute('SET NAMES utf8;')
    db_cursor.execute('SET CHARACTER SET utf8;')
    db_cursor.execute('SET character_set_connection=utf8;')
    sql = "UPDATE dglyblog_blogmodel SET body = '%s' WHERE identify = '%s' " % (body,identify)

    try:
        db_cursor.execute(sql)
    except:
        success = False

    db_cursor.close()
    db_connection.commit()
    db_connection.close()

    print(success)

    return success

def get_category(blogid, username, password):

    return {}

def main():
    server = SimpleXMLRPCServer(('localhost', PORT))
    server.register_introspection_functions()
    server.register_function(get_user_blogs, 'blogger.getUsersBlogs')
    server.register_function(new_post, 'metaWeblog.newPost')
    server.register_function(get_post, 'metaWeblog.getPost')
    server.register_function(edit_post, 'metaWeblog.editPost')
    server.register_function(get_category, 'metaWeblog.getCategories')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
