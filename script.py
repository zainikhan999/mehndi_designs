from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import streamlit as st
from dotenv import load_dotenv
import os


# Step 1: Configure your API key
# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")
client = genai.Client(api_key=api_key)  # Replace with your actual API key

# Step 2: Set up Streamlit UI
st.title("Floral Mehndi Design Generator")
st.write("Enter your command to generate a floral mehndi design:")

# Add dropdown for Mehndi type selection with brief description
mehndi_type = st.selectbox(
    "Select the Type of Mehndi Design",
    [
        "Pakistani Mehndi Design - Intricate patterns with floral and geometric motifs.",
        "Arabic Mehndi Design - Bold, floral patterns with long, flowing lines.",
        "Indian Mehndi Design - Detailed designs with peacock motifs and rich patterns.",
        "Portrait Mehndi Design - Artistic designs with portraits or faces.",
        "Moroccan Mehndi Design - Geometric and symmetric designs with bold patterns.",
        "Bridal Mehndi Design - Complex designs typically used for weddings, covering hands and feet.",
        "Jewellery Mehndi Design - Mehndi designs inspired by jewelry patterns, often with elegant curves.",
        "Tattoo Mehndi Design - Modern, minimalist designs often resembling tattoos.",
        "Western-style Mehndi - Contemporary designs with a fusion of mehndi and Western art.",
        "African Mehndi Design - Bold and simple designs with circular and linear patterns.",
        "Punjabi Mehndi Design - Vibrant, bold patterns with motifs from Punjabi culture."
    ]
)

# Add Hand Type selection
hand_type = st.selectbox(
    "Select the Age Range of the Hand Type",
    [
        "Toddlerhood (2-4 years)",
        "Childhood (5-12 years)",
        "Adolescence (13-19 years)",
        "Young Adulthood (20-39 years)",
        "Middle Adulthood (40-59 years)",
        "Senior Adulthood (60+ years)"
    ]
)

# Add Occasion selection
occasion = st.selectbox("Select Occasion", ['Wedding', 'Festival', 'Party', 'Casual', 'Other'])

# Add Complexity selection
complexity = st.slider(
    "Select the Complexity of Design",
    1,  # Minimum complexity
    5,  # Maximum complexity
    3,  # Default value
    step=1,  # Step size
    format="%d",  # Display format
    help="1 is Simple, 5 is Complex"
)

# User input for custom details
user_command = st.text_input("Enter any custom details you want to include in the design:")

# Add number of images to generate
num_images = st.slider("Select Number of Images", min_value=1, max_value=10, value=1)

# Function to add a white background to images with transparency
def add_white_background(img):
    # Ensure the image is in RGBA format (it will include transparency)
    img = img.convert("RGBA")

    # Check if the image has an alpha channel (transparency)
    if img.mode == 'RGBA':
        # Create a white background image with the same size as the original image
        background = Image.new("RGBA", img.size, (255, 255, 255, 255))
        # Paste the original image onto the white background using its alpha channel as mask
        background.paste(img, (0, 0), img)
        # Convert back to RGB (no alpha channel, no transparency)
        img = background.convert("RGB")
    else:
        # If no alpha channel exists, just convert directly to RGB
        img = img.convert("RGB")
    return img

# Function to determine the hand description based on the hand type selected
def get_hand_description(hand_type):
    if hand_type == "Toddlerhood (2-4 years)":
        return "a toddler's hand, including both the palm and the back of the hand"
    elif hand_type == "Childhood (5-12 years)":
        return "a child's hand, including both the palm and the back of the hand"
    elif hand_type == "Adolescence (13-19 years)":
        return "a teenager's hand, including both the palm and the back of the hand"
    elif hand_type == "Young Adulthood (20-39 years)":
        return "an adult's hand, including both the palm and the back of the hand"
    elif hand_type == "Middle Adulthood (40-59 years)":
        return "a middle-aged adult's hand, including both the palm and the back of the hand"
    elif hand_type == "Senior Adulthood (60+ years)":
        return "a senior adult's hand, including both the palm and the back of the hand"
    else:
        return "an adult's hand, including both the palm and the back of the hand"  # Default case for adult hands

# Button to generate the content
if st.button("Generate"):
    if user_command:
        # Get the hand type description based on the user's selection
        hand_description = get_hand_description(hand_type)

        # Append the hand type, occasion, mehndi type, and complexity info to the user command
# Append the hand type, occasion, mehndi type, and complexity info to the user command
        detailed_command = (
           f"You are an expert Mehndi artist. Generate a clear and realistic image of ONE human hand only — "
            "the hand must have EXACTLY 5 distinct fingers: 1 thumb and 4 fingers. No extra fingers, double thumbs, or merged fingers. "
           "The fingers and thumb should be naturally spaced, and the arm must be included. Do NOT show two hands or mirrored views. "
            f"The hand must clearly resemble this description: {hand_description}. "
           "Show only a single hand with a white background — no home or parlor backgrounds. "
            "Ensure the palm AND the back of the hand are visible in the design (you may use a 3D-style view or split-view layout). "
            f"Generate a {mehndi_type.split(' - ')[0]} style Mehndi design suitable for a {occasion}, "
             f"with a {complexity} complexity level. "
            "Do NOT generate more than one hand or any other object in the image.")

        st.write("Processing your request...")

        # Initialize list to hold images
        images = []

        # Loop to generate multiple images
        for _ in range(num_images):
            try:
                # Call the AI model to generate content based on the user command
                response = client.models.generate_content(
                    model="gemini-2.0-flash-exp-image-generation",
                    contents=detailed_command,
                    config=genai.types.GenerateContentConfig(
                        response_modalities=['Text', 'Image']  # Requesting both Text and Image
                    )
                )

                # Process the response to get images
                for part in response.candidates[0].content.parts:
                    if part.inline_data is not None:
                        image = Image.open(BytesIO(part.inline_data.data))  # Convert byte data to image
                        
                        # Ensure the image has a white background
                        image = add_white_background(image)
                        
                        images.append(image)  # Add image to the list

            except Exception as e:
                st.error(f"Error: {e}")
                break

        # Check if images were generated
        if images:
            # Set the fixed width and height for each image (larger size now)
            image_width = 600  # Larger width in pixels
            image_height = 700  # Larger height in pixels

            # Display images in a single row, with fixed width and height
            cols = st.columns(len(images))  # Create columns equal to the number of images

            for idx, img in enumerate(images):
                # Resize the image to fit the desired width and height
                img = img.resize((image_width, image_height))

                with cols[idx]:
                    st.image(img, caption=f"Generated Mehndi Design {idx + 1}", use_container_width=False)

        else:
            st.error("No images generated. Please try again.")
    else:
        st.warning("Please enter a command.")
