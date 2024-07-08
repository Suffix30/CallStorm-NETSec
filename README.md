
# CallStorm-NETSec 📞🌩️

CallStorm is a powerful call flooding tool designed for educational purposes. It leverages multiple calling services to simulate high-volume call scenarios, aiding in stress testing and other related activities. The project features a user-friendly GUI built with CustomTkinter.

## Features

- **Multi-Service Support**: Integrates with Twilio, Plivo, Nexmo, and Sinch for diverse call flooding capabilities.
- **Random Number Generation**: Generate fake numbers to display as caller IDs.
- **Configurable Targeting**: Easily specify the target number for the call flood.
- **Intuitive GUI**: Simple and intuitive interface for easy operation.
- **Start/Stop Control**: Start or stop the call flooding process at any time.

## Installation

### Prerequisites

- Python 3.8+
- Pip

### Clone the Repository

```bash
git clone https://github.com/Suffix30/CallStorm.git
```
```
cd CallStorm
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configuration

Before running the application, you need to configure the service credentials and other settings. Update the \`config.py\` file located in the \`Config_Files\` directory with your service credentials and other relevant configurations.

### Config_Files/config.py

```python
voiceml = "URL_TO_YOUR_VOICEML_FILE"
sourceNumbers = []
```

### Usage

#### Running the Application

Run the main script to launch the GUI.

```bash
python callstorm.py
```

#### Using the GUI

- **Target Number**: Enter the phone number you want to flood with calls.
- **Number of Fake Numbers**: Specify how many fake numbers to generate.
- **Generate Numbers**: Click to generate and update the fake numbers in the configuration.
- **Service Selection**: Choose one or more calling services (Twilio, Plivo, Nexmo, Sinch) to use for the call flood.
- **Start Flood**: Click to start the call flooding process.
- **Stop Flood**: Click to stop the call flooding process.

### Directory Structure

```
CallStorm/
│   ├── callstorm.py
│   ├── requirements.txt
│   ├── Call_Services/
│   │   ├── nexmo_call.py
│   │   ├── plivo_call.py
│   │   ├── sinch_call.py
│   │   ├── twilio_call.py
│   ├── Config_Files/
│   │   ├── config.py
│   ├── Number_Generator/
│   │   ├── number_generator.py
│   ├── Source_Numbers/
│   │   ├── source_numbers.pyt
└── README.md
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

### Steps to Contribute

1. Fork the Project
2. Create your Feature Branch (\`git checkout -b feature/AmazingFeature\`)
3. Commit your Changes (\`git commit -m 'Add some AmazingFeature'\`)
4. Push to the Branch (\`git push origin feature/AmazingFeature\`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Disclaimer

This tool is intended for educational purposes only. The use of CallStorm for malicious activities, harassment, or any illegal purposes is strictly prohibited and against the intended use of this tool.
