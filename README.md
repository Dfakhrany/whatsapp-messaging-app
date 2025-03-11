# WhatsApp Messaging Application

This project is a WhatsApp messaging application that integrates with WhatsApp Web, providing a range of features for message and contact management, browser automation, and enhanced user experience.

## Features

- **Browser Automation**: Utilizes Selenium for automating interactions with WhatsApp Web, including session management and headless mode support.
- **Message Management**: Create, save, and schedule messages with rich text formatting and queuing systems.
- **Contact Management**: Manage contacts with features like bulk input, duplicate removal, and CSV/Excel import.
- **Media Handling**: Add attachments, edit images, and compress videos for sharing.
- **Reporting and Analytics**: Generate reports on message delivery and open rates, with export options to Excel/CSV.
- **Security Enhancements**: Implement two-factor authentication, end-to-end encryption, and user permissions management.
- **Cloud Integration**: Backup messages and contacts to the cloud, with synchronization across devices.
- **Modern UI**: Built with CustomTkinter for an appealing and user-friendly interface.
- **Error Handling**: Robust error handling and logging, including automatic reconnection for WhatsApp disconnections.
- **Testing Tools**: Includes tools for verifying setup and testing functionalities without sending messages.

## Key Features

- **GUI-Based Interface**:
    - The program provides a user-friendly interface with buttons for connecting to WhatsApp, adding messages, attaching files, and starting/stopping the sending process.
    - It supports scrolling for large lists of contacts and messages.

- **Message Sending**:
    - Users can input multiple phone numbers and messages.
    - Messages are sent in rotation, and the program handles delays and breaks between messages.

- **Attachment Handling**:
    - Users can add and remove attachments (e.g., images, documents) to be sent along with messages.

- **Progress and Reporting**:
    - The program tracks the status of each message (sent, failed, pending) and displays it in real-time.
    - It generates a detailed report at the end of the process, including success and failure counts.

- **Language Support**:
    - The GUI can switch between English and Arabic, with text alignment adjusted accordingly.

- **Session Management**:
    - Users can choose to reuse an existing WhatsApp session or start a new one.

- **Settings Customization**:
    - Users can configure minimum and maximum delays between messages, break intervals, and break durations.
    
## Installation

To install the application, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/whatsapp-messaging-app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd whatsapp-messaging-app
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```sh
    python app.py
    ```
2. Follow the on-screen instructions to connect to WhatsApp Web and start using the features.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.