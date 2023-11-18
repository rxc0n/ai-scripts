import language_tool_python
from pynput import keyboard

class GrammarCorrector:
    def __init__(self):
        # Initialize LanguageTool for grammar correction
        self.tool = language_tool_python.LanguageTool('en-US')

        # Initialize variables for real-time typing correction
        self.current_text = ''
        self.current_correction = ''

    def on_key_release(self, key):
        # Check if the key is alphanumeric or a space
        if hasattr(key, 'char') and (key.char.isalnum() or key.char.isspace()):
            # Update the current text
            self.current_text += key.char

            # Perform real-time grammar correction
            self.current_correction = self.correct_grammar(self.current_text)

            # Print the corrected text
            print(f'\rCorrected: {self.current_correction}', end='', flush=True)

    def correct_grammar(self, text):
        # Perform grammar correction using LanguageTool
        matches = self.tool.check(text)
        corrected_text = self.tool.correct(text, matches)

        return corrected_text

    def start(self):
        # Monitor keypress events
        with keyboard.Listener(on_release=self.on_key_release) as listener:
            listener.join()

if __name__ == "__main__":
    # Create GrammarCorrector instance
    corrector = GrammarCorrector()

    # Start real-time correction
    corrector.start()
