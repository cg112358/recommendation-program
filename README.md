# Recommendation Program

## Overview
The Recommendation Program is a simple command-line application that suggests categories and specific recommendations based on user input. Users can explore various topics such as restaurants, movies, books, television, and podcasts by entering letters or words into the terminal.

## Features
- User-friendly interface for entering queries.
- Dynamic search functionality to provide relevant recommendations.
- Categorized dataset for diverse topics.
- Easy to extend and modify for additional categories or recommendations.

## Project Structure
```
recommendation-program
├── src
│   ├── main.py                # Entry point of the program
│   ├── data
│   │   └── recommendations.json # Dataset of recommendations
│   ├── algorithms
│   │   └── search.py           # Search algorithm for recommendations
│   └── utils
│       └── helpers.py          # Utility functions for data processing
├── tests
│   └── test_main.py            # Unit tests for the main program logic
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
└── blog_post.md                 # Technical blog post
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/cg112358/recommendation-program.git
   ```
2. Navigate to the project directory:
   ```
   cd recommendation-program
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the recommendation program, execute the following command:
```
python src/main.py
```
Follow the prompts to enter your query and receive recommendations.

## Contribution
Feel free to fork the repository and submit pull requests for any improvements or additional features.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.