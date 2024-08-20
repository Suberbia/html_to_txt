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
        
        text_element = message.find('div', class_='text')
        media_element = message.find('div', class_='media_wrap')

        if media_element:
            title_element = media_element.find('div', class_='title bold')
            description_element = media_element.find('div', class_='description')
            status_element = media_element.find('div', class_='status details')

            if title_element and description_element and status_element:
                media_title = title_element.text.strip()
                media_description = description_element.text.strip()
                media_status = status_element.text.strip()
                text = f"Media: {media_title} - {media_description} ({media_status})"
            else:
                continue  # Skip if media details are incomplete
        elif text_element:
            text = text_element.text.strip()
        else:
            continue  # Skip messages without text or media information

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
input('press enter to exit')
