# Force - Advanced Web Authentication Testing Tool

![Force Banner](https://img.shields.io/badge/FORCE-Web%20Brute%20Forcer-red)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

```
███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
█████╗  ██║   ██║██████╔╝██║     █████╗  
██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
```

## ⚠️ Legal Disclaimer

**This tool is developed for authorized penetration testing and security research ONLY.**  
Unauthorized use against systems without explicit permission is illegal and unethical.  
The author assumes no liability for any misuse of this software.

## Overview

Force is a high-performance web authentication testing tool designed for security professionals. Built with multithreading capabilities, it efficiently evaluates the resilience of web application login mechanisms against dictionary-based attacks.

## Features

- Multi-threaded architecture for optimized performance
- Adaptive thread management system
- Session-based authentication handling
- Real-time progress monitoring with color-coded output
- Comprehensive success metrics and statistics
- Graceful error handling and session management

## Technical Implementation

Force operates by:

1. **Session Management**: Establishes and maintains an authenticated session using the provided PHPSESSID cookie
2. **Request Parameterization**: Dynamically constructs login requests with target username and passwords from the wordlist
3. **Response Analysis**: Parses HTTP responses to detect authentication success patterns
4. **Concurrent Processing**: Leverages Python's ThreadPoolExecutor to distribute workload across multiple threads
5. **Success Detection**: Identifies successful authentication by analyzing response content for absence of failure indicators

The tool uses GET requests with query parameters, ideal for testing applications like DVWA. The concurrent processing architecture allows it to efficiently test hundreds or thousands of passwords while maintaining a manageable footprint on the target system.

## Installation

```bash
# Clone the repository
git clone https://github.com/ySergeb250/brute.git
cd force

# The tool requires only the requests library
pip install requests

# Run the tool
python3 brute.py
```

## Usage

```bash
# Execute the tool
python3 brute.py
```

You will be prompted for:

- **Target URL**: The authentication endpoint (e.g., http://target.com/login)
- **Username**: Account identifier to test against
- **Wordlist Path**: Path to dictionary file containing candidate passwords
- **PHPSESSID cookie**: Valid session identifier for maintaining authentication context
- **Threads**: Number of concurrent workers (5-10 recommended for balance of speed and stability)

## Example Workflow

1. **Reconnaissance**: Identify the target login endpoint and parameter structure
2. **Session Preparation**: Obtain a valid PHPSESSID by logging into the application
3. **Execution**: Run Force with appropriate parameters
4. **Analysis**: Review results and performance metrics

```
[CONFIGURATION]
[?] Target URL: http://target.com/login.php
[?] Username to brute force: admin
[?] Path to wordlist file: /path/to/wordlist.txt
[?] PHPSESSID cookie: a1b2c3d4e5f6g7h8i9j0
[?] Threads: 8

[ATTACK STARTED]
[*] Target: http://target.com/login.php
[*] Username: admin
[*] Wordlist: /path/to/wordlist.txt
[*] Threads: 8
Press Ctrl+C to stop

[+] CRACKED! Password found: Passw0rd!

[STATISTICS]
[*] Time elapsed: 5.73 seconds
[*] Passwords tried: 289
[*] Speed: 50.44 attempts/second
```

![Brute](https://github.com/Sergeb250/web-brute-forcer/blob/df0eb639bb305e8de8ca7e33d372e41aeaacc742/bruteImages/Screenshot%20(28).png)
![Brute]()

## Professional Usage Guidelines

- Conduct testing only with proper authorization and documentation
- Implement appropriate timing controls to prevent DoS conditions
- Consider the target system's logging capabilities and incident response procedures
- Document all findings according to professional security assessment standards
- Follow responsible disclosure protocols for any vulnerabilities discovered

## Contributing

Contributions are welcome through pull requests. When contributing:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/enhancement`)
3. Implement your changes with appropriate documentation
4. Commit with clear, descriptive messages
5. Submit a pull request detailing the changes and their benefits

## License

This project is licensed under the MIT License.

## Acknowledgments

- Developed by hackx (sergeB)
- Created for professional security assessment operations
