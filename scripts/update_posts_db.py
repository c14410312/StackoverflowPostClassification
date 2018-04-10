import psycopg2
import pandas as pd

#connect to the psql database
conn = psycopg2.connect(database="quiz_posts", user="dbutler", password="password", host="127.0.0.1", port="5432")

#print("Open database successful")

#once connected, iterate over each row in csv file and insert it into
#the database.

df = pd.read_csv('../data/java_questions_including_topics.csv')

cur = conn.cursor() #creates a curser required to insert 

#for each row in the dataframe
for index, row in df.iterrows():
    
    postId = df.loc[index, 'Id']#get ID for post
    title = df.loc[index, 'Title']
    body = df.loc[index, 'Body']
    tags = df.loc[index, 'Tags'].split()
    answer = df.loc[index, 'body']
    try:
        topic = int(df.loc[index, 'Topic'])
    except ValueError:
        topic = -1
    cur.execute('insert into posts (id, title, body, tags, answer, topic) values (%s, %s, %s, %s, %s, %s)', (int(postId), title, body, [tags], answer, topic))

conn.commit()
print("records successfully updated")
conn.close()

    

