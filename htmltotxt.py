from bs4 import BeautifulSoup

def transform_html_to_whatsapp(html_file):
    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract chat messages
    messages = soup.find_all('div', class_='message')

    # Transform messages to WhatsApp format
    whatsapp_chat = ''
    for message in messages:
        sender_element = message.find('div', class_='from_name')
        if sender_element is None:
            continue  # Skip messages without sender information

        sender = sender_element.text.strip()
        timestamp_div = message.find('div', class_="pull_right date details")
        if timestamp_div:
            timestamp = timestamp_div['title']
            date_str = timestamp[:10]
            time_str = timestamp[11:19]
        else:
            date_str, time_str = None, None

        text = message.find('div', class_='text').text.strip()

        # Format message in WhatsApp format
        if time_str:
            whatsapp_message = f'[{date_str}, {time_str}] {sender}: {text}\n'
            whatsapp_chat += whatsapp_message

    # Save the transformed chat to a file
    with open('_chat.txt', 'w', encoding='utf-8') as file:
        file.write(whatsapp_chat)

    print('Transformation complete. The WhatsApp chat export is saved as _chat.txt')

# Usage example
transform_html_to_whatsapp('messages.html')
