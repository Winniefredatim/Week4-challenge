import click
import requests

# the apikey you got from newsapi.org
API_KEY = '6c3837a119744444a98c5eacb182ef75'

@click.group()
def main():
        pass


@main.command()
def listsources():
	""" Lists 4 sources from the top headlines """
	main_url = "https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=6c3837a119744444a98c5eacb182ef75"
 
	open_source = requests.get(main_url)
	print("Status code:", open_source.status_code)

	source_dict = open_source.json()
	articles =source_dict['articles']
	print(source_dict.keys())
 
def getheadlines():
    print("You are Welcome to your favourite news sites")
    print('-' * 50)
    print("Below is a list of sources you may chose from")
    print("1.The Next Web")
    print("2.The Guardian (AU)")
    print("3.Medical New Todays")
    print("4.MTV News")
    print('-' * 50)
    news_source =input(str("Enter News Source Number \t"))
    print ('\n')

    if(news_source=='1'):
        print("\t\t\t The Next Web HeadLines")
        abcnews_request = requests.get(
            "https://newsapi.org/v2/top-headlines?sources=the-next-web&apiKey=45d024f423f94974a94342bc7b1d6fd6")
        source_dict = thenewsweb_request.json()
        articles =source_dict['articles']

        for article in source_dict[:10] :
            click.echo(click.style('TITLE: ' + article['title'], fg='blue'))
            click.echo(click.style('BY: ' + article['author'], fg='black'))
            click.echo('\n')
            click.echo(click.wrap_text(article['description'], 100))
            click.echo('\n')
            click.echo('-' * 90)
    elif(news_source=='2'):
        print("\t\t\t The Guardian (AU) HeadLines")
        abcnews_request = requests.get(
            "https://newsapi.org/v2/top-headlines?sources=the-guardian-au&apiKey=6c3837a119744444a98c5eacb182ef75")
        source_dict = theguardian_request.json()
        articles =source_dict['articles']

        for article in source_dict[:10] :
            click.echo(click.style('TITLE: ' + article['title'], fg='yellow'))
            click.echo(click.style('BY: ' + article['author'], fg='black'))
            click.echo('\n')
            click.echo(click.wrap_text(article['description'], 100))
            click.echo('\n')
            click.echo('-' * 90)
    elif(news_source=='3'):
        print("\t\t\t Medical News Today HeadLines")
        abcnews_request = requests.get(
            "https://newsapi.org/v2/top-headlines?sources=medical-news-today&apiKey=6c3837a119744444a98c5eacb182ef75")
        source_dict = medicalnewstoday_request.json()
        articles =source_dict['articles']

        for article in source_dict[:10] :
            click.echo(click.style('TITLE: ' + article['title'], fg='blue'))
            click.echo(click.style('BY: ' + article['author'], fg='black'))
            click.echo('\n')
            click.echo(click.wrap_text(article['description'], 100))
            click.echo('\n')
            click.echo('-' * 90)
    elif(news_source=='4'):
        print("\t\t\t MTV News HeadLines")
        abcnews_request = requests.get(
            "https://newsapi.org/v2/top-headlines?sources=mtv-news&apiKey=6c3837a119744444a98c5eacb182ef75")
        source_dict = abcnews_request.json()
        articles =source_dict['articles']

        for article in source_dict[:10] :
            click.echo(click.style('TITLE: ' + article['title'], fg='blue'))
            click.echo(click.style('BY: ' + article['author'], fg='black'))
            click.echo('\n')
            click.echo(click.wrap_text(article['description'], 100))
            click.echo('\n')
            click.echo('-' * 90)
    else:
        print("Please Select value within the range")           


@main.command()
def topheadlines():
          """ Please enter your choice from the listsources """
          newsSource = click.prompt("Please enter your choice from listsources")
    
          main_url = "https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=6c3837a119744444a98c5eacb182ef75"+newsSource

	# fetching data in json format 
          open_headline = requests.get(main_url).json() 

	# getting all headlines in a string articles 
          headline = open_headline["articles"] 

	# empty list which will 
	# contain all trending newssources 
          output = [] 
	
          for word in headline: 
                click.echo('\n')
                click.echo(click.style('TITLE: ' + word['title'], fg='blue'))
                click.echo(click.wrap_text(h['description']))
                click.echo(click.style('DOMAIN: ' + word['url'], fg='green'))
           
           	
          for i in output[:10]:
                print(i)


if __name__ == '__main__':
	main()
