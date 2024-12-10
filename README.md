## Gemini Chat App - A Streamlit Interface

This project provides a user-friendly interface for interacting with Google's generative AI model, Gemini, using Streamlit.

### Features

* Select a pre-trained Gemini model from the sidebar.
* Adjust the temperature parameter to control the creativity of the generated responses.
* Enter your message in the chat box.
* Receive responses from Gemini, displayed in a chat history format.
* Track the total token usage for each conversation.


### Requirements

* Python 3.x
* `streamlit` package
* `google-generativeai` package
* `.env` file with your Google Cloud API key (optional, for paid models)

**Note:** To use paid models, you'll need a Google Cloud account and a billing plan enabled.


### Installation

1. Install the required packages:

   ```bash
   pip install streamlit google-generativeai
   ```

2. (Optional) Create a `.env` file and store your Google Cloud API key under the variable name `API_KEY`.


### Usage

1. Run the script:

   ```bash
   streamlit run app.py
   ```

2. (Optional) Select a different model and adjust the temperature setting in the sidebar.
3. Enter your message in the chat box and press Enter.
4. Observe the response from Gemini displayed below your message.

**Note:** Free models have a usage limit of 1 million tokens per month. The sidebar displays the total tokens used during your current chat session.

### Explanation of the Code

The code utilizes Streamlit to create a user interface with functionalities like:

* Selecting the model and adjusting temperature through the sidebar.
* Displaying chat history in a user-friendly format.
* Tracking and displaying total token usage.
* Handling user input, sending it to the model, and displaying the response.

For a deeper understanding of the code, refer to the specific functionalities of Streamlit (`st`) and `google.generativeai` packages in their respective documentations.


### Contributing

We welcome contributions to this project! Feel free to fork the repository and submit pull requests with your enhancements.
