from jinja2 import Environment, FileSystemLoader
import mysql.connector
def read_file(filename:str)->str: # read file from disk
    filename = 'static/' + filename
    with open(filename,mode='r') as my_file:
        contents =  my_file.read()
    return contents

def read_sql(filename:str)->str: # read SQL file from disk
    filename = 'static/sql/' + filename
    with open(filename,mode='r') as my_file:
        contents =  my_file.read()
    return contents
def connect_to_database(dictionary = True,raw = False):
    try:
        # Устанавливаем соединение с базой данных
        conn = mysql.connector.connect(
            host="******",
            user="******",
            password="*******",
            database="******"
        )
        
        # Создаем курсор
        # cursor = conn.cursor()
        cursor = conn.cursor(dictionary=dictionary,raw=raw)
        return conn, cursor, None
    except Exception as e:
        print(f"Ошибка при подключении к базе данных: {str(e)}")
        return None, None,str(e)



def shortcut_render(template_filename:str,**params)->str:
    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template(template_filename)
    return tmpl.render(params)  
     