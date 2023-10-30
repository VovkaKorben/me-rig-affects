import io
import traceback
import mysql.connector
import mytools
import mysolution
from flask import (
    Flask,
    make_response,
    redirect,
    request,
    render_template,
    jsonify,
    url_for,
    render_template_string
)
app = Flask(__name__)

"""
def make_table():

    def recurse(parentID, level):
        log_file = 'C:/EVE_WM/nc/market_logs/ok.txt'

        def log2file(s):
            print(s)
            with open(log_file,mode='a', encoding='utf-8') as my_file:
                my_file.write(s+'\n')
    
        if parentID == None:
            q = 'is null'
        else:
            q = '= {}'.format(parentID)
        
        s = sqls.format(q) 
        cursor.execute(s)
        res = cursor.fetchall()  
        
        
        for q in res:
            cursor.execute(sqli,(q['marketGroupID'],q['parentGroupID'],q['marketGroupName'],q['description'],level,))
            cursor.execute('commit;')
            recurse(q['marketGroupID'], level+1)
            
    conn, cursor, mysqlerror = mytools.connect_to_database()
    if mysqlerror!=None:
        print(mysqlerror)
        exit
    cursor.execute('delete from `!tmp_market`;')
    cursor.execute('commit;')

    level = 0
    sqls = 'select * from invmarketgroups  where parentGroupID {} order by marketGroupName;'
    sqli = 'insert into `!tmp_market` (`marketGroupID`,`parentGroupID`,`marketGroupName`,`description`,`level`) values (%s,%s,%s,%s,%s);'
    recurse(2, 0)
"""
@app.route('/')
def me_check(): 

    def recurse(groupID,level,inherit,parents):
        nonlocal html
        if groupID == None:
            q = 'is null'
        else:
            q = '= {}'.format(groupID)
        sqls = 'select * from me_prepare  where parent {} order by name;'
        sqls = sqls.format(q)
        cursor.execute(sqls)
        mr = cursor.fetchall()
        inherit_store = inherit
        # if len(mr)>0:
        for r in mr:
            # inherit_copy = inherit
            if r['me_group'] != None:
                inherit = r['me_group']
            
            html += mytools.shortcut_render('me_test_row.html',
                    id = r['id'],
                    name = r['name'],
                    level = level,
                    parents =  ' -> '.join(parents),
                    inherit = inherit,
                    vocab = vocab)    
            
            parents_copy = parents.copy()         
            parents_copy.append(r['name'])
            recurse(r['id'],level+1,inherit,parents_copy)
            inherit = inherit_store

    conn, cursor, mysqlerror = mytools.connect_to_database()
    if mysqlerror!=None:
        print(mysqlerror)
        exit
    
    vocab = {}
    cursor.execute('select * from me_groups;')
    for x in cursor.fetchall():
        vocab[x['groupID']] = x['description']
    
    
    html = ''
    recurse(2,0,None,[])
    
    

    # expand dict
    return mytools.shortcut_render('me_test_index.html',rows = html)

def make_groups():
    
    def get_group_me(group):
        r = None
        while True:
            cursor.execute(sql_bp_info,(group,))       
            bpinfo = cursor.fetchall()
            # print(bpinfo)
            if len(bpinfo)==0:
                return None
            bpinfo = bpinfo[0]
            if bpinfo['me_group'] != None:
                return bpinfo['me_group']
            group = bpinfo['parent']
            

    conn, cursor, mysqlerror = mytools.connect_to_database()
    if mysqlerror!=None:
        print(mysqlerror)
        exit
    
    with open('C:/EVE_WM/deploy/me/get_list.sql',mode='r') as my_file:
        sql_get_list =  my_file.read()
    with open('C:/EVE_WM/deploy/me/get_bp_info.sql',mode='r') as my_file:
        sql_bp_info =  my_file.read()
    with open('C:/EVE_WM/deploy/me/update_me_group.sql',mode='r') as my_file:
        sql_update =  my_file.read()

    cursor.execute(sql_get_list)
    for bp in cursor.fetchall():
        # print(bp)
        bpID = bp['bpID']
        gi = get_group_me(bp['marketID'])
        if gi==0 or gi is None:
            print('`{}` has group: {}'.format(bp['bpName'],gi))
        cursor.execute(sql_update,(gi,bp['bpID']))
        cursor.execute('commit;')
        
# make_groups()
