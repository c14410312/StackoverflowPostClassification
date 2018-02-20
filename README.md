# Post classification Experiment using Scikit learn

* Date 20/02/18
* Dylan Butler

## Task
The overall task of this experiment is to create a trained classifier to correctly classify whether or not a post is useful for quizes and knowledge testing of Java core concepts.

## Data
The data for this experiment consists of a manually labelled dataset of 1500 stackoverflow posts. These posts have been filtered according to the following characteristics:

* They posses the structure of either a "how-to"(procedural intent) or a "why"(casual intent) type of question
* They have a minimum score of 7 (post score)
* They have not been deleted
* They have not been closed
* They have an accepted answer

After extracting this data I conducted an analysis on the resulting dataset to gain a deeper understanding of the data:

### Extracted Data insights
* Group 1 (useful for quizzes):
    * How to split a string in Java?
    * Read and convert an input stream to a string?
    * How to read all files in a folder in Java?
    * How to round a number to n decimal places in Java?
    * How to parse JSON in Java?
    * How do I declare and initialize an array in Java?
    * Why is it faster to process an unsorted array vs a sorted array
    * How do I compare strings in Java?
* Group 2 (not useful fr quizzes):
    * How do I fix android.os.NetworkOnMainThreadException?
    * How do you assert that a certain exception is thrown in JUnit 4 tests?
    * How to fix java.lang.UnsupportedClassVersionError: Unsupported major.minor version
    * How to add local jar files to a Maven project?
    * How do I set up IntelliJ IDEA for Android applications?
    * How does autowiring work in Spring?
    * How do I tell Maven to use the latest version of a dependency?
    * Unfortunately MyApp has stopped. How can I solve this?
    * Why is subtracting these two times (in 1927) giving a strange result?

### Key Findings
* Useless Q's
    * A key difference I can spot is that most of the questions that pose no use are environment, framework, related and focus on a technology that uses Java.
    * Verbs like; set-up, fix, stopped ... i.e. less java specific and more generic - used in everyday language. 
* Useful Q's
    * The useful questions seem to be following a pattern in which the main words in the questions (split, string, read, java, JSON, declare, initialize) are all words closely related to Java and programming concepts in general.  
    * The verbs/action words used in the useful q's are closely associated with java itself.
    
    
# Experiment Process

1. Chunk tags and titles and bodies into a single body
    * eliminate code snippets 
    * remove stop words
    * lemmatise each body
2. Extract the core features from the text that the algorithm can learn from
3. Train a classifier
4. Evaluate
5. Improve results
