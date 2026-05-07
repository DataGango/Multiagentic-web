import os
import sys
import re
from google import genai

def generate_project(prompt, output_dir="output"):
    # Initialize the client. It will automatically use the GEMINI_API_KEY environment variable.
    client = genai.Client()
    
    system_instruction = """
    You are an expert multi-language software developer and web agent. You generate complete projects containing multiple files.
    You support ALL programming languages (Java, Python, HTML, JS, C++, Go, etc.) and test scripts.
    The user will describe the project. You must output the code for each file using the following format exactly:
    
    ==== FILE: path/to/filename.ext ====
    <file contents here>
    ====================================
    
    Do NOT use markdown code blocks like ```java around the content. Just provide the raw content between the boundary markers.
    Ensure that you generate ALL necessary files. For example, if asked for Java and HTML with test scripts, provide the backend Java files, HTML frontend files, and Java JUnit test files.
    """
    
    print(f"Generating multi-language project for prompt: '{prompt}'...")
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_instruction,
                temperature=0.7,
            )
        )
        
        text_content = response.text
        
        # Parse the response to extract multiple files
        pattern = re.compile(r'==== FILE:\s*(.*?)\s*====\n(.*?)(?=\n==== FILE:|\Z|====================================)', re.DOTALL)
        matches = pattern.findall(text_content)
        
        os.makedirs(output_dir, exist_ok=True)
        
        if not matches:
            print("Warning: Could not parse specific files. Saving raw output.")
            raw_path = os.path.join(output_dir, "raw_output.txt")
            with open(raw_path, "w") as f:
                f.write(text_content)
            print(f"Saved to {raw_path}")
            return
            
        for file_path, content in matches:
            file_path = file_path.strip()
            content = content.strip()
            
            # Remove markdown blocks if the model accidentally included them
            if content.startswith("```"):
                lines = content.split('\n')
                if len(lines) > 1:
                    content = '\n'.join(lines[1:])
            if content.endswith("```"):
                content = content[:-3].strip()
            
            full_path = os.path.join(output_dir, file_path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            
            with open(full_path, "w") as f:
                f.write(content)
                
            print(f"Generated: {full_path}")
            
        print(f"\nProject successfully generated in the '{output_dir}' directory.")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agent.py '<prompt_describing_project>' [output_dir]")
        sys.exit(1)
        
    user_prompt = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"
    generate_project(user_prompt, output_dir)
