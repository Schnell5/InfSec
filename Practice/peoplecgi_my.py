import cgi
import html
import shelve
import sys
import os


shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'pay', 'job')

form = cgi.FieldStorage()
print('Content-type: text/html')
if not os.getcwd() in sys.path:
    sys.path.insert(0, os.getcwd())

replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method=POST action="peoplecgi_my.py">
    <table>
    <tr><th>key<td><input type=text name=key value="{key}">
    $ROWS$
    </table>
    <p>
    <input type=submit value="Fetch", name=action>
    <input type=submit value="Update", name=action>
</form>
</body>
</html>
"""

rowhtml = '<tr><th>{0}<td><input type=text name={1} value="{{{2}}}">\n'
rowshtml = ''

for fieldname in fieldnames:
    rowshtml += (rowhtml.format(*((fieldname,) * 3)))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)


def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:
        value = new[field]
        new[field] = html.escape(repr(value))
    return new


def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__
        fields['key'] = key
    except Exception:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields


def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]
        else:
            from person import Person
            record = Person(name='?', age='?')
        for field in fieldnames:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields


db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')
    fields['key'] = 'Missing or invalid action!'
db.close()
print(replyhtml.format(**htmlize(fields)))

