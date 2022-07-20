from bs4 import BeautifulSoup
import unidecode


# text = """"""

# text = BeautifulSoup(text, 'html.parser').get_text()
# text = unidecode.unidecode(text)



html_str = '''
<td><a href="http://www.fakewebsite.example">Please can you strip me?</a>
<br/><a href="http://www.fakewebsite.example">I am waiting....</a>
</td>
'''
soup = BeautifulSoup(html_str)

print(soup.get_text())