from bs4 import BeautifulSoup
import os

def process_html_file(file_path):
    """
    Reads a Telegram export HTML file and extracts all messages.

    Args:
        file_path (str): The path to the HTML file.

    Returns:
        list: A list of tuples, where each tuple represents a message and contains:
              (sortable_timestamp, date_str, time_str, sender, text_content)
    """
    print(f" - Processing {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"   [Warning] File not found: {file_path}. Skipping.")
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    messages = soup.find_all('div', class_='message')

    extracted_data = []

    for message in messages:
        sender_element = message.find('div', class_='from_name')
        timestamp_div = message.find('div', class_="pull_right date details")

        # Skip messages that don't have a sender or timestamp, as they can't be sorted or formatted.
        if sender_element is None or timestamp_div is None or 'title' not in timestamp_div.attrs:
            continue

        sender = sender_element.text.strip()
        timestamp = timestamp_div['title']  # Expected format: DD.MM.YYYY HH:MM:SS

        # Original date and time strings for the final output
        date_str = timestamp[:10]
        time_str = timestamp[11:19]

        # Create a sortable timestamp string in YYYY-MM-DD HH:MM:SS format
        sortable_ts = f"{timestamp[6:10]}-{timestamp[3:5]}-{timestamp[0:2]} {time_str}"

        text_element = message.find('div', class_='text')
        media_element = message.find('div', class_='media_wrap')
        text_content = ""

        if media_element:
            title_element = media_element.find('div', class_='title bold')
            description_element = media_element.find('div', class_='description')
            status_element = media_element.find('div', class_='status details')

            if title_element and description_element and status_element:
                media_title = title_element.text.strip()
                media_description = description_element.text.strip()
                media_status = status_element.text.strip()
                text_content = f"Media: {media_title} - {media_description} ({media_status})"
            else:
                continue  # Skip if media details are incomplete
        elif text_element:
            text_content = text_element.text.strip()
        else:
            continue  # Skip messages without text or media information

        # Add the structured message data to our list if it has content
        if text_content:
             extracted_data.append((sortable_ts, date_str, time_str, sender, text_content))

    return extracted_data

def main():
    """
    Main function to orchestrate the transformation of multiple HTML files
    into a single, sorted WhatsApp chat file.
    """
    # 1. Define the range of files to process.
    # This will generate a list like: ['messages.html', 'messages1.html', ..., 'messages94.html']
    base_name = 'messages'
    file_count = 94

    file_paths = [f'{base_name}.html']
    file_paths.extend([f'{base_name}{i}.html' for i in range(1, file_count + 1)])

    # 2. Process all specified HTML files and aggregate the messages
    all_messages = []
    print("Starting to process HTML files...")
    for path in file_paths:
        if os.path.exists(path):
             messages_from_file = process_html_file(path)
             all_messages.extend(messages_from_file)
        # If file doesn't exist, we just silently skip it.
        # The process_html_file function will handle explicit FileNotFoundError logging if needed.

    if not all_messages:
        print("\nNo messages were found in any of the HTML files. Exiting.")
        return

    # 3. Sort all collected messages by timestamp to ensure chronological order
    print("\nAll files read. Sorting messages by date and time...")
    all_messages.sort(key=lambda msg: msg[0])

    # 4. Format the sorted messages into the final WhatsApp chat string
    # We join with '\n' at the end for efficiency
    whatsapp_chat_lines = []
    for _, date_str, time_str, sender, text in all_messages:
        whatsapp_chat_lines.append(f'[{date_str}, {time_str}] {sender}: {text}')

    final_output = '\n'.join(whatsapp_chat_lines)

    # 5. Save the transformed chat to a single file
    output_filename = '_chat.txt'
    print(f"Writing sorted chat to {output_filename}...")
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(final_output)

    print(f'\nTransformation complete! All messages have been merged and saved to {output_filename}')

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
    input('\nPress Enter to exit...')
