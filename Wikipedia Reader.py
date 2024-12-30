# Import the necessary modules for web scrapping.
import requests
from bs4 import BeautifulSoup as soup


# Start program with beautiful appearances.
print('\n\n')
print('* *  Wikipedia Reader  * *')

# Run the program in counter True while, so it can run again.
while True:
    # Get the url from the user to send the request.
    url = str(input('\n\nEnter URL: '))
    print('\n\nPlease wait...')

    # If the code gets an error, the "try except" can handle it.
    try:
        # Send counter get requests to receive some information from the web page.
        response = requests.get(url, timeout=7)

    # Check if the connection was too late, it will stop sending request and inform to the user.
    except requests.exceptions.ConnectTimeout:
        print("\n\n!!!  This site can’t be reached  !!!")

    # Check if the connection has an error, it will stop sending request and inform to the user.
    except requests.exceptions.ConnectionError:
        print('\n\n!!!  Connection failed, Check WiFi connection and try again  !!!')

    # Check if the url was invalid, it will stop sending request and inform to the user.
    except requests.exceptions.MissingSchema:
        print('\n\n!!!  Invalid URL  !!!')

    # Check if the connection has not any error, it will run the below codes.
    else:
        # If status code was 200(Ok), it will continue getting information from the web page to show the result.
        if response.status_code == 200:
            # Get the source code of the web page to get other information.
            source = soup(response.text, 'html.parser')
            # If the web page contains something like an article, it will get the title and headers.
            if source.find('h1') is not None:
                print(f'\n\n=>  {source.find("h1").text}  <=\n')
                exists = False
                for counter, heading in enumerate(source.find_all('h2')):
                    if heading.text == 'فهرست':
                        exists = True
                        continue
                    else:
                        num = counter if exists else counter + 1
                        print(f'    {heading.text[:heading.text.index("[ویرایش]")]} .{num}\n') if '[ویرایش]' in heading.text else print(f'    {num}. {heading.text}\n')
                print('\n\nFinished.')
            # If the web page does not contain an article,  "No result fount" will be displayed to the user.
            else:
                print('\n\n!!!  No result found from the page  !!!')
        # If the connection status code was not 200(ok), the status code without the main results will be displayed.
        else:
            print(f'\n\n!!!  Status Code: {response.status_code} ,  {response.reason}  !!!\n')

    # At the end of the program, it will ask the user to run again.
    finally:
        repeat = input('\n\nDo you want to run again? (y / n): ')
        if repeat in ['Y', 'y', 'Yes', 'yes', 'YES', 'YS', 'Ys', 'ys', '؛', 'غ', '؛ثس', 'غثس', '؛ٍُ', '؛ُ', '؛س', 'غس']:
            print('\n\n\n\n')
            continue
        else:
            print('\n\nOk.\n\n')
            break
