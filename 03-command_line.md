# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> >  ls: looks at the folder you are in, and then "lists" the files and folders inside
pwd: "print working directory", outputs name of the directory you are currently in
cd: "change directory" 
touch: creates a new file inside the working directory
ls -a: modifies the behavior of ls, can see hidden files
cp: command copies files or directories
mv: moving a file, mv superman.txt superhero/
rm: remove one directory, rm -r removes directories
echo "Hello" > hello.txt: Redirects the standard output to a file
cat: view the output data of a .txt 
sort: takes the standard input and orders it alphabetically for the standard outputs
    sort deserts.txt | uniq
uniq: stands for "unique" and filters out adjacent, duplicate lines in a file
grep -R: searches all files in a directory and outputs filenames and lines containing matched results. 
sed: "stream editor". Accepts standard input and modifies it based on an expression, before displaying it as output data. 's/snow/rain/': s stands for substituion, snow the search string, the text to find, rain is the replacement string, the text to add in place



---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`: Looks at folder you are in and then lists all files
`ls -a`  : lists all contents, including hidden files and directories
`ls -l`  : lists all content of a directory in long format
`ls -lh` : shows sizes of human readable format 
`ls -lah`  : shows sizes of all files including hidden
`ls -t`  : order files and directories by the time they were last modified
`ls -Glp`  : gives same output as -lah?

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -R: display subdirectories as well
ls - u: Display files by the file access time
ls -g: displays the long format listing, but exclude owner name
ls -1: Displays each entry on a line
ls -t: displays newest files first

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > 
xargs reads items from the standard input, delimited by blanks or newlines, and executes the command one or more times with any initial-arguments followed by items read from standard input.
You can find .bak files in or below the current directory and delete them
$ find . -name "*.bak" -type f -print | xargs /bin/rm -f

 

