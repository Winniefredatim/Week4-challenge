import click
import requests

# the apikey you got from newsapi.org
API_KEY = '6c3837a119744444a98c5eacb182ef75'

@click.group()
def main():
        pass

@main.command()

def listsources():
	""" Lists 4 sources from the API """
	main_url = " https://newsapi.org/v2/sources?apiKey=6c3837a119744444a98c5eacb182ef75"
 
	open_source = requests.get(main_url).json() 

	source = open_source['sources'] 
 
	results = [] 
	
	for article in source: 
                results.append(article["id"])
            
   	
	for i in results[0:5]:
            print(i)	


@main.command()
def topheadlines():
          """ Please enter your choice from the listsources """
          newsSource = click.prompt("Please enter your choice from listsources")
    
          main_url = "https://newsapi.org/v2/top-headlines?apiKey=newsSource6c3837a119744444a98c5eacb182ef75="+newsSource

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
