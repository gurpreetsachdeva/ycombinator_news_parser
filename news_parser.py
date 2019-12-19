#Why going for parse approach, when you have an api for this ?  Ans : Asked in Question

import requests
import sys
 
class Post:
    def __init__(self,title,author,comments_count,rank):
        self.title=title
        self.author=author
        self.comments_count=comments_count
        self.rank=rank
    def __repr__(self):
        return (self.rank +"    "+self.title+"    "+self.author+"    "+str(self.comments_count))
class Author:
    def __init__(self,name,karma):
        self.name=name
        self.karma=karma
def parseSite(posts,authors):
    url="https://news.ycombinator.com/news?p="
    page_no=1
    text="<tr class='athing'"
    css_class="<tr class='athing'"
    while(text.find(css_class)!=-1 ):
        print("Started Parsing Page No "+str(page_no))
        page_url=url+str(page_no)
        resp=requests.get(page_url)
        if resp.status_code!=200:
            break
        else:
            text=resp.text
            parsePosts(text,posts,authors)
        page_no=page_no+1
    return posts
        
def parsePosts(text,posts,authors):
        css_class="<tr class='athing'"
        while(text.find(css_class)!=-1):
            text=text[text.find(css_class)+len(css_class):len(text)]
            row=text[0:text.find(css_class)]
            post=extractRow(row)
            
            posts.append(post)
            author=getAuthorKarmaFromName(post.author)
            authors[post.author]=author.karma
        return posts
def extractRow(row):
    #print("*******")
    title=""
    author=""
    comments_count=0
    rank=0
    if row.find("class=\"rank\"")!=-1:
        row=row[row.find("class=\"rank\""):len(row)]
        rank=row[row.find(">")+1:row.find(".</span>")]
    else:
        print("Title Blank")
    
    if row.find("class=\"storylink\"")!=-1:
        row=row[row.find("class=\"storylink\""):len(row)]
        title=row[row.find(">")+1:row.find("</a>")]
    else:
        print("Title Blank")
    if row.find("user?id=")!=-1:
        row=row[row.find("user?id=")+len("user?id="):len(row)]
        author=row[0:row.find("\"")]
    else:
        print("Author Blank For a row")
    
    if row.find("hide</a>")!=-1 and row.find("comment")!=-1:
        row=row[row.find("hide</a>")+len("hide</a>")+1:len(row)]
        comments_count=row[row.find(">")+1:row.find("&nbsp;comment")]
        comments_count=int(comments_count)
    else:
        print("Comment count Blank For a row")
    print(rank,title,author,comments_count)
    return Post(title, author, comments_count,rank)
        

def parseTopPage(resp):
    text=resp.text
    if text.find("karma")==-1:
        return 0
    text=text[text.find("karma:</td><td>")+len("karma:</td><td>"):len(text)]
    text=text[0:text.find("</td></tr>")]
    return int(text)
    
def getAuthorKarmaFromName(name):
    url="https://news.ycombinator.com/user?id="+name
    resp=requests.get(url)
    if name=="":
        return Author(name,0)
    if  resp.status_code!=200:
        #print("Inside Blank Name for author or Response Code not 200")
        #return Author("",0)
        #Get Through the API, URL Fetch is failing
        r=requests.get("https://hacker-news.firebaseio.com/v0/user/"+name+"/karma.json")
        return Author(name,int(r.text))
    author=Author(name,parseTopPage(resp))
    return author

#Single Author
def getTopRatedAuthor(authors):
    l=getTopRatedAuthors(authors)
    if(len(l)!=0):
        print("Top Rated Author *************************")
        print(l[0])
        return l[0]
    else:
        print("No Top Rated Author")
        
#Multiple Authors
def getTopRatedAuthors(authors):
    l=authors.items()
    l=sorted(l,key=lambda x:x[1],reverse=True)
    printPretty(l)
    return l
def getPostByComments(posts):
    ans=sorted(posts,key=lambda x:x.comments_count,reverse=True)
    printPretty(ans)
    return ans
def printPretty(posts):
    print("\n".join(map(str,posts)))
    
posts=[]
authors={}
parseSite(posts,authors)
if sys.argv[1]=="get_top_rated_author":
    print("Top Rated Author \n")
    getTopRatedAuthor(authors)
elif sys.argv[1]=="sort_by_comments":
    print("Enter Sort By Comments Output \n")
    getPostByComments(posts)
else:
    print("Top Rated Authors\n")
    getTopRatedAuthors(authors)

    
    



  
    

    
