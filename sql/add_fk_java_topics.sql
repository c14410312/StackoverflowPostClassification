ALTER TABLE posts
ADD CONSTRAINT java_topic_fk FOREIGN KEY (topic)
REFERENCES java_topics(id);
